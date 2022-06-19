from Listas import lifestore_products
from Listas import lifestore_sales
from Listas import lifestore_searches

#se crea la funcion para mostrar los mejores o peores productos
def show_rank():

#se crean listas para almacenar la informacion    
    lista_ventas_totales = []
    lista_busqueda_totales = []

    lista_busqueda_totales_peor = []
    lista_busqueda_totales_0 = []

    lista_ventas_totales_peor = []
    lista_ventas_totales_0 = []

#se crea un for para darle valor a la lista "lista_ventas_totales" que almacena [ventas totales,ID del producto]
    for producto in lifestore_products:

        ventas_totales_producto = 0

        for ventas in lifestore_sales:

            if producto[0] == ventas[1]:

                ventas_totales_producto += 1

        lista_ventas_totales.append([ventas_totales_producto, producto[0]])

#se crea un for para darle valor a la lista "lista_busqueda_totales" que almacena [busquedas totales,ID del producto]
    for producto in lifestore_products:

        busquedas_totales_producto = 0

        for busquedas in lifestore_searches:

            if producto[0] == busquedas[1]:

                busquedas_totales_producto += 1

        lista_busqueda_totales.append([busquedas_totales_producto, producto[0]])

#Se da un input para el usuario decida que hacer
#try para evitar errores
    try:
      do_rank = int(input("Ver mejores productos(1)  ver peores productos(2) \n: "))
      print("\n")
    except:
      print("ERROR")
      print("\n")
      do_rank = 0

#si es 1 se van a imprimir los mejores productos
    if do_rank == 1:

        Boolean_rank = True
#Se ordenan la listas usando el metodo sort de mayor a menor        
        lista_ventas_totales.sort(reverse=Boolean_rank)
        lista_busqueda_totales.sort(reverse=Boolean_rank)

        print("Productos con mas ventas")
        print(lista_ventas_totales[0:5])
        print("\n")

        print("Productos mas buscados")
        print(lista_busqueda_totales[0:10])
        print("\n")

# si el input es 2 se muestran los peores productos
    elif do_rank == 2:

        Boolean_rank = False
#Se ordenan la listas usando el metodo sort de menor a mayor    
        lista_ventas_totales.sort(reverse=Boolean_rank)
        lista_busqueda_totales.sort(reverse=Boolean_rank)

        for venta in lista_ventas_totales:

#se crea un if para descartar los productos sin ventas
            if venta[0] == 0:

                lista_ventas_totales_0.append(venta)

            if venta[0] >= 1:

                lista_ventas_totales_peor.append(venta)

        for busquedas in lista_busqueda_totales:

#se crea un if para descartar los productos sin busquedas
            if busquedas[0] == 0:
                lista_busqueda_totales_0.append(busquedas)

            if busquedas[0] >= 1:
                lista_busqueda_totales_peor.append(busquedas)

#se imprimen las listas
        print("Productos sin ventas")
        print(lista_ventas_totales_0)
        print("\n")

        print("Productos sin busquedas")
        print(lista_busqueda_totales_0)
        print("\n")

        print("Productos menos vendidos")
        print(lista_ventas_totales_peor[0:5])
        print("\n")

        print("Productos menos buscados")
        print(lista_busqueda_totales_peor[0:10])
        print("\n")

#se crea una funcion para mostrar las reseñas
def show_review():

    lista_review = []
#try para evitar errores
    try:
      do_review = int(input("Ver mejores productos(1), Ver peores productos(2) \n:"))
      print("\n")
    except:
      print("ERROR")
      print("\n")
      do_review = 0
    

#se crea un if para decidir el orden de la lista 1 es True 2 es False
    if do_review == 1:
        print("Mostrando productos con mejores reseñas:")
        Boolean_review = True
    elif do_review == 2:
        print("Mostrando productos con peores reseñas:")
        Boolean_review = False

#se crea un for para darle valor a la lista "lista_review" donde es... 
# [total de reseñas, promedio de las resñas, ID del producto]

#decdi ordenar segun el total de reseñas ya que hay productos con una sola reseña y dan un promedio alto 

    for producto in lifestore_products:

        cantidad_review = 0
        review_total = 0

#Se crea un for para saber si los ID coinciden
        for review in lifestore_sales:

            if producto[0] == review[1]:

                cantidad_review += 1
                review_total += review[2]

        if review_total > 0:

            lista_review.append(
                [cantidad_review, round(review_total / cantidad_review, 2), producto[0]]
            )
#Se ordena la lista segun el input de usuario 1 o 2
    lista_review.sort(reverse=Boolean_review)
    
#se imprimen los primeros 10
    print(lista_review[0:10])
    print("\n")