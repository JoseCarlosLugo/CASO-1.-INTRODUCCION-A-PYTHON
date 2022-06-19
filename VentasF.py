
from Listas import lifestore_products
from Listas import lifestore_sales


'''Hay dos errores de logica que no puede solucionar'''
'''en el for de la linea 23'''
'''Y en el while de la linea 52'''


#Se crea una funcion para ver los ingresos
def Show_ingresos():

    lista_venta_mes= []
    lista_venta_por_mes = []
    
    lista_ingreso_mes = []
    lista_ingreso_por_mes = []
    
    
 #Se crea un for para darle valor la listas:
 #lista_venta_mes donde es [mes,año,ventas]
 #Lista_ingres_mes donde es [mes,venta,valor del producto]
    for ventas in lifestore_sales:
    
        fechas = ventas[3]
        year = int(fechas[6:])
        mes = int(fechas[3:5])

#if para descartar las ventas de que no son del año 2020 ya solo hay una venta del 2018 y otra del 2002
#y los creo elevantes, en caso de querer cambiarlos se remplaza por >= 2020
#               >= 2018           
        if year == 2020:
        
            lista_venta_mes.append([mes,year,ventas[1]])
    
            for producto in lifestore_products:
    
                if ventas[1] == producto[0]:
    
                    lista_ingreso_mes.append([mes,ventas[1],producto[2]])

    '''Hay un error en este for que hace que el mes 12 no exista, ya
       que al no haber ninguna venta en el 12 este mes no se añade a lista'''


    
#Se crea un while para darle valor a la lista  
# lista_venta_por_mes [Ventas del mes, mes]

    meses = 1
    while meses < 12:

        for mes in lista_venta_mes: 
    
    
            if meses == mes[0]:
    
                ventas_mes = 0
            
                for ventas in lista_venta_mes:
            
                    if meses == ventas[0]:
                
                        ventas_mes += 1
                
        lista_venta_por_mes.append([ventas_mes, meses, ]) 

        meses += 1
    '''El error es que le agrega una venta al mes 10 y 11 (y posiblemente al 12 si existiera)'''  
    '''Esto pasa ya que la variable ventas_mes simpre es 1 el terminar el ciclo del for de la linea 61'''
    '''La solucion que intente darle es crear otro if donde compare las ventas con 0 para darle el valor
       a la variable ventas_mes si no hay ventas
       if ventas == 0:
         ventas_mes = 0'''  

    '''Pero no exiten las no ventas lo cual no puede hacer la comparacion'''   
    
#Se crea un while para darle valor a la lista:
#lista_ingreso_por_mes[ingresos por mes, mes]    
    meses = 1
    while meses < 12:
        
        ingreso_por_mes = 0
    
        for mes in lista_ingreso_mes:   
    
            if meses == mes[0]:
    
                ingreso_por_mes += mes[2]
    
        lista_ingreso_por_mes.append([ingreso_por_mes,meses]) 
        
        meses += 1

#se crea input para el usuario   
#try para evitar errores
    try:
      do_ingresos = int(input("Mostrar ventas por mes(1)   Mostrar meses con mas ventas(2) \n: "))
      print("\n")
    except:
      print("ERROR")
      print("\n")
      do_ingresos = 0
    
    if do_ingresos == 1:
#se imprimen los ingresos por mes y las ventas por mes
        print("Total de ingresos por mes:")
        for mostrar in lista_ingreso_por_mes:
            print(mostrar)
        print("\n")
        print("Total de ventas por mes:")

        for mostrar in lista_venta_por_mes:

            print(mostrar)
        print("\n")

#se imprimen los 3 mejores meses        
    elif do_ingresos == 2:

#se ordenan la lista de mayor a menor
        lista_venta_por_mes.sort(reverse = True)
        
        print("Meses con mas ventas:")

        print(lista_venta_por_mes[0])
        print(lista_venta_por_mes[1])
        print(lista_venta_por_mes[2])
        print("\n")
