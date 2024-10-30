import pathlib
import tempfile


from IPython.display import display

import ipywidgets as ipw

# from ..euphonic.bands_pdos import *
from .intensity_maps import (
    generate_force_constant_instance,
    export_euphonic_data,  # noqa: F401
)
from .euphonic_single_crystal_widgets import SingleCrystalFullWidget
from .euphonic_powder_widgets import PowderFullWidget
from .euphonic_q_planes_widgets import QSectionFullWidget


###### START for detached app:

# spinner for waiting time (supercell estimations)
spinner_html = """
<style>
@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.spinner {
  display: inline-block;
  width: 15px;
  height: 15px;
}

.spinner div {
  width: 100%;
  height: 100%;
  border: 4px solid #f3f3f3;
  border-top: 4px solid #3498db;
  border-radius: 50%;
  animation: spin 1s linear infinite;
}
</style>
<div class="spinner">
  <div></div>
</div>
"""


# Upload buttons
class UploadPhonopyYamlWidget(ipw.FileUpload):
    def __init__(self, **kwargs):
        super().__init__(
            description="upload phonopy YAML file",
            multiple=False,
            layout={"width": "initial"},
        )


class UploadForceConstantsHdf5Widget(ipw.FileUpload):
    def __init__(self, **kwargs):
        super().__init__(
            description="upload force constants HDF5 file",
            multiple=False,
            layout={"width": "initial"},
        )


class UploadPhonopyWidget(ipw.HBox):
    def __init__(self, **kwargs):
        self.upload_phonopy_yaml = UploadPhonopyYamlWidget(**kwargs)
        self.upload_phonopy_hdf5 = UploadForceConstantsHdf5Widget(**kwargs)

        self.reset_uploads = ipw.Button(
            description="Discard uploaded files",
            icon="pencil",
            button_style="warning",
            disabled=False,
            layout=ipw.Layout(width="auto"),
        )

        super().__init__(
            children=[
                self.upload_phonopy_yaml,
                self.upload_phonopy_hdf5,
                self.reset_uploads,
            ],
            **kwargs,
        )

    def _read_phonopy_files(self, fname, phonopy_yaml_content, fc_hdf5_content=None):
        suffix = "".join(pathlib.Path(fname).suffixes)

        with tempfile.NamedTemporaryFile(suffix=suffix) as temp_yaml:
            temp_yaml.write(phonopy_yaml_content)
            temp_yaml.flush()

            if fc_hdf5_content:
                with tempfile.NamedTemporaryFile(suffix=".hdf5") as temp_file:
                    temp_file.write(fc_hdf5_content)
                    temp_file.flush()
                    temp_hdf5_name = temp_file.name

                    try:
                        fc = generate_force_constant_instance(
                            path=pathlib.Path(fname),
                            summary_name=temp_yaml.name,
                            fc_name=temp_hdf5_name,
                        )
                    except ValueError:
                        return None

                    return fc
            else:
                temp_hdf5_name = None

                try:
                    fc = generate_force_constant_instance(
                        path=pathlib.Path(fname),
                        summary_name=temp_yaml.name,
                        # fc_name=temp_hdf5_name,
                    )
                except ValueError:
                    return None

                return fc


#### END for detached app


##### START OVERALL WIDGET TO DISPLAY EVERYTHING:


