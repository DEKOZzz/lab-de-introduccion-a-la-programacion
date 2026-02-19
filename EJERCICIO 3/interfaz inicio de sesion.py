usuario = "Admin"
contraseña = "Admin2026"
intentos: 0
maximo_intentos: 3

while intentos < maximo_intentos:
    print("inicio de sesion")

    Usuario = input("usuario:")
    contraseña = input ("contraseña")
    if not usuario: 
        print("no pusiste nada wey")
    
    valido = True 
    for c in usuario:
        if not (c.isdigit() or ('a' <= c <= 'z') or ('A' <= c <= 'Z')):
            valido = False
            break
    if not valido:
        print("solo acepto letras y numeros")
    elif len(contraseña) < 8:
        print("tienes que poner almenos 8 caracteres")
    if not

   
    if not usuario:
        print ("no no chikitin intenta de nuevo")

