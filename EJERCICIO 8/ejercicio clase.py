def palabra_diez_veces():

    programa_activo = True
    contador = 0
    usuario_escribio = input("Escribe una palabra para iniciar el programa: ")
    while programa_activo:
        contador += 1
        print(usuario_escribio)
        if contador >= 10:
            programa_activo = False
    print("Programa finalizado después de mostrar 10 pantallas.")

def edad_conteo():

    programa = True
    edad = int(input("Ingresa tu edad: "))
    print(f"Iniciando conteo a edad de {edad} años:")
    for i in range(1, edad + 1):
        print(i)

def numero_entero_cuenta_impar():

    numero = int(input("Ingresa un número entero: "))
    contador = 0
    for i in range(1, numero + 1):
        if i % 2 != 0:
            contador += 1
    print(f"Los numeros impares de 1 a {numero} son: ")
    for i in range(1, numero + 1):
        if i % 2 != 0:
            print(i, end=" ")
def cuenta_regresiva():

    numero = int(input("Ingresa un número entero para iniciar la cuenta regresiva: "))
    print(f"Iniciando cuenta regresiva desde {numero}:")
    for i in range(numero, 0, -1):
        print(i)
    print("¡Cuenta regresiva finalizada!")

def inversion():
    
    monto_inicial = int(input("Ingresa el monto inicial de la inversión: "))
    tasa_interes = int(input("Ingresa la tasa de interés anual (en porcentaje): "))
    años = int(input("Ingresa el número de años para la inversión: "))
    total = 0 
    for i in range(años):
        total = total + monto_inicial + (monto_inicial * tasa_interes / 100)
        print(total) 
    
def triangulo_asteriscos():

    altura = int(input("Ingresa la altura del triángulo de asteriscos: "))
    for i in range(1, altura + 1):
        print("*" * i)

def tablas():
    for i in range(1, 11):
        for j in range(1, 11):
            resultado = i * j
            print(i, "x", j, "=", resultado)

def piramide_impares():
    altura = int(input("Ingresa la altura de la pirámide de números impares: "))
    for i in range(1, altura + 1):
        for j in range(2 * i - 1, 0, -2):
            print(j, end=" ")
        print()

def contraseña():
    contraseña= "Laboratorio"
    intento = ""
    while intento != contraseña:
        intento = input("Ingresa la contraseña: ")
    print("¡Contraseña correcta! Acceso concedido.")

def num_entero_primo():
    numero = int(input("Ingresa un número entero: "))
    if numero < 2:
        print(numero, "no es primo")      
        return
    print(numero, "es primo")

def palabra_invertida():
    palabra = input("Ingresa una palabra: ")
    palabra_invertida = palabra[::-1]
    print("La palabra invertida es:", palabra_invertida)

def frase_letra():
    frase = input("Ingresa una frase: ")
    letra = input("Ingresa una letra para contar su aparición: ")
    contador = 0
    for char in frase:
        if char == letra:
            contador += 1
    print(f"La letra '{letra}' aparece {contador} veces en la frase.")

def eco():
    palabra = input("Ingresa una palabra: ")
    veces = int(input("¿Cuántas veces quieres que se repita la palabra? "))
    for i in range(veces):
        print(palabra)

opcion= int(input("dame el numero de opciones: "))
match opcion:
    case 1:
        palabra_diez_veces()                    
    case 2:
        edad_conteo()
    case 3:
        numero_entero_cuenta_impar()
    case 4:
        cuenta_regresiva()
    case 5:
        inversion()
    case 6:
        triangulo_asteriscos()
    case 7:
        tablas()
    case 8:
        piramide_impares()
    case 9:
        contraseña()
    case 10:
        num_entero_primo()
    case 11:
        palabra_invertida()
    case 12:
        frase_letra()
    case 13:
        eco()