'''
codigo numero 1
simulador de votacion con validacion cruzada
'''
while True:
    name=input("Ingrese su nombre (nombre y apellido): ") #ejemplo de un nombre completo
    #Arwen Dayanne Rivera Rios, este nombre contiene aprox 25 caracteres, contando espacios
    dpi=input("ingrese su numero de DPI (debe contener 13 digitos): ")
    department= input("ingrese su departamento de origen: ")
    yearofbirth=int(input("Ingrese su fecha de nacimiento: "))

    if len(name) <=5:
        print ("Nombre incorrecto,  ingrese un nombre mayor a 5 caracteres")
    elif len(dpi) != 13 or not dpi.isdigit(): #esta funcion es una funcion de python que sirve para verificar que en nuestra variable "dpi" hayan unicamente numeros
        print("Numero de DPI invalido, ingrese un DPI correcto")



