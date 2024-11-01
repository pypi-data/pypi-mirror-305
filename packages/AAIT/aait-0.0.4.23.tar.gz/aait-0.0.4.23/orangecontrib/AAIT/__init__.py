import os
import tempfile

if "site-packages/Orange/widgets" in os.path.dirname(os.path.abspath(__file__)).replace("\\","/"):
     from Orange.widgets.orangecontrib.AAIT.utils.tools import first_time_check
else:
     from orangecontrib.AAIT.utils.tools import first_time_check


def remove_temp_file():
    temp_folder = tempfile.gettempdir()
    temp_file_path = os.path.join(temp_folder, 'orange_lance.txt')
    if os.path.exists(temp_file_path):
        try:
            os.remove(temp_file_path)
        except Exception as e:
            print(f"Erreur lors de la suppression du fichier temporaire : {e}")

remove_temp_file()