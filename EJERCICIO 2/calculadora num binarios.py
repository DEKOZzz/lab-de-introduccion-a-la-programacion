def convertir_base (numero, base) :
    resultado = ""
    digitos = "0123456789ABCDEF"
    while numero > 0 :
        residuo = numero % base
        resultado = digitos[residuo]+resultado
        numero = numero // base
    return resultado
numero = int(input("ingresa un numero decimal: ")) 
print (convertir_base(numero, 2)) 
print (convertir_base(numero, 8))
print (convertir_base(numero, 16))