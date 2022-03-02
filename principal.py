from funciones import *

todojson = leer_json("fichero.json")

menujson = '''
1. Listar los nombres de todas las confiterías junto con su horario
2. Por cada confitería contar el número de categorias que tiene
3. Introduce una dirección y muestra la confitería que se encuentre en esa dirección
4. Introduce una categoría y muestra todas las confiterías que tienen esa categoría
5. Introduce el nombre de una confitería y mostrar: descripción, dirección y teléfono
'''
print(menujson)
opc = int(input("Introduce una opción: "))

while opc != 6:
    if opc == 1:
        lista = confiterias_horarios(todojson)
        print("\n")
        for a in lista:
            print("CONFITERÍA: ", a[0], " HORARIO: ", a[1])
        print("--------------------------------------------------------------")

    elif opc == 2:
        print("CONFITERÍA | NUM. CATEGORÍAS")
        listanumcat = contar_categoria(todojson)
        print("\n")
        for a in listanumcat:
            for e in a:
                print(e," ",end="")
            print()
        print("--------------------------------------------------------------")

    elif opc == 3:
        listatododire = []
        for i in todojson.get("directorios").get("directorio"):
            listatododire.append([i.get("direccion")[0]])
        for a in listatododire:
            for e in a:
                print(e,"",end="")
            print()
        print()
        direccion = input("Introduce una dirección: ")
        horariosyconfit = direccion_introducida(todojson,direccion)
        print("\n")
        for dir in horariosyconfit:
            print("La confitería que se encuentra en esa dirección es ", dir)
        print("--------------------------------------------------------------")

    elif opc == 4:
        todocat = []
        for a in todojson.get("directorios").get("directorio"):
            for e in a.get("categorias").get("categoria"):
                todocat.append(e.get("content"))
        todocat = list(set(todocat))
        print("Estas son todas las categorías que hay:")
        for e in todocat:
            print(e," | ",end=" ")
        print()
        print()
        categ = input("Introduce una categoría a buscar: ")
        listaconfis = categoria_filtro(todojson,categ)
        print("\n")
        print("Confiterías con la categoría ",categ,":")
        for cat in listaconfis:
            print(cat)
        print("--------------------------------------------------------------")

    elif opc == 5:
        listatodoconfit = []
        print("-- ESTAS SON TODAS LAS CONFITERÍAS --")
        for e in todojson.get("directorios").get("directorio"):
            listatodoconfit.append(e.get("nombre").get("content"))
        for a in listatodoconfit:
            print(a," | ",end="")
        print()
        print()
        nombreconfit = input("Introduce el nombre de una de las confiterías: ")
        todoatributos = mostrar_ddt(todojson,nombreconfit)
        for a in todoatributos:
            print("\n")
            print("-- DESCRIPCIÓN --", a[0])
            print("\n")
            print("-- DIRECCIÓN --", a[1])
            print("\n")
            print("-- TELÉFONO --", a[2])
        print()
        print("--------------------------------------------------------------")

    else:
        print("Valor no válido")

    print("\n")
    print(menujson)
    opc = int(input("Introduce una opción: "))

print("¡FIN DE PROGRAMA!")