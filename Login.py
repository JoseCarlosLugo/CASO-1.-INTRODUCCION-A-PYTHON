
#Se cran las listas de usuarios 
admin = [["emtech","caso1"], ["emtech2","caso1"]]
user_no_admin =[["emtech3","caso1"], ["emtech4","caso1"] ]
lista_user = [["",""]]

#se crea la funcion de login
def login_correct():

  cont = 0
  print("iniciando sesión")
  user = input("ingrese el usuario: ")
  password = input("ingrese la contraseña: ")

  lista_user[0]=([user,password])

#Se crea un for para verificar si el input coincide con los usuarios admin o los no admin
  for object_admin in admin:
  
    if lista_user[0] == admin[cont]:
      print("\n")
      print("Esta iniciando como admin")
      print("\n")
      return True
      

    cont +=1
#Se crea un for para verificar si el input coincide con los usuarios no admin    
  cont = 0
  for object_user in user_no_admin:
    
    if lista_user[0] == user_no_admin[cont]:
      print("\n")
      print("Esta iniciando como usuario normal")
      print("\n")
      return True
      
    cont +=1

  return False


#Crea la funcion para cuando los input de usuarios no coinciden
def login_fail():
  
  print("Error el usuario o la contraseña no coinciden")
  print("intentar nueva mente(1)    Crear nuevo usuario(2)")
  

  do_user = int(input(": "))
  print("\n")

#Se llama la funcion de login para volverlo a intentar  
  if do_user == 1:
    login_correct()
    
#Se crea un nuevo usuario
  if do_user == 2:
    print("Se creara un nuevo usuario")
    new_user = input("ingrese el usuario: ")
    new_password = input("ingrese la contraseña: ")
    print("\n")
    user_no_admin.append([new_user, new_password])
   
#Se llama la funcion de login para volverlo a intentar  
    login_correct()
    
  return True