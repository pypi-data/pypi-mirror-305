import ctypes
import os
import sys

import Orange.data
from Orange.widgets.settings import Setting
from Orange.widgets.widget import Input, Output, OWWidget

# if "site-packages/Orange/widgets" in os.path.dirname(os.path.abspath(__file__)).replace("\\","/"):
#     from Orange.widgets.orangecontrib.AAIT.utils import check_data_in
# else:
#     from orangecontrib.AAIT.utils import check_data_in


class EndLoopWidget(OWWidget):
    name = "End Loop"
    description = "Widget to end a loop based on a predefined condition."
    icon = "icons/endloop.png"
    if "site-packages/Orange/widgets" in os.path.dirname(os.path.abspath(__file__)).replace("\\", "/"):
        icon = "icons_dev/endloop.png"

    gui = os.path.join(os.path.dirname(os.path.abspath(__file__)), "designer/owendloop.ui")
    want_control_area = False
    priority = 20

    class Inputs:
        in_data = Input("Data In", Orange.data.Table)
        in_pointer = Input("End of the Loop Do-While", str, auto_summary=False)

    class Outputs:
        out_data = Output("Data Out", Orange.data.Table)

    def __init__(self):
        super().__init__()
        self.data = None
        self.in_pointer = None

    @Inputs.in_data
    def set_data(self, data):
        if data is None:
            print("No data received in the end loop.")
            return
        self.error("")
        # #########################
        # if not check_data_in.check_all_data(self,data,["data_in","variable_sans_interet"],["StringVariable","ContinuousVariable"]):
        #     self.error("Error! check data in")
        # #########################
        if self.in_pointer is None:
            return
        print("\n=== EndLoop Entry ===")
        print("Number of lines ---->", self.get_nb_line_from_start())
        print("Name and type ---->", self.get_column_name_and_type_from_start())

        if data is not None:
            #self.data=data
            # Make a deep copy of the input table
            self.data = data#copy.deepcopy(data)
            # Check if the number of lines has changed
            print(self.get_nb_line())
            print(self.get_nb_line_from_start())
            if self.get_nb_line() != self.get_nb_line_from_start():
                self.error("Error! You can't change the number of lines in this version!")
                return
            # Check if column names and types have changed
            # if self.get_column_name_and_type() != self.get_column_name_and_type_from_start():
            #     self.error("Error! You can't change the column type or name! If you want to know why, call JC at 0635283519")
            #     return
            print("affiche avant proCess")
            self.give_args_to_input()
            self.process_data_based_on_iter()
            self.check_loop_condition()
            print("affiche apres proCess")





        else:
            print("No data received.")
            self.data = None
        print("\n=== EndLoop Exit ===")

    @Inputs.in_pointer
    def set_pointer(self, pointer):
        self.in_pointer = int(pointer) if pointer else None

    def get_column_name_and_type_from_start(self):
        if self.in_pointer is not None:
            result = ctypes.cast(int(self.in_pointer), ctypes.py_object).value.get_column_name_and_type()
        return result

    def get_nb_line_from_start(self):
        result = 0
        if self.in_pointer is not None:
            result = ctypes.cast(int(self.in_pointer), ctypes.py_object).value.get_nb_line()
        return result

    def get_nb_line(self):
        # Return the number of lines to compare with another widget
        if self.data is None:
            return 0
        return len(self.data)

    def get_column_name_and_type(self):
        # Return the name and type of 'data_in' to verify if they are the same
        if self.data is None:
            return [[], []]
        column_names = []
        column_types = []
        for element in self.data.domain:
            column_names.append(str(element))
            column_types.append(str(type(element)))
        return column_names, column_types

    # 0 ok 1 erreur
    def give_args_to_input(self):
        # pour toutes les colonnes de data_in -> si la colonne n 'est pas dans in loop continue
        col_names,col_types=self.get_column_name_and_type()
        col_names_start_loop,col_types_start_loop=(self.get_column_name_and_type_from_start())
        print("---->", col_names)
        print("---->", col_names_start_loop)
        print("---->", col_types)
        print("---->", col_types_start_loop)
        nb_maj=0
        table_representation = []
        for i in range(len(col_names)):
            for j in range(len(col_names_start_loop)):
                if col_names[i]!=col_names_start_loop[j]:
                    continue
                if col_types[i] != col_types_start_loop[j]:
                    self.error("col type change "+col_types_start_loop[j]+"->"+col_types[i]+" ("+col_names[i])+")"
                    return 1
                # print value
                print("######")
                print(col_names[i])
                print(col_types[i])

                print(self.data.domain)
                print(self.data[:,self.data.domain.index(col_names[i])])

                column_name = col_names[i]
                column_type = col_types[i]
                column_values = self.data[:,self.data.domain.index(col_names[i])]
                table_representation.append({
                    "name": column_name,
                    "type": column_type,
                    "values": column_values
                })
        if False:

            print("Test")
            # Mettre les données de la table representation dans self.data
            domain_attributes = [Orange.data.ContinuousVariable(col['name']) if "Continuous" in col['type'] else Orange.data.StringVariable(col['name']) for col in table_representation]
            new_domain = Orange.data.Domain(domain_attributes)
            new_data = np.array([col['values'] for col in table_representation], dtype=object).T
            self.data = Orange.data.Table(new_domain, new_data)
            # Mettre les données de la table representation dans self.data

            # start_widget = ctypes.cast(int(self.in_pointer), ctypes.py_object).value
            # if hasattr(start_widget, 'set_data'):
            #     start_widget.set_data(self.data)

