# Ejercicios Python Pt3 (ejercicio faltante #8 y 9)

# 1. Numero mayor
import random
from math import log, floor
import re
print("Digite un numero")
n1 = int(input())
print("Digite un numero mayor que el primero")
n2 = int(input())

for i in range(n1, n2):
    print(i)

# 2. Par
print("Digite un numero")
a = int(input())
print("Digite un numero mayor que el primero")
b = int(input())

for a in range(b):
    if (a % 2 == 0):
        print("Los numeros pares son: ", a)

# 3. Impar
print("Digite un numero")
a = int(input())
print("Digite un numero mayor que el primero")
b = int(input())

for a in range(b):
    if (a % 2 == 1):
        print("Los numeros impares son: ", a)

# 4. Factorial
print("Digite un numero:")
n = int(input())


def factorial(n):
    factorial_t = 1
    while n > 1:
        factorial_t *= n
        n -= 1
    return factorial_t


print(factorial(n))

# 5. Mostrar en pantalla
continuar = "si"
salir = "no"

while continuar == 'si':
  lista = []
  print("-----------------------------")
  print("Digite la cantida de numeros:")
  n = int(input())
  print("Digite la cantidad:")
  num = int(input())

  if n >= 0:
    while n <= num:
      lista = lista + [n]
      n += 1
    print(lista)
    continuar = input("\nQuieres ingresar otro numero 'si' o 'no': ")
  else:
    print()

# 6. Descomponer


def descomponer(n):
    primos = []

    for i in range(2, n+1):
        while n % i == 0:
            primos.append(i)
            n = n / i
    return primos


print("Digite un numero: ")
num = int(input())
print(descomponer(num))

# 7. Contraseña
print("Bienvenido")
password = "senprot123"

intento = input("Introduce la contraseña:")

while intento != password:
    print("La contraseña no es correcta!")
    intento = input("Intentalo de nuevo:")

print("Contraseña Correcta")
print("SENPROT")

# 8.
# 9.
# 10. Contraseña true or false


def validar_password(password):
    if 8 <= len(password) <= 16:
        if re.search('[a-z]', password) and re.search('[A-Z]', password):
            if re.search('[0-9]', password):
                if re.search('[$@#]', password):
                    return True

    return False
# Forma corecta Password__1234@#$ = true
# Forma incorrecta password123 = false


clave = input('Escriba la contraseña: ')
print(validar_password(clave))

# 11.Random

intentos = 0

print('¡Hola! ¿Cuál es tu nombre?')
nombre = input()

numero = random.randint(1, 20)
print('Bueno, '+nombre+', piensa un número entre 1 y 20.')

while intentos < 6:
    print('¡Adivínalo! Tienes 6 intentos')
    adivina = input()
    adivina = int(adivina)

    intentos = intentos+1

    if adivina < numero:
        print('¡Demasiado pequeño!')

    if adivina > numero:
        print('¡Demasiado grande!')

    if adivina == numero:
        break

if adivina == numero:
    intentos = str(intentos)
    print('Fabuloso, '+nombre+', acertaste el número en ' +
          intentos+' intentos. ¡Estarás orgulloso-a!')

if adivina != numero:
    numero = str(numero)
    print('¡Qué fatalidad '+nombre+' ! Yo estaba pensando en el número '+numero)
# 12. Potencia de 2


def es_potencia_de_dos(numero):
    if numero < 1:
        return False
    i = log(numero, 2)
    return 0 == (i - floor(i))


print("Digite un numero: ")
num = int(input())
print(es_potencia_de_dos(num))

# 13. Divisores


def sum_divisores(n):
    sum = 0
    divisor = n

    while divisor > 1:
        divisor = divisor - 1
        if (n % divisor) == 0:
            sum += divisor

    # la suma de todos los divisores de n, sin incluir n
    return sum


print(sum_divisores(0))

print(sum_divisores(5))

print(sum_divisores(44))

