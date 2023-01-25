import csv
import cProfile

nif_dict = {"0":"T", "1":"R","2":"W","3":"A","5":"M","6":"Y","7":"F","8":"P","9":"D","10":"X","11":"B","12":"N",
            "13":"J","14":"Z", "15":"S","16":"Q","17":"V","18":"H","19":"L","20":"C","21":"K","22":"E",}

def check_nif(nif_persona):
    numeros = int(nif_persona[0:8])
    resto = int(numeros % 23)
    nif_correcto = numeros + nif_dict[str(resto)]
    return str(nif_correcto)

def check_username(nombre):
    nombre_corregido = nombre.title()
    return nombre_corregido

def check_DGT(ficheros):
    personas_csv = []
    with open(ficheros, encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=",", dialect=csv.excel)
        for persona in reader:
            personas_csv.append(persona)
    personas_csv.pop(0)
    for persona in personas_csv:
        persona[0] = check_username(persona[0])
        persona[1] = check_nif(persona[1])
    with open(ficheros, encoding="utf-8") as corregido:
        corregir = open(ficheros, "w", newline="")
        corregido = csv.writer(corregir, quotechar="", quoting=csv.QUOTE_ALL)
        for linea in personas_csv:
            corregido.writerow(linea)
    return check_DGT("500.csv")
cProfile.run("check_DGT(`1000.csv´)")













