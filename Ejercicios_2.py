# Ejercicios Python Pt2 (ejercicio faltante #8)

# 1. Mayor menor
import math
x = int(input("¿Cuál es el primer número?"))
y = int(input("¿Cuál es el segundo número?"))
if x > y:
    print('El primer número es mayor.')
elif x < y:
    print('El primer número es menor.')
else:
    print('Es el mismo número.')

# 2. Pares e impares
def main():
    print("Pares e impares")
    numero_1 = int(input("Escriba un número entero: "))
    numero_2 = int(
        input(f"Escriba un número entero mayor o igual que {numero_1}: "))

    if numero_2 < numero_1:
        print(f"¡Le he pedido un número entero mayor o igual que {numero_1}!")
    else:
        for i in range(numero_1, numero_2 + 1):
            if i % 2 == 0:
                print(f"El número {i} es par.")
            else:
                print(f"El número {i} es impar.")


if __name__ == "__main__":
    main()

# 3. Promedio
print("Programa para calcular promedios de valores")
suma = 0
contador = 0
promedio = 0
lista = []
lista2 = []
valor_r = int(input("Introduzca el rango de valores a calcular: "))
for i in range(valor_r):
    valor_n = int(input("Ingrese el valor numerico: "))
lista.extend([valor_n])
suma = suma+valor_n
promedio = suma/valor_r
for i in range(len(lista[:])):
    if promedio <= lista[i]:
        contador = contador+1
lista2.extend([lista[i]])
print("El promedio de los " + str(valor_r) + " valores es: " + str(promedio))
print("La cantidad de valores mayores al promedio son: " + str(contador))

# 4. Orden mayor a menor
print("Ingrese un numero")
N1 = int(input())
print("Ingrese un segundo numero")
N2 = int(input())

if N1 < N2:
    print("el orden de los numeros es: ", N1, "y", N2)
else:
    print("el orden de los numeros es: ", N2, "y", N1)

# 5. Organizar 3 numeros
print("Ingrese un numero")
N1 = int(input())
print("Ingrese un segundo numero")
N2 = int(input())
print("ingrese un tercer numero")
N3 = int(input())


if (N1 > N2 and N2 > N3):
    print("el orden de los numeros es: ", N1, "y", N2, "y", N3)
else:
    if (N1 > N3 and N3 > N2):
        print("el orden de los numeros es: ", N1, "y", N3, "y", N2)
    else:
        if (N2 > N1 and N1 > N3):
            print("el orden de los numeros es: ", N2, "y", N1, "y", N3)
        else:
            if (N2 > N3 and N3 > N1):
                print("el orden de los numeros es: ", N2, "y", N3, "y", N1)
            else:
                if(N3 > N1 and N1 > N2):
                    print("el orden de los numeros es: ", N3, "y", N1, "y", N2)
                else:
                    if (N3 > N2 and N2 > N1):
                        print("el orden de los numeros es: ",
                              N3, "y", N2, "y", N1)

# 6.Bruto
print("ingrese las horas trabajadas")
d_horas = int(input())
print("Ingrese su nombre")
nom = input()
tarifa = 200

if(d_horas < 35):
    sbruto = d_horas * tarifa
else:
    sbruto = 35 * tarifa(d_horas - 35) * 1.5 * tarifa

if (sbruto > 2000):
    impuestos = 0
else:
    if (sbruto > 2000 and sbruto < 35000):
        impuestos = (sbruto - 2000)*0.20
    else:
        impuestos = (790000 * 0.20)+(sbruto - 35000)*0.30


neto = sbruto - impuestos

print("tu nombre es: ", nom)
print("tu trabajo es: ", sbruto)
print("los impuestos es: ", impuestos)
print("tu salario neto es: ", neto)

# 7. Edad
edad = int(input("Escribe tu edad: "))
if edad >= 18:
    print("Eres mayor de edad puedes ingresar a la discoteca")
    print("ingresa tu identificacion")
    Cedula = int(input("Escribe tu Cedula: "))
    print("", Cedula)
else:
    print("Tu eres menor de edad no puedes ingresar")

# 8. Tatiana


# 9. Entero Real
dato = input("Ingrese dato: ")

num = None
for conv in (int, float, complex):
    try:
        num = conv(dato)
        break
    except ValueError:
        pass

if num is None:
    print("Error de entrada")
else:
    print(f"dato={num} (tipo: {type(num).__name__})")

