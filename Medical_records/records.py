opciones = ["n", "b", "v", "d", "e", "h"]

# Diccionario de textos en inglés
textos = {
    "menu": "New Record (n) \nSearch Record (b) \nView all records (v) \nDelete Record (d) \nEdit Record (e) \nHelp (h) \nWhat do you want to do?: ",
    "opciones_invalidas": "Please enter a valid option (n, b, v, d, e, h)\n",
    "nombre": "Patient's first name: ",
    "apellido": "Patient's last name: ",
    "edad": "Age: ",
    "diagnostico": "Diagnosis: ",
    "fecha_intro": "Enter the record date:",
    "dia": "Day (number): ",
    "mes": "Month (number): ",
    "año": "Year (number): ",
    "exp_guardado": "Record saved.\n",
    "buscar_menu": "Search by: 1) First name  2) Last name  3) Age  4) Diagnosis  5) Date  6) All data",
    "criterio": "Choose the search criterion number: ",
    "nombre_buscar": "First name to search: ",
    "apellido_buscar": "Last name to search: ",
    "edad_buscar": "Age to search: ",
    "diagnostico_buscar": "Diagnosis to search: ",
    "fecha_buscar": "Date to search (format MM/DD/YYYY): ",
    "todos_buscar": ["First name: ", "Last name: ", "Age: ", "Diagnosis: ", "Date (format MM/DD/YYYY): "],
    "buscar_no_valido": "Invalid search option.\n",
    "exp_encontrados": "Records found:",
    "exp_no_encontrados": "No records found.\n",
    "todos_expedientes": "All records:\n",
    "no_expedientes": "No records saved.\n",
    "nombre_borrar": "Patient's first name to delete: ",
    "apellido_borrar": "Patient's last name to delete: ",
    "exp_borrar": "Records found to delete:",
    "seleccion_borrar": "Choose the record number to delete (or several separated by comma): ",
    "exp_borrado": "Record(s) deleted.\n",
    "exp_no_borrar": "No record found with that first and last name.\n",
    "nombre_editar": "Patient's first name to edit: ",
    "apellido_editar": "Patient's last name to edit: ",
    "exp_editar": "Records found to edit:",
    "seleccion_editar": "Choose the record number to edit: ",
    "nueva_edad": "New age (leave blank to keep): ",
    "nuevo_diagnostico": "New diagnosis (leave blank to keep): ",
    "nueva_fecha": "New date (format MM/DD/YYYY, leave blank to keep): ",
    "exp_editado": "Record edited.\n",
    "exp_no_editar": "No record found with that first and last name.\n",
    "exp_no_valido": "No valid record selected.\n",
    "ayuda": """
--- Help for the record manager ---

Available options:
n - New Record: Allows you to create a record for a patient. Enter first name, last name, age, diagnosis, and date (day, month, and year as numbers).
b - Search Record: You can search records by first name, last name, age, diagnosis, date, or all data together.
v - View all records: Shows all saved records.
d - Delete Record: Search by first and last name, shows matches, and you can choose which to delete.
e - Edit Record: Search by first and last name, shows matches, and you can choose which to edit. You can change age, diagnosis, and date.
h - Help: Shows this explanation.

To select an option, type the corresponding letter and press Enter.

Dates must be entered in numeric format, for example: Day: 05, Month: 08, Year: 2025.

Remember that the data is saved in a file called \"expedientes.txt\" in the same directory where this program is run.
Do not delete or manually modify this file to avoid data
"""
}

def nuevo():
    nombre = input(textos["nombre"])
    apellido = input(textos["apellido"])
    edad = input(textos["edad"])
    diagnostico = input(textos["diagnostico"])
    print(textos["fecha_intro"])  # Show this only before asking for the date
    mes = input(textos["mes"])   # Month first
    dia = input(textos["dia"])   # Day second
    año = input(textos["año"])
    fecha = f"{mes.zfill(2)}/{dia.zfill(2)}/{año}"  # MM/DD/YYYY
    with open("expedientes.txt", "a", encoding="utf-8") as f:
        f.write(f"{nombre}|{apellido}|{edad}|{diagnostico}|{fecha}\n")
    print(textos["exp_guardado"])

