# Ejercicios Python Pt1 (ejercicio faltante #10)

# 1. Edad
print("ingrese su nombre")
nombre = input()
print("ingrese su edad")
edad = int(input())
print("ingrese identificacion")
id = int(input())
print("su nombre es", (nombre), "su edad es ",
      (edad), "su identificacion es ", (id))
if edad >= 18:
    print("mayor de edad")
else:
    print("menor de edad")


# 2 y 4. Numero decimal a binario, octal y hexadecimal Opcion 1 
def hexa(num):

    hexadecimal = ""
    while num != 0:
        cambios = cambio(num % 16)
        hexadecimal = str(cambios) + hexadecimal
        num = int(num / 16)
    print('El decimal en hexadecimal es:', hexadecimal)

def binario(decimal):
    binario = ""
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario

def num_octal(decimal):
    octal = ""
    while decimal > 0:
        residuo = decimal % 8
        octal = str(residuo) + octal
        decimal = int(decimal / 8)
    return octal

def cambio(digito):
    decimal = [10, 11, 12, 13, 14, 15]
    hexadecimal = ["A", "B", "C", "D", "E", "F"]
    for cont in range(7):
        if digito == decimal[cont - 1]:
            digito = hexadecimal[cont - 1]
    return digito

numero = int(input("Ingresa un número decimal: "))

# decimal a binario
print("El decimal en binario es: ", binario(numero))

# decimal a octal
#octal = num_octal(numero)
print("El decimal en octal es: ", num_octal(numero))
hexa(numero)

# 2 y 4. Numero decimal a binario, octal y hexadecimal Opcion 2

def num_hexadecimal(valor):
    valor = str(valor)
    arrays = {
        "10": "A",
        "11": "B",
        "12": "C",
        "13": "D",
        "14": "E",
        "15": "F",
    }
    if valor in arrays:
        return arrays[valor]
    else:
        return valor


def num_decimal(numero):
    hexadecimal = ""
    while numero > 0:
        res = numero % 16
        caracter = num_hexadecimal(res)
        hexadecimal = caracter + hexadecimal
        numero = int(numero / 16)
    return hexadecimal


def binario(decimal):
    binario = ""
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario


def num_octal(decimal):
    octal = ""
    while decimal > 0:
        residuo = decimal % 8
        octal = str(residuo) + octal
        decimal = int(decimal / 8)
    return octal


numero = int(input("Ingresa un número decimal: "))
# decimal a binario
print("El decimal en binario es:", binario(numero))

# deciaml a octal
octal = num_octal(numero)
print("El decimal en octal es:", octal)

# deciaml a hexadecimal
hexadecimal = num_decimal(numero)
print("El decimal en hexadecimal es:", hexadecimal)

# 3. Numero binario a decimal
print("Ingrese un numero binario:")
binario = input()
decimal = 0
for digito in binario:
    if int(digito) > 1:
        print("Error!, ese no es un numero binario")
        raise ValueError
    decimal = decimal*2 + int(digito)
print("El numero en binario es: ", decimal)

# 5. Promedio
print("ingrese primer numero")
num1 = int(input())
print("ingrese segundo numero")
num2 = int(input())
print("ingrese tercer numero")
num3 = int(input())
Suma = (num1 + num2 + num3)
prom = (Suma)/3
print("La suma es ", Suma)
print("El promedio es:", prom)

# 6. Minicalculadora
print("ingrese primer numero")
num1 = int(input())
print("ingrese segundo numero")
num2 = int(input())
Suma = (num1 + num2)
resta = (num1 - num2)
producto = (num1 * num2)
division = (num1 / num2)
exponente = (num1 ** num2)
modulo = (num1 % num2)
print("La suma es de: ", Suma)
print("La resta es de: ", resta)
print("El Producto es de: ", producto)
print("La division es de: ", division)
print("La potencia es de :", exponente)
print("El modulo de la division es de:", modulo)

a, b = b, a
print(f"El nuevo valor de a es {a}")
print(f"El nuevo valor de b es {b}")

# 7. IVA
print("Ingrese el precio del producto")
produ = int (input())

calcu = produ * 0.19
total = produ - calcu
print("Iva es: ", calcu)
print("El descuento del producto es: ",total)

# 8. Convertir Unidades
print("Ingrese los megas que tiene: ")
N1 = int(input())

bits = N1 / 0.125
bytess = N1 * 1024 * 1024
kb = N1 * 1024
mg = N1 / 1024

print("Los bits son: ",bits)
print("Los bytes son: ",bytess)
print("Los kilobytes son: ",kb)
print("Los megabytes son: ",mg)

# 9. Exponente
print("ingrese la base")
Base = int(input())
print("ingrese el exponente")
exponente = int(input())
res =  (Base ** exponente)
#Forma 2
res =  pow(Base, exponente)

print("Resultado es de :", res)
print("Resultado es de :", res)

# 10. Tipo de dato


# 11. Longitud del valor
print("¿Como te llamas?")
nombre = input()
print("Bienvenido", nombre)
print("Se ha ingresado ", len(nombre), "carcateres")

# 12. Ejercicio Area Circulo
print("Area Circulo")
pi = 3.14
radio = int(input("Ingresa el valor del radio: "))
area = (radio ** 2) * pi
print("El area es ",  area)

# 13. Ejercicio Area Triangulo
print("Area del triangulo")
base = input("Ingrese la base: ")
altura = input("Ingrese la altura: ")
area = int(base) * int(altura) / 2.0
print("el resultado es: " + str(area))

# 14. Intercambio de variable
a = input("a -> ")
b = input("b -> ")

a , b = b , a
print(f"El nuevo valor de a es {a}")
print(f"El nuevo valor de b es {b}")