# 10. Año bisiesto
print("Año Bisiesto")
año = int(input("Ingrese el año: "))
if (año % 400 == 0) or (año % 4 == 0) and (año % 100 != 0):
    print("El año", año, "es BISIESTO")
else:
    print("El año", año, "NO es BISIESTO")

# 11.Triangulo
# Declarando Variables de tipo entero
LadoA = int(input("Ingrese el primer lado: \n"))
LadoB = int(input("Ingrese el segundo lado: \n"))
LadoC = int(input("Ingrese el tercer lado: \n"))

# Solo para el método clásico
Altura = int(input("Ingrese el primer lado \n"))
Base = int(input("Ingrese el primer lado \n"))

# Solo para el método clásico
Perimetro = LadoA + LadoB + LadoC
Area = Base * Altura / 2

# Solo para el teorema heron
Perimetro = LadoA + LadoB + LadoC
Sp = Perimetro / 2
Area = ((Sp * (Sp - LadoA) * (Sp - LadoB) * (Sp - LadoC)) ** 0.5)

# Mostando los resultados
print("El perímetro calculado del triangulo es: ", Perimetro)
print("Y su área es de: ", Area)

# 12. Pico y placa
print("Pico y placa")

dia = [
    "Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"
]
pyp = [
    "8-9-0-1", "2-3-4-5", "6-7-8-9", "0-1-2-3", "4-5-6-7", "8-9-0-1", "2-3-4-5"
]

num = int(input("Digite un dia del año: "))

if (num > 0 and num < 366):
    if (num < 7):
        print(dia[num - 1] + " : " + pyp[num - 1])
    elif (num % 7 == 0):
        print(dia[6] + " : " + pyp[6])
    else:
        print(dia[(num - 1) % 7] + " : " + pyp[(num - 1) % 7])
else:
    print("Por favor un dia entre 1 y 366")

# 13. Distancia
print("Distancia establecida entre 20 y 35")
print("Cual es su distancia:")
dis = int(input())

if(dis > 20) and (dis < 35):
    print("Ingrese la velocidad:")
    v = float(input())

    print("Ingrese el tiempo en segundos:")
    t = float(input())

elif (dis < 20):
    print("Muy cerca")
else:
    print("Muy lejos")

d = v*t
print("La distancia es:", d, "mts")

# 14. Numeros
x = int(input('Digite el primer numero: '))
y = int(input('Digite el segundo numero: '))
z = int(input('Digite el tercer numero: '))

menor = min(x, y, z)
mayor = max(x, y, z)
valor_medio = (x + y + z) - menor - mayor

print(valor_medio)

# 15. Raiz cuadrada
x = 81
print(math.sqrt(x))

# 16. Estudiantes gordos
pes40 = 0
pes40y50 = 0
pes50y60 = 0
pes60 = 0

print("Ingrese la cantidad de alumnos: ")
cantidad = int(input())

for i in range(cantidad):
    print('Ingrese el peso del ', i, ' alumno: ')
    peso = int(input())

    if peso < 40:
        pes40 = pes40 + 1
    elif (peso >= 40) and (peso <= 50):
        pes40y50 = pes40y50 + 1
    else:
        if (peso > 50) and (peso < 60):
            pes50y60 = pes50y60 + 1
        else:
            pes60 = pes60 + 1

print('Alumnos con pesos')
print('Menos de 40: ', pes40)
print('Entre 40 y 50: ', pes40y50)
print('Mas de 50 y menos de 60: ', pes50y60)
print('Mas o igual a 60: ', pes60)

# 17. Angulo
print("Ingrese un angulo en grados: ")
angulo = int(input())

if angulo <= 89:
    print("Angulo Agudo")
    print("           *")
    print("         *")
    print("       *")
    print("     *")
    print("   *")
    print(" *")
    print("*************")

if angulo >= 91:
    print("Angulo Obtuso")
    print("*")
    print(" *")
    print("  *")
    print("   *")
    print("    *")
    print("     *")
    print("      *************")

if angulo == 90:
    print("Angulo Recto")
    print("*")
    print("*")
    print("*")
    print("*")
    print("*")
    print("*")
    print("*************")

# 18. Sistemas Estde calificacion
print("Ingrese calificacion numerica")
num = int(input())
if (num >= 90):
    print("su calificacion es A")
elif (num < 90) and (num > 80):
    print("su calificacion es B")
elif (num < 80) and (num >= 70):
    print("su calificacion es C")
elif (num < 70) and (num >= 69):
    print("su calificacion es D")
elif(num < 69):
    print("su calificacion es F")