def buscar():
    print(textos["buscar_menu"])
    criterio = input(textos["criterio"])
    encontrados = []
    with open("expedientes.txt", "r", encoding="utf-8") as f:
        for idx, linea in enumerate(f):
            partes = linea.strip().split("|")
            if len(partes) != 5:
                continue
            nombre, apellido, edad, diagnostico, fecha = partes
            if criterio == "1":
                valor = input(textos["nombre_buscar"])
                if nombre.lower() == valor.lower():
                    encontrados.append((idx, nombre, apellido, edad, diagnostico, fecha))
            elif criterio == "2":
                valor = input(textos["apellido_buscar"])
                if apellido.lower() == valor.lower():
                    encontrados.append((idx, nombre, apellido, edad, diagnostico, fecha))
            elif criterio == "3":
                valor = input(textos["edad_buscar"])
                if edad == valor:
                    encontrados.append((idx, nombre, apellido, edad, diagnostico, fecha))
            elif criterio == "4":
                valor = input(textos["diagnostico_buscar"])
                if diagnostico.lower() == valor.lower():
                    encontrados.append((idx, nombre, apellido, edad, diagnostico, fecha))
            elif criterio == "5":
                valor = input(textos["fecha_buscar"])
                if fecha == valor:
                    encontrados.append((idx, nombre, apellido, edad, diagnostico, fecha))
            elif criterio == "6":
                valores = [input(x) for x in textos["todos_buscar"]]
                # valores[4] is date in MM/DD/YYYY
                if (nombre.lower() == valores[0].lower() and
                    apellido.lower() == valores[1].lower() and
                    edad == valores[2] and
                    diagnostico.lower() == valores[3].lower() and
                    fecha == valores[4]):
                    encontrados.append((idx, nombre, apellido, edad, diagnostico, fecha))
                break
            else:
                print(textos["buscar_no_valido"])
                return
    if encontrados:
        print(textos["exp_encontrados"])
        for i, (idx, nombre, apellido, edad, diagnostico, fecha) in enumerate(encontrados, 1):
            print(f"{i}. {textos['nombre']}{nombre} | {textos['apellido']}{apellido} | {textos['edad']}{edad} | {textos['diagnostico']}{diagnostico} | Fecha: {fecha}")
    else:
        print(textos["exp_no_encontrados"])

def ver():
    print(textos["todos_expedientes"])
    try:
        with open("expedientes.txt", "r", encoding="utf-8") as f:
            vacio = True
            for linea in f:
                partes = linea.strip().split("|")
                if len(partes) == 5:
                    nombre, apellido, edad, diagnostico, fecha = partes
                    print(f"{textos['nombre']}{nombre} | {textos['apellido']}{apellido} | {textos['edad']}{edad} | {textos['diagnostico']}{diagnostico} | Date: {fecha}")
                    vacio = False
            if vacio:
                print(textos["no_expedientes"])
    except FileNotFoundError:
        print(textos["no_expedientes"])

