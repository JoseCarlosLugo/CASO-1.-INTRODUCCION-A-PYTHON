from Login import login_correct
from Login import login_fail
from ProductosF import show_rank
from ProductosF import show_review
from VentasF import Show_ingresos




#Se Crea una variable a la cual se le da el valor (true/false) sengun la funcion de login
login_true = login_correct()

#Si el login es incorecto se crea un blucle y se llama la funcion para crear un nuevo usuario
if login_true == False:
  while login_true == False:
    login_true = login_fail()
    
#si el login es correcto se despliega el menu
if login_true == True:

#Se crea un bucle para repetir el menu segun el usuario lo quiera
  while True:
    
    print("\n")
    print("Que quiere hacer? \n")
  
    print("Ver las compras de los productos(1)",
                      "\nVer reseñas de los productos(2)",
                      "\nVer los ingresos(3)")

#se crea un try para evitar errores
    try:
      do_main = int(input("Salir (4) \n:"))
      print("\n")
    except:
      print("ERROR")
      print("\n")
      do_main = 0
#Se llama la funcion para mostrar los mejores o peores productos    
    if do_main == 1:
      show_rank()
#Se llama la funcion mostrar los productos con mas  reseñados       
    elif do_main == 2:
      show_review()
# se llama la funcion para ver los ingresos      
    elif do_main == 3:
      Show_ingresos()
#Se cierra el programa      
    elif  do_main == 4:
      print("Cerrando sesión")
      print(".")
      print("..")
      print("...")
      print("Sesión cerrada correctamente")
      break

    do_main = 0
