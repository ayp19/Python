"""
Proyecto Básico de Python (El Ahorcado).
Basado en el proyecto de: Kylie Ying (@kylieyying). 
"""
```
import random #se importa la libreria random
import string # se importa la libreria string que nos va a permitir usar cadenas de caracteres 
from palabras import palabras #se importa el archivo palabras se importara la lista de palabras importa un modulo de un archivo que nosostros creamos
from ahorcado_diagramas import vidas_diccionario_visual # del archivo ahorcado_diagramas se trae el diccionario visual

# se define la funcion 
def obtener_palabra_válida(palabras):# se define la función
    palabra = random.choice(palabras) # al azar se va a selecionar una palabra de la lista  ( de la lista palabras)y la va a asignar a la palabra palabras 

#ciclo que nos permita filtrar las palabras que contengan - o espacio en este caso va a seleccionar la palabra que no tenga ninguna de estas
    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras) # va a seleccionar una palabra de la lista al azar   y la va a asignar a la variable palabra
#se va a regresar la palabra en mayusculas (usando el método upper)
    return palabra.upper()

#se define la funcion
def ahorcado():
#se muestra el mensaje en la pantalla del jugador ¡bienvenido al juego del ahorcado!
    print("=======================================")
    print(" ¡Bienvenido(a) al juego del Ahorcado! ")
    print("=======================================")

    palabra = obtener_palabra_válida(palabras)#se define la variable  palabra  va aser una lista de palabras validas para le juego
    #se van a definir 3 variables 
    letras_por_adivinar = set(palabra)  #se crea un conjunto ( con set)que nos permite guardar un elemento sin repetirlos
    abecedario = set(string.ascii_uppercase)  # se usa set para que sea tambien un conjunto de letras, 
    #ese modulo tiene una constante que contiene todas las letras( nos va a dar todas las letras del abecedario en mayusculas por el uppercase)
    letras_adivinadas = set()  #se necesita crear un conjunto para las pañabras que ya han sido adivinadas pero que este vacío, se llama a set para crear un conjunto

    vidas = 7 #se define la variable con el número de vidas que son 7

# se crea un ciclo while porque no sabemos cuantas repeticiones se van a realizar, mientras existan letras pendiente y le queden vidas se va a seguir repitiendo
    while len(letras_por_adivinar) > 0 and vidas > 0:
#le va a mostrar al usuario cuantas vidas le quedan y cuantas letras has usado
        print(f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)}")# se usa join para unir los elementos de un conjunto  

      #se debe mostrar el estado actual de la palabra
        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra]# se va a crear una lista  de las letras que hemos adivinadas y sino esta que se incluya un -
        print(vidas_diccionario_visual[vidas]) #se va a mostrar el estado de la horca visualmente, vidas se usa como clave para mostrar el diagrama correspondiente
        print(f"Palabra: {' '.join(palabra_lista)}") #se va a mostrar la palabra en su estado actual 

     # se crea una variable letra_usuario para que el usuario 
     # escoja una letra y vamos a convertir la letra a mayúscula
        letra_usuario = input('Escoge una letra: ').upper()
#si la letra esta en el conjunto de letras del abecedario y 
#no esta en el conjunto de letras que se ingresaron entonces se debe agregar esa letras al conjunto de letras ingresada
        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)
#  se crea un ciclo para saber si la letra está en la palabra se va a quitar 
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('')# se agrega una cadena vacía
#en caso de que no este la letra se le va a quitar un vida al usuario
            else:
                vidas = vidas - 1
                print(f"\nTu letra, {letra_usuario} no está en la palabra.") # va a mostrar al usuario un mensaje que diga que la 
                #letra que escogío el usuario no esta en la palabra 
 #si la letra escogida por el usuario ya fue ingresada  se va a mostrar el mensaje        
        elif letra_usuario in letras_adivinadas:
            print("\nYa escogiste esa letra. Por favor escoge una letra nueva.")
        else:#si ninguna de estas opciones es verdadera significa que ninguna de estas  no es válida
            print("\nEsta letra no es válida.")

   #se crea una condición 
    if vidas == 0:
        print(vidas_diccionario_visual[vidas])# va a mostrar el ahorcado visualmente 
        print(f"¡Ahorcado! Perdiste. Lo lamento mucho. La palabra era: {palabra}")# se va amostrar el mensaje
    else:# en caso de que este no sea el caso se mostrara el mensaje 
        print(f'¡Excelente! ¡Adivinaste la palabra {palabra}!')


    ahorcado()# se llama a la función ahorcado para ejecutar el programa
    
```

