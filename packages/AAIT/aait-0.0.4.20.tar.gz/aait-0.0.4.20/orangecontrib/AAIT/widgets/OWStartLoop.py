import copy
import os
import sys

import Orange.data
from AnyQt.QtWidgets import QPushButton
from Orange.data import Domain, StringVariable
from Orange.widgets.utils.signals import Input, Output
from Orange.widgets.widget import Output, OWWidget

# from ..utils import check_data_in


class LoopStartWidget(OWWidget):
    name = "Loop Start"
    description = "Widget to start a loop with data table input and output."
    icon = "icons_dev/startloop.png"
    gui = os.path.join(os.path.dirname(os.path.abspath(__file__)), "designer/owstartloop.ui")
    want_control_area = False
    priority = 10

    class Inputs:
        data_in = Input("Data In", Orange.data.Table)

    class Outputs:
        data_out = Output("Data Out", Orange.data.Table)
        out_pointer = Output("Begin of the Loop Do-While", str, auto_summary=False)

    def __init__(self):
        super().__init__()
        self.data = None

        # Ajouter un bouton d'activation/désactivation
        self.activate_button = QPushButton("Activer", self)
        self.activate_button.setCheckable(True)  # Le bouton peut être basculé entre états activé/désactivé
        ##################### A SUPPRIMER POUR DEV UNIQUEMENT#####################################
        self.activate_button.setChecked(True)  # Le bouton est activé par défaut
        ##################### A SUPPRIMER POUR DEV UNIQUEMENT#####################################
        self.activate_button.clicked.connect(self.on_activate_button_clicked)
        self.mainArea.layout().addWidget(self.activate_button)

        self.send_pointer()  # Sending pointer at initialization (only once is needed)

    def on_activate_button_clicked(self):
        if self.activate_button.isChecked():
            self.information("Le bouton est activé !")
            self.activate_button.setText("Désactiver")
        else:
            self.information("Le bouton est désactivé !")
            self.activate_button.setText("Activer")

    @Inputs.data_in
    def set_data(self, dataset):
        if dataset is None:
            print("No data received.")
            return
        self.error("")
        # #########################
        # if not check_data_in.check_all_data(self,data,["data_in","variable_sans_interet"],["StringVariable","ContinuousVariable"]):
        #     self.error("Error! check data in")
        # #########################
        # Validate the data types (only StringVariable or ContinuousVariable allowed)
        print(dataset)

        for el_domain in dataset.domain:
            if str(type(el_domain)) not in ["StringVariable", "ContinuousVariable"]:
                self.error(
                    f"Error {str(type(el_domain))}: This widget can only be used with StringVariable or ContinuousVariable")
                return

        # Make a deep copy of the dataset
        self.data = copy.deepcopy(dataset)
        print("\n=== StartLoop Entry ===")
        print("Number of lines ---->", self.get_nb_line())

        self.process_data()

    def get_nb_line(self):
        """Return the number of lines to be called from another widget."""
        return 0 if self.data is None else len(self.data)

    def get_column_name_and_type(self):
        """Return the name and type of 'data_in' to be called from another widget."""
        if self.data is None:
            return [[], []]
        column_names = []
        column_types = []
        for element in self.data.domain:
            column_names.append(str(element))
            column_types.append(str(type(element)))
        return column_names, column_types

    def process_data(self):
        """Main process executed when data is available."""
        # if self.data is not None:
        if self.data is not None and self.activate_button.isChecked():
            if 'data_out' not in [meta.name for meta in self.data.domain.metas]:
                self.add_data_out_column()
            self.Outputs.data_out.send(self.data)  # Sending the data
        else:
            print("No data sent. The activate button is not checked or no data received.")

    def add_data_out_column(self):
        """Add the 'data_out' column if it doesn't already exist."""
        print("Adding the 'data_out' column")
        data_out_column = StringVariable("data_out")
        new_domain = Domain(self.data.domain.attributes, self.data.domain.class_vars,
                            metas=self.data.domain.metas + (data_out_column,))
        new_data = Orange.data.Table.from_table(new_domain, self.data)

        for i in range(len(new_data)):
            new_data[i, new_data.domain["data_out"]] = ""
        self.data = new_data

    def send_pointer(self):
        """Send a pointer to the current class for the loop."""
        pointer = str(id(self))
        self.Outputs.out_pointer.send(pointer)


if __name__ == "__main__":
    from AnyQt.QtWidgets import QApplication

    app = QApplication(sys.argv)
    obj = LoopStartWidget()
    obj.show()
    app.exec_()