def borrar():
    nombre_borrar = input(textos["nombre_borrar"])
    apellido_borrar = input(textos["apellido_borrar"])
    expedientes = []
    candidatos = []
    with open("expedientes.txt", "r", encoding="utf-8") as f:
        for idx, linea in enumerate(f):
            partes = linea.strip().split("|")
            if len(partes) == 5:
                nombre, apellido, edad, diagnostico, fecha = partes
                if nombre.lower() == nombre_borrar.lower() and apellido.lower() == apellido_borrar.lower():
                    candidatos.append((idx, nombre, apellido, edad, diagnostico, fecha))
                else:
                    expedientes.append(linea)
            else:
                expedientes.append(linea)
    if candidatos:
        print(textos["exp_borrar"])
        for i, (idx, nombre, apellido, edad, diagnostico, fecha) in enumerate(candidatos, 1):
            print(f"{i}. {textos['nombre']}{nombre} | {textos['apellido']}{apellido} | {textos['edad']}{edad} | {textos['diagnostico']}{diagnostico} | Fecha: {fecha}")
        seleccion = input(textos["seleccion_borrar"])
        indices_borrar = [int(x)-1 for x in seleccion.split(",") if x.strip().isdigit()]
        expedientes_final = []
        for idx, linea in enumerate(open("expedientes.txt", "r", encoding="utf-8")):
            partes = linea.strip().split("|")
            if len(partes) == 5 and idx in [candidatos[i][0] for i in indices_borrar]:
                continue
            expedientes_final.append(linea)
        with open("expedientes.txt", "w", encoding="utf-8") as f:
            for expediente in expedientes_final:
                f.write(expediente)
        print(textos["exp_borrado"])
    else:
        print(textos["exp_no_borrar"])

def editar():
    try:
        with open("expedientes.txt", "r", encoding="utf-8") as f:
            lineas = f.readlines()
    except FileNotFoundError:
        print(textos["no_expedientes"])
        return

    if not lineas or all(line.strip() == "" for line in lineas):
        print(textos["no_expedientes"])
        return

    nombre_editar = input(textos["nombre_editar"])
    apellido_editar = input(textos["apellido_editar"])
    expedientes = []
    candidatos = []
    for idx, linea in enumerate(lineas):
        partes = linea.strip().split("|")
        if len(partes) == 5:
            nombre, apellido, edad, diagnostico, fecha = partes
            if nombre.lower() == nombre_editar.lower() and apellido.lower() == apellido_editar.lower():
                candidatos.append((idx, nombre, apellido, edad, diagnostico, fecha))
            expedientes.append(linea)
        else:
            expedientes.append(linea)
    if candidatos:
        print(textos["exp_editar"])
        for i, (idx, nombre, apellido, edad, diagnostico, fecha) in enumerate(candidatos, 1):
            print(f"{i}. {textos['nombre']}{nombre} | {textos['apellido']}{apellido} | {textos['edad']}{edad} | {textos['diagnostico']}{diagnostico} | Fecha: {fecha}")
        seleccion = input(textos["seleccion_editar"])
        if seleccion.isdigit() and 1 <= int(seleccion) <= len(candidatos):
            idx_editar = candidatos[int(seleccion)-1][0]
            nueva_edad = input(textos["nueva_edad"])
            nuevo_diagnostico = input(textos["nuevo_diagnostico"])
            nueva_fecha = input(textos["nueva_fecha"])
            expedientes_modificados = []
            for idx, linea in enumerate(expedientes):
                partes = linea.strip().split("|")
                if idx == idx_editar and len(partes) == 5:
                    nombre, apellido, edad, diagnostico, fecha = partes
                    if nueva_edad == "":
                        nueva_edad = edad
                    if nuevo_diagnostico == "":
                        nuevo_diagnostico = diagnostico
                    if nueva_fecha == "":
                        nueva_fecha = fecha
                    expedientes_modificados.append(f"{nombre}|{apellido}|{nueva_edad}|{nuevo_diagnostico}|{nueva_fecha}\n")
                else:
                    expedientes_modificados.append(linea)
            with open("expedientes.txt", "w", encoding="utf-8") as f:
                for expediente in expedientes_modificados:
                    f.write(expediente)
            print(textos["exp_editado"])
        else:
            print(textos["exp_no_valido"])
    else:
        print(textos["exp_no_editar"])

def ayuda():
    print(textos["ayuda"])

while True:
    opción = input(textos["menu"])
    if opción not in opciones:
        print(textos["opciones_invalidas"])
    else:
        if opción == "n":
            nuevo()
        elif opción == "b":
            buscar()
        elif opción == "v":
            ver()
        elif opción == "d":
            borrar()
        elif opción == "e":
            editar()
        elif opción == "h":
            ayuda()
    print("\n")