class EuphonicSuperWidget(ipw.VBox):
    """
    Widget that will include everything,
    from the upload widget to the tabs with single crystal and powder predictions.
    In between, we trigger the initialization of plots via a button.
    """

    def __init__(self, mode="aiidalab-qe app plugin", fc=None, q_path=None):
        """
        Initialize the Euphonic utility class.
        Parameters:
        -----------
        mode : str, optional
            The mode of operation, default is "aiidalab-qe app plugin".
        fc : optional
            Force constants, default is None.
        q_path : optional
            Q-path for phonon calculations, default is None. If Low-D system, this can be provided.
            It is the same path obtained for the PhonopyCalculation of the phonopy_bands.
        Attributes:
        -----------
        mode : str
            The mode of operation.
        upload_widget : UploadPhonopyWidget
            Widget for uploading phonopy files.
        fc_hdf5_content : None
            Content of the force constants HDF5 file.
        tab_widget : ipw.Tab
            Tab widget for different views.
        plot_button : ipw.Button
            Button to initialize INS data.
        fc : optional
            Force constants if provided.
        """

        self.mode = mode

        self.upload_widget = UploadPhonopyWidget()
        self.upload_widget.reset_uploads.on_click(self._on_reset_uploads_button_clicked)
        self.fc_hdf5_content = None

        self.tab_widget = ipw.Tab()
        self.tab_widget.layout.display = "none"
        self.tab_widget.set_title(0, "Single crystal")
        self.tab_widget.set_title(1, "Powder sample")
        self.tab_widget.set_title(2, "Q-plane view")
        self.tab_widget.children = ()

        if fc:
            self.fc = fc

        self.q_path = q_path

        self.plot_button = ipw.Button(
            description="Initialise INS data",
            icon="pencil",
            button_style="primary",
            disabled=True,
            layout=ipw.Layout(width="auto"),
        )
        self.plot_button.on_click(self._on_first_plot_button_clicked)

        self.loading_widget = ipw.HTML(
            value=spinner_html,
        )
        self.loading_widget.layout.display = "none"

        if self.mode == "aiidalab-qe app plugin":
            self.upload_widget.layout.display = "none"
            self.plot_button.disabled = False
        else:
            self.upload_widget.children[0].observe(self._on_upload_yaml, "_counter")
            self.upload_widget.children[1].observe(self._on_upload_hdf5, "_counter")

        super().__init__(
            children=[
                self.upload_widget,
                self.plot_button,
                self.loading_widget,
                self.tab_widget,
            ],
        )

    def _on_reset_uploads_button_clicked(self, change):
        self.upload_widget.upload_phonopy_yaml.value.clear()
        self.upload_widget.upload_phonopy_yaml._counter = 0
        self.upload_widget.upload_phonopy_hdf5.value.clear()
        self.upload_widget.upload_phonopy_hdf5._counter = 0

        self.plot_button.layout.display = "block"
        self.plot_button.disabled = True

        self.tab_widget.children = ()

        self.tab_widget.layout.display = "none"

    def _on_upload_yaml(self, change):
        if change["new"] != change["old"]:
            for fname in self.upload_widget.children[
                0
            ].value.keys():  # always one key because I allow only one file at the time.
                self.fname = fname
                self.phonopy_yaml_content = self.upload_widget.children[0].value[fname][
                    "content"
                ]

        if self.plot_button.disabled:
            self.plot_button.disabled = False

    def _on_upload_hdf5(self, change):
        if change["new"] != change["old"]:
            for fname in self.upload_widget.children[1].value.keys():
                self.fc_hdf5_content = self.upload_widget.children[1].value[fname][
                    "content"
                ]

    def _generate_force_constants(
        self,
    ):
        if self.mode == "aiidalab-qe app plugin":
            return self.fc

        else:
            fc = self.upload_widget._read_phonopy_files(
                fname=self.fname,
                phonopy_yaml_content=self.phonopy_yaml_content,
                fc_hdf5_content=self.fc_hdf5_content,
            )

            return fc

    def _on_first_plot_button_clicked(self, change=None):
        # It creates the widgets
        self.plot_button.layout.display = "none"

        self.loading_widget.layout.display = "block"

        self.fc = self._generate_force_constants()

        # I first initialise this widget, to then have the 0K ref for the other two.
        singlecrystalwidget = SingleCrystalFullWidget(self.fc, self.q_path)

        self.tab_widget.children = (
            singlecrystalwidget,
            PowderFullWidget(
                self.fc, intensity_ref_0K=singlecrystalwidget.intensity_ref_0K
            ),
            QSectionFullWidget(
                self.fc, intensity_ref_0K=singlecrystalwidget.intensity_ref_0K
            ),
        )

        self.loading_widget.layout.display = "none"

        self.tab_widget.layout.display = "block"


class DownloadYamlHdf5Widget(ipw.HBox):
    def __init__(self, phonopy_node, **kwargs):
        self.download_button = ipw.Button(
            description="Download phonopy data",
            icon="pencil",
            button_style="primary",
            disabled=False,
            layout=ipw.Layout(width="auto"),
        )
        self.download_button.on_click(self.download_data)
        self.node = phonopy_node

        super().__init__(
            children=[
                self.download_button,
            ],
        )

    def download_data(self, _=None):
        """
        Download both the phonopy.yaml and fc.hdf5 files.
        """
        phonopy_yaml, fc_hdf5 = generate_force_constant_instance(
            self.node, mode="download"
        )
        self._download(payload=phonopy_yaml, filename="phonopy" + ".yaml")
        self._download(payload=fc_hdf5, filename="fc" + ".hdf5")

    @staticmethod
    def _download(payload, filename):
        from IPython.display import Javascript

        javas = Javascript(
            """
            var link = document.createElement('a');
            link.href = 'data:text/json;charset=utf-8;base64,{payload}'
            link.download = "{filename}"
            document.body.appendChild(link);
            link.click();
            document.body.removeChild(link);
            """.format(payload=payload, filename=filename)
        )
        display(javas)
