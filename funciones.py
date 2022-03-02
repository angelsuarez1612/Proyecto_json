import json
import sys

def leer_json(fichero):
    try:
        with open(fichero) as f:
            doc=json.load(f)
        return doc
    except:
        print("Error al leer el fichero json")
        sys.exit(0)

#1
def confiterias_horarios(doc):
    confshor = []
    for i in doc.get("directorios").get("directorio"):
        confshor.append([i.get("nombre").get("content"),i.get("horario")])
    return confshor

#2
def contar_categoria(doc):
    numcat = []
    for i in doc.get("directorios").get("directorio"):
        numcat.append([i.get("nombre").get("content"),len(i.get("categorias").get("categoria"))])
    return numcat

#3
def direccion_introducida(doc,direccion):
    direc = []
    valid = False
    for a in doc.get("directorios").get("directorio"):
        for i in a.get("direccion"):
            if direccion == i:
                direc.append(a.get("nombre").get("content"))
                valid = True
    if valid == False:
        print("No encontramos resultados con esa dirección")
    return direc

#4
def categoria_filtro(doc,categ):
    categoriasdeconfit = []
    valid = False
    for a in doc.get("directorios").get("directorio"):
        for e in a.get("categorias").get("categoria"):
            if e.get("content") == categ:
                categoriasdeconfit.append(a.get("nombre").get("content"))
                valid = True
    if valid == False:
        print("No encontramos resultados acerca de ese sector")
    return categoriasdeconfit

#5
def mostrar_ddt(doc,nombreconfit):
    atributos = []
    valid = False
    for a in doc.get("directorios").get("directorio"):
        if nombreconfit == a.get("nombre").get("content"):
            atributos.append([a.get("descripcion").get("content"),a.get("direccion")[0],a.get("telefono").get("content")])
            valid = True
    if valid == False:
        print("No encontramos resultados de confiterías con ese nombre")
    return atributos