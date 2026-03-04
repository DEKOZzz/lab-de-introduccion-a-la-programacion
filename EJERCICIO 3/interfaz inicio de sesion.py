usuario_valido = "Admin"
contraseña_valida = "Admin2026"

intentos = 0
maximo_intentos = 3

while intentos < maximo_intentos:
    print                ("inicio de sesion")

    usuario = input("usuario: ")
    contraseña = input ("contraseña: ")
    
    if not usuario: 
        print              ("no pusiste nada en el usuario wey")
        intentos += 1
        continue
    
    valido = True 
    for c in usuario:
        if not (c.isdigit() or ('a' <= c <= 'z') or ('A' <= c <= 'Z')):
            valido = False
            break
    if not valido:
        print("solo acepto letras y numeros en el usuario pa")
        intentos += 1
        continue
    
    
    
    if len(contraseña) < 8:
        print("tienes que poner en la contraseña almenos 8 caracteres")
        intentos += 1
        continue
    
    tiene_letra = False
    tiene_numero = False

    for c in contraseña:
        if c.isdigit():
            tiene_numero = True
        if ('a' <= c <= 'z') or ('A' <= c <= 'Z'):
            tiene_letra = True
    
    if not tiene_letra or not tiene_numero:
        print      ("La contraseña almenos debe tener 1 numero y 1 letra echale ganas tilin ")
        intentos += 1
        continue
   
    if usuario == usuario_valido and contraseña == contraseña_valida:
        print                   ("Esta bien,te dejare pasar nomas por hoy")
        break
    else:
        print                    ("NO NO NO intentale de nuevo wey")
        intentos += 1

if intentos == maximo_intentos:
    print     ("MIRA WE YA TE PASE MUCHAS, me voy a Autodestruir en 3 2 1.......")


while True:
    print("Menú de opciones:")
    print("1. Clasificar número")
    print("2. Categoria de edad y permisos")
    print("3. Calcular Tarifa Final")
    print("4. Cerrar Sesión")
    print("5. Salir")

    seleccion = input("Selecciona una opción (1-5): ")
    if seleccion == '1':
        print("Clasificar número.")
        while True:
            try:
                número = int(input("Ingresa un número: "))
                if número > 0:
                    print("El número es positivo.")
                elif número < 0:
                    print("El número es negativo.")
                if número %2 == 0:
                    print("El número es par.")
                else:
                    print("El número es impar.")
                break
            except ValueError:
                print("Por favor, ingresa un número válido we.")
    
    elif seleccion == '2':
        print("Categoria de edad y permisos.")
        while True:
        
            try:
                edad = int(input("Ingresa tu edad:"))
                if edad < 0:
                    print("Tu edad no puede ser negativa mi bro (como vas a tener -0 años). Intenta de nuevo.")
                elif edad <= 12:
                    print("Eres un escuincle no puedes registrarte .")
                elif 13 <= edad < 18:
                    print("Eres un adolescente, puedes registrarte pero no puedes manejar ni hacer compras sin tutor chaval.")
                elif 18 <= edad :
                    print("Eres mayor de edad puedes conducir y hacer compras sin Tutor.")
                elif edad >= 21:
                    print("Tienes el servicio VIP :D puedes hacer lo que quieras sin restricciones.")
                break
            except ValueError:
                print("Por favor, ingresa una número válido.")

    elif seleccion == '3':
        print("Calcular Tarifa Final.")
        tarifa_base = 200.0
        
    while True: 
        try:
            descuento_total = 0.0
            recargo = 0.0
            edad = int(input("Ingresa tu edad: "))
            if edad < 0 or edad > 120:
                print("Tu edad no es válida, por favor ingresa una edad entre 0 y 120.")
                continue
            Dia_de_la_semana = int(input("Ingresa el día de la semana (1=Lun... 7= Dom): "))
            if Dia_de_la_semana < 1 or Dia_de_la_semana > 7:
                print("Día de la semana no válido, por favor ingresa un número entre 1 y 7.")
                continue
            estudiante = input("¿Eres estudiante? (s/n): ").lower()
            if estudiante not in ['s', 'n']:
                print("Respuesta no válida, por favor ingresa 's' para sí o 'n' para no.")
                continue
            miembro = input("¿Eres miembro del club? (s/n): ").lower()
            if miembro not in ['s', 'n']:
                print("Respuesta no válida, por favor ingresa 's' para sí o 'n' para no.")
                continue
            metodo_pago = input("¿Cuál es tu método de pago? (E= Efectivo, T= Tarjeta): ").upper()
            if metodo_pago not in ['E', 'T']:
                print("Método de pago no válido, por favor ingresa 'E' para efectivo o 'T' para tarjeta.")
                continue
            
            #recargos y descuentos de agencia chikitines
            if Dia_de_la_semana == 6 or Dia_de_la_semana == 7:
                recargo = tarifa_base * 0.10
            if edad 
            
    elif seleccion == '4':
        print("Cerrando sesión...")
        break  
    elif seleccion == '5':
        print("Saliendo del programa...")
        exit()  
    else:
        print("Opción no válida, por favor selecciona una opción entre 1 y 5.")
        intentos += 1
        continue

