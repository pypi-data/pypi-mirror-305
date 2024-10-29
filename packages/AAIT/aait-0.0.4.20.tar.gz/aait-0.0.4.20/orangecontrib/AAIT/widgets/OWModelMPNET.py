import os
import sys

from AnyQt.QtWidgets import QApplication, QLabel
from Orange.widgets import widget
from Orange.widgets.utils.signals import Output
from sentence_transformers import SentenceTransformer

from ..utils import SimpleDialogQt, thread_management
from ..utils.import_uic import uic
from ..utils.initialize_from_ini import apply_modification_from_python_file
from ..utils.MetManagement import GetFromRemote, get_local_store_path


#@apply_modification_from_python_file()
class OWModelMPNET(widget.OWWidget):
    name = "Model - Embeddings - MPNET"
    description = "Load the embeddings model all-mpnet-base-v2 from the AAIT Store"
    icon = "icons/owembeddingsmodel.svg"
    if "site-packages/Orange/widgets" in os.path.dirname(os.path.abspath(__file__)).replace("\\", "/"):
        icon = "icons_dev/owembeddingsmodel.svg"
    gui = os.path.join(os.path.dirname(os.path.abspath(__file__)), "designer/owembeddingsmodel.ui")
    want_control_area = False

    class Outputs:
        model = Output("Model", SentenceTransformer, auto_summary=False)

    def __init__(self):
        super().__init__()
        # Path management
        self.current_ows = ""
        local_store_path = get_local_store_path()
        model_name = "all-mpnet-base-v2"
        self.model_path = os.path.join(local_store_path, "Models", "NLP", model_name)
        self.model = None

        # Qt Management
        self.setFixedWidth(470)
        self.setFixedHeight(300)
        uic.loadUi(self.gui, self)
        if not os.path.exists(self.model_path):
            if not SimpleDialogQt.BoxYesNo("Model isn't in your computer. Do you want to download it from AAIT store?"):
                return
            try:
                GetFromRemote("Advanced Text Embeddings")
            except:  # TODO ciblage de l'erreur
                SimpleDialogQt.BoxError("Unable to get the Model.")
                return
        # Data Management
        self.progressBarInit()
        self.thread = thread_management.Thread(self.load_sentence_transformer, self.model_path)
        self.thread.finish.connect(self.handle_loading_finish)
        self.thread.start()

    def load_sentence_transformer(self, model_path):
        self.model = SentenceTransformer(model_path)

    def handle_loading_finish(self):
        if self.model is not None:
            self.Outputs.model.send(self.model)
        else:
            SimpleDialogQt.BoxError("An Error Occurred when loading model.")
            self.Outputs.model.send(None)
        self.progressBarFinished()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_widget = OWModelMPNET()
    my_widget.show()
    app.exec_()
