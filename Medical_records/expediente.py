opciones = ["n", "b", "v", "d", "e", "h"]

textos = {
    "menu": "Nuevo Expediente (n) \nBuscar Expediente (b) \nVer todos los expedientes (v) \nBorrar Expediente (d) \nEditar Expediente (e) \nAyuda (h) \n¿Qué quieres hacer?: ",
    "opciones_invalidas": "Por favor ingresa una opción válida (n, b, v, d, e, h)\n",
    "nombre": "Nombre del paciente: ",
    "apellido": "Apellido: ",
    "edad": "Edad: ",
    "diagnostico": "Diagnóstico: ",
    "fecha_intro": "Introduce la fecha del expediente:",
    "dia": "Día (número): ",
    "mes": "Mes (número): ",
    "año": "Año (número): ",
    "exp_guardado": "Expediente guardado.\n",
    "buscar_menu": "Buscar por: 1) Nombre  2) Apellido  3) Edad  4) Diagnóstico  5) Fecha  6) Todos los datos",
    "criterio": "Elige el número del criterio de búsqueda: ",
    "nombre_buscar": "Nombre a buscar: ",
    "apellido_buscar": "Apellido a buscar: ",
    "edad_buscar": "Edad a buscar: ",
    "diagnostico_buscar": "Diagnóstico a buscar: ",
    "fecha_buscar": "Fecha a buscar (formato DD/MM/AAAA): ",
    "todos_buscar": ["Nombre: ", "Apellido: ", "Edad: ", "Diagnóstico: ", "Fecha (formato DD/MM/AAAA): "],
    "buscar_no_valido": "Opción de búsqueda no válida.\n",
    "exp_encontrados": "Expedientes encontrados:",
    "exp_no_encontrados": "No se encontraron expedientes.\n",
    "todos_expedientes": "Todos los expedientes:\n",
    "no_expedientes": "No hay expedientes guardados.\n",
    "nombre_borrar": "Nombre del paciente a borrar: ",
    "apellido_borrar": "Apellido del paciente a borrar: ",
    "exp_borrar": "Expedientes encontrados para borrar:",
    "seleccion_borrar": "Elige el número del expediente a borrar (o varios separados por coma): ",
    "exp_borrado": "Expediente(s) borrado(s).\n",
    "exp_no_borrar": "No se encontró ningún expediente con ese nombre y apellido.\n",
    "nombre_editar": "Nombre del paciente a editar: ",
    "apellido_editar": "Apellido del paciente a editar: ",
    "exp_editar": "Expedientes encontrados para editar:",
    "seleccion_editar": "Elige el número del expediente a editar: ",
    "nueva_edad": "Nueva edad (dejar vacío para no cambiar): ",
    "nuevo_diagnostico": "Nuevo diagnóstico (dejar vacío para no cambiar): ",
    "nueva_fecha": "Nueva fecha (formato DD/MM/AAAA, dejar vacío para no cambiar): ",
    "exp_editado": "Expediente editado.\n",
    "exp_no_editar": "No se encontró ningún expediente con ese nombre y apellido.\n",
    "exp_no_valido": "No se seleccionó un expediente válido.\n",
    "ayuda": """
--- Ayuda para el manejador de expedientes ---

Opciones disponibles:
n - Nuevo Expediente: Permite crear un expediente para un paciente. Debes ingresar nombre, apellido, edad, diagnóstico y fecha (día, mes y año en números).
b - Buscar Expediente: Puedes buscar expedientes por nombre, apellido, edad, diagnóstico, fecha o todos los datos juntos.
v - Ver todos los expedientes: Muestra todos los expedientes guardados.
d - Borrar Expediente: Busca por nombre y apellido, muestra coincidencias y puedes elegir cuál borrar.
e - Editar Expediente: Busca por nombre y apellido, muestra coincidencias y puedes elegir cuál editar. Puedes cambiar edad, diagnóstico y fecha.
h - Ayuda: Muestra esta explicación.

Para seleccionar una opción, escribe la letra correspondiente y presiona Enter.

Las fechas deben ingresarse en formato numérico, por ejemplo: Día: 05, Mes: 08, Año: 2025.

Recuerda que los datos se guardan en un archivo llamado "expedientes.txt" en el mismo directorio donde se ejecuta este programa. 
Asegúrate de no borrar o modificar este archivo manualmente para evitar problemas con los datos.
"""
}

def nuevo():
    print(textos["fecha_intro"])
    nombre = input(textos["nombre"])
    apellido = input(textos["apellido"])
    edad = input(textos["edad"])
    diagnostico = input(textos["diagnostico"])
    dia = input(textos["dia"])
    mes = input(textos["mes"])
    año = input(textos["año"])
    fecha = f"{dia.zfill(2)}/{mes.zfill(2)}/{año}"
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
                    print(f"{textos['nombre']}{nombre} | {textos['apellido']}{apellido} | {textos['edad']}{edad} | {textos['diagnostico']}{diagnostico} | Fecha: {fecha}")
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
