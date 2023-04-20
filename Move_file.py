import os
import shutil

from_dir = 'C:/Users/Usuario/Downloads/'
to_dir = 'C:/Users/Usuario/Desktop/'

list_of_files = os.listdir(from_dir)

for file in list_of_files:
    name, extension = os.path.splitext(file)
    if extension == " ":
        continue
    elif extension in [".txt", ".doc", ".docx", ".pdf"]:
        path1 = from_dir + file
        path2 = to_dir + "Arquivos_Documentos/"
        path3 = to_dir + "Arquivos_Documentos/" + file

        if os.path.exists(path2):
            print("movendo " + file)
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("movendo " + file)
            shutil.move(path1, path3)
