import os

def ClearClutter(path, extension):
    i=1
    files = os.listdir(path)
    

    for file in files:
        if file.endswith("." + extension):
            print(file)
            os.rename(f"{path}/{file}",f"{path}/{i}.{extension}")
            i=i+1

ClearClutter(r"C:\Users\LENOVO\Pictures\Screenshots\bug", "PNG")
