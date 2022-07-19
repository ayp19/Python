# 5 Práctica 5. Operadores relacionales. (6 puntos) 
### 5.1 Ejercicio 1 (2 puntos)
Programa que imprima si el número es positivo o negativo, el número debe ser ingresado por consola.
```
#Declaro la variable
num=0
#se imprime ingrese el número para almacenarlo en la variable
num=float (input('Ingrese un número '))
#se usa la condición if
if num ==0:
    print(' ¡el número es neutro!')        
elif num<0:
        print(' ¡el número es negativo!')                
else:
        print('¡el número ingresado es positivo!')
        
```        

### 5.2 Ejercicio 2 (2 puntos)
Programa que imprima si el número ingresado esta en el rango de 1 a 7, el número se solicita por consola.

```
#declaramos la variable
num=0
#escribe/ muestra en pantalla 'ingrese un número'
num=int(input('ingrese un número '))
#condición 
if num <=1 or num <= 7:
    print('el número ingresado esta dentro del rango')# se imprime/ muestra en la pantalla        
else:
        print( 'el número ingresado no está en el rango')
 ```       

### 5.3 Ejercicio 3 (2 puntos)
Programa que solicite un monto y que solicite el interés mensual, si el interés es mayor al 30% nos imprimirá que es incorrecto, si es menor realizará el cálculo e imprimira el monto con su interés adicionado.

```
#Declaro las variables
monto=0
interes=0
intAdicionado=0
# solicito que ingrese el monto para almacenarlo en la variable monto
monto=float(input('Ingrese el monto'))
#Solicito que ingrese el interes para almacenarlo en la variable interes
interes=float(input('Ingrese el interés'))
#condición
if interes >= 30:
    print('¡El interés es correcto!')
else:
    intAdicionado=(monto * interes*12)/100
    print(f'el monto con el interés es {intAdicionado}')
    
