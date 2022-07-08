# EJERCICIO 1
1 - Realiza un programa que solicite dos números y una operación (suma, resta, división y multiplicación) e imprima el resultado.

Además deberá mostrar un menú con las siguientes opciones:

Mostrar números

Sumar

Restar

Dividir (considerar la división entre 0)

multipicar

cerrar calculadora


# EJERCICIO 2
2 - Realizar un programa que administre una agenda. Se debe almacenar para cada contacto el nombre, el teléfono y el email.

Además deberá mostrar un menú con las siguientes opciones:

Añadir contacto

Lista de contactos

Buscar contacto

Editar contacto

Cerrar agenda


nombre=0
tel=0
email=0
directorio=[]


while True:
  opcion=int(input('''
  Selecciona una opcion
  1 - Añadir contacto
  2 - Lista de contactos
  3 - Buscar contacto
  4 - Editar contacto
  5 - Cerrar agenda'''))

  if(opcion == 1):
      nombre =input('Ingresa el nombre: ')
      tel = input('Ingresa el teléfono: ')
      email= input('Ingresa el email')
      directorio.append ([nombre, tel, email])
      print('Se ha agregado con éxito a la lista de contacto')

  elif(opcion == 2):
      for contacto in agenda:
    print(f'La lista de contactos es {contacto}')
    
  elif(opcion == 3):
       buscar=input('Ingrese el nombre a buscar')
      for nombre in agenda:
    print(f'El contacto es: nombre: {nombre}\n teléfono:{teléfono}\n email:{email}')
    else:
        print('El contacto no existe')
        

  elif(opcion == 4):
      tel=input('ingrese el nuevo número')
      agenda[nombre]=numero


    print('El número ha sido cambiado')

  elif(opcion == 5):
    break

  else:
    print(f'Opción no valida ')
    
    
    
    
    #ejercicio con poo
    
    
    #se crea la clase
class Agenda
#se crea iniit que hará referencia a los contactos
def __init__(self,contactos, nombre, tel, email):
    self.contactos= []
    self.nombre= []
    self.tel=[]
    self.email[]
    
def opciones (self):
    opciones=[
			['Agenda Personal'],
			['1 - Añadir Contacto'],
			['2 - Lista de contactos'],
			['3 - Buscar contacto'],
			['4 - Editar contacto'],
			['5 - Cerrar agenda']
		]
		opciones=input('ingrese el número de la opción deseada')
		if opciones ==1:
		    def añadir (self):
		        nombre=input("Introduzca el nombre: ")
		        tel=int(input("Introduzca el teléfono: "))
		        email=input("Introduzca el email: ")
		self.contactos.append({'nombre':nombre,'tel':telf,'email':email})
		    def lista==2:
		        for contactos in agenda:
		            print('La lista de contactos es:')
		            print(f'El nombre:{nombre}')
		            print(f'El teléfono es :{tel}')
		            print(f'El email es : {email}')
		            
		            

		        
 