print(sum_divisores(102))

# 14. Numeros perfectos


def perfecto(num):
    contador = 0
    for i in range(1, num):
        if num % i == 0:
            contador += i
    if contador == num:
        print(u"Es un número perfecto.")
    else:
        print(u"No es un número perfecto.")


perfecto(5)


# 15. Amigos
def numeros_amigos(x, y):
    suma_x = 0
    suma_y = 0

    for i in range(1, x):
        if x % i == 0:
            suma_x += i
            print("Divisores del nº 1:", suma_x)

    print("----------------------")

    for k in range(1, y):
        if y % k == 0:
            suma_y += k
            print("Divisores del nº 2:", suma_y)

    return suma_x == y and suma_y == x


n_1 = int(input('Introduzca el nº 1: '))
n_2 = int(input('Introduzca el nº 2: '))
print("---------------------------")

if numeros_amigos(n_1, n_2):
    print('¡Son amigos! :)')
else:
    print('No son amigos :(')

# 16. Primos
n = int(input("Digite un numero entero:"))
if n > 0:
    for i in range(2, n):
        aum = 2
        primo = True

        while primo and aum < i:
            if i % aum == 0:
                primo = False

            else:
                aum += 1

        if primo:
            print(i, "Es primo")

else:
    print("El numero ingresado no es corecto :(")

# 17. Intentos
num = 0

while True:
    print("Introduce un numero")
    num = int(input())
    if not num != 0:
        break


# 18. Intentos
num = 0
suma = 0

while True:
    print("Introduce un numero")
    num = int(input())
    suma = suma + num
    if not num != 0:
        break
print("la suma de los intentos es: ", suma)

# 19. Primeros 200 numeros pares


def numeros(n):
    pares = []
    contador = 0
    numero = 0

    while contador < n:
        if numero % 2 == 0:
            pares.append(numero)
            contador += 1

        numero += 1

    return pares


n = int(input('Escriba la cantidad de números pares: '))
if n > 0:
    pares = numeros(n)

    print('Los primeros', len(pares), "numeros pares son: ")
    print(pares)
else:
    print('El número debe ser positivo.')

# 20. Secuencias numericas


def series(num):
    for i in range(1, num + 1):
        f = pow(2, i-1)
        print(f, end=" ")


num = int(input("Digite cuantos numero quiere ver en pantalla:  "))
series(num)

# 21. Letras


def contarletras(string, letra):
    cont = 0
    string = string.upper()
    letra = letra.upper()

    for elemento in string:
        if elemento == letra:
            cont = cont + 1
    return cont


txt = input("Escriba una frase: ")
letra = input("Ingrese la letra que desee: ")

cont = contarletras(txt, letra)

print("La letra (", letra, ") aparece", cont, "veces")


# 22. Vocales


def l():
    global txt
    txt = (input("Escriba una frase:  ")).lower()


def c():
    v = ["a", "A", "á"]
    d = ["e", "E", "é"]
    g = ["i", "I", "í"]
    t = ["o", "O", "ó"]
    e = ["u", "U", "ú"]
    cont_a = 0
    cont_e = 0
    cont_i = 0
    cont_o = 0
    cont_u = 0

    for i in v:
        for j in txt:
            if (i == j):
                cont_a += 1
    for r in d:
        for y in txt:
            if (r == y):
                cont_e += 1
    for h in g:
        for ñ in txt:
            if (h == ñ):
                cont_i += 1
    for l in t:
        for k in txt:
            if (l == k):
                cont_o += 1
    for s in e:
        for n in txt:
            if (s == n):
                cont_u += 1

    cont = cont_a + cont_e + cont_i + cont_o + cont_u
    print("El numero total de vocales es: ", cont)
    print(f"""El numero por vocal es:
    a: {cont_a}
    e: {cont_e}
    i: {cont_i}    
    o: {cont_o}
    u: {cont_u}
    """)


l()
c()
