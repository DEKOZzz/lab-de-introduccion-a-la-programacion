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