###############################################Morlot Test give arg#################################################
    # def give_args_to_input(self):
    #     if self.data is None:
    #         print("No data available to send.")
    #         return
    #
    #     col_names, col_types = self.get_column_name_and_type()
    #
    #     table_representation = []
    #     for i in range(len(col_names)):
    #         column_name = col_names[i]
    #         column_type = col_types[i]
    #         column_values = self.data[:, self.data.domain.index(column_name)]
    #         table_representation.append({
    #             "name": column_name,
    #             "type": column_type,
    #             "values": column_values
    #         })
    #     print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    #     print(table_representation)
    #     pointer = ctypes.py_object(pickle.dumps(table_representation))
    #     self.in_pointer = ctypes.cast(ctypes.pointer(pointer), ctypes.c_void_p).value
    #     self.in_pointer.set_data(self.data)



    ###############################################Morlot Test give arg#################################################

    ############################ Envoyer les données avec ce qu'il y a dans les lignes dans start loop où on remplira un tableau


        # sinon on va remplacer----> ca j'ai pas encore fait , c'est ce que tu m'avais deamnder de faire la derniere fois
        # oui que se passe t il si tu a value ==1? dans data_out_value
    # vu
    # c'est le meme fonctionneement qu'avant , si la ligne ==1 alors on la transfer dans data_out et on lefface de dans data_in
    def process_data_based_on_iter(self):
        """Update 'data_in' and 'data_out' based on the value of 'iter'."""
        for i, row in enumerate(self.data):
            iter_value = row[self.data.domain["iter"]]
            data_in_value = str(row[self.data.domain["data_in"]])
            data_out_value = str(row[self.data.domain["data_out"]])

            if iter_value == 1:
                print(f"Transferring row {i} to 'data_out'.")
                if data_out_value in ("", "0.0", "?"):
                    self.data[i, self.data.domain["data_out"]] = data_in_value
                self.data[i, self.data.domain["data_in"]] = ""  # Clear 'data_in'
            # If iter_value == 0, do nothing (data stays for the next iteration)

    def check_loop_condition(self):
        """Check whether the loop should continue or stop."""
        all_iters = []
        for row in self.data:
            iter_value = row[self.data.domain["iter"]]
            iter_value = int(bool(iter_value)) if isinstance(iter_value, (float, int)) else int(iter_value.lower() == "true") if isinstance(iter_value, str) else 0
            all_iters.append(iter_value)

        if all(value == 1 for value in all_iters):
            print("All rows have iter == 1. Sending final data.")
            final_data = self.clean_final_data(self.data)
            self.Outputs.out_data.send(final_data)
        else:
            print("Some rows have iter == 0. Restarting the loop.")
            if self.in_pointer is not None:
                print("OOOONNNNNN arrete ce pointer pour voir si ça fonctionne avec l'autre")
                start_widget = ctypes.cast(int(self.in_pointer), ctypes.py_object).value
                if hasattr(start_widget, 'set_data'):
                    start_widget.set_data(self.data)

    def clean_final_data(self, data):
        """Clean the data, keeping only the updated 'data_in' column and original columns without 'iter'."""
        original_attributes = [attr for attr in data.domain.attributes if attr.name != "iter"]
        data_in_var = Orange.data.StringVariable("data_in")
        clean_domain = Orange.data.Domain(original_attributes, metas=[data_in_var])
        clean_data = Orange.data.Table.from_table(clean_domain, data)

        for i in range(len(data)):
            data_out_value = str(data[i, data.domain["data_out"]])
            clean_data[i, clean_data.domain["data_in"]] = data_out_value

        return clean_data

if __name__ == "__main__":
    from AnyQt.QtWidgets import QApplication
    app = QApplication(sys.argv)
    obj = EndLoopWidget()
    obj.show()
    app.exec_()
