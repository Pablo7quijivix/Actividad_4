'''
codigo numero 1
simulador de votacion con validacion cruzada

while True:
    name=input("Ingrese su nombre (nombre y apellido): ") #ejemplo de un nombre completo
    #Arwen Dayanne Rivera Rios, este nombre contiene aprox 25 caracteres, contando espacios
    dpi=input("ingrese su numero de DPI (debe contener 13 digitos): ")
    department= input("ingrese su departamento de origen: ")
    yearofbirth=int(input("Ingrese su año de nacimiento: "))

    department2=department.lower()

    if len(name) <=5: #conditional name
        print ("Nombre incorrecto,  ingrese un nombre mayor a 5 caracteres")

    if department2== "peten" or "alta verapaz":
        print("El departamento de Petén y Alta Verapaz, pueden votar desde los 17 años ")

    if len(dpi) != 13 or not dpi.isdigit(): #conditonal dpi
        print("Ingrese un numero de dpi correcto (13 digitos): ")

    if  yearofbirth >=18: #conditional yearofbirth
        print(f"{name} es mayor de 18 años, puede votar!")
    else:
        print (f"{name} es manor de edad, NO PUEDE VOTAR")

#codigo numero 2: Calculadora de impuestos progresivos
ingreso_anual=int(input("Escriba sus ingresos anuales: \n"))
dependientes= int(input("ingrese numero de dependientes: \n"))

deducciones= 1000*dependientes

if ingreso_anual >=0 and ingreso_anual <=30000:
    caso1= ingreso_anual * (5/100)
    print(f"De Q0.00 a Q30,000 el impuesto progresivo es del 5%, total= Q{caso1}")
    if ingreso_anual /12 <= 40000 and dependientes > 2:
        print(f"____Tiene más de 2 dependientes___({dependientes})")
        print(f"___No paga impuestos____")
elif  ingreso_anual >= 30001 and ingreso_anual <= 60000:
    caso2= ingreso_anual* (10/100)
    print(f"De Q30,001 a Q60,000 el impuesto progresivo es del 10%, total=Q{caso2}")
elif ingreso_anual >= 60001 and ingreso_anual <= 100000:
    caso3= ingreso_anual * (15/100)
    print(f" De Q60,001 a Q100,000 el impuesto progresivo es de 15%, total= Q{caso3}")
elif ingreso_anual >100000:
    caso4= ingreso_anual * (20/100)
    print(f"más de Q100,000 el impuesto progresivo es de 20%, total= Q{caso4}")

'''
#codigo numero 3
#sistema de autenticacion avanzado con penalización
resgistro_usu={
    "pablo": "567",
    "jimena": "cristiano",
    "apolo": "ares"
}
intentos= 3 #intentos permitidos segun el codigo

while intentos > 0:
    usuario= input("Ingrese su usuario (su nombre):  ")
    passward= input("Ingrese su contraseña: ")

    if usuario in resgistro_usu:





