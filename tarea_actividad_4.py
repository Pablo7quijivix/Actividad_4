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
'''
#codigo numero 2: Calculadora de impuestos progresivos
ingreso_anual=int(input("Escriba sus ingresos anuales: \n"))
dependientes= int(input("ingrese numero de dependientes: \n"))

deducciones= 1000*dependientes

if ingreso_anual >=0 and ingreso_anual <=30000:
    caso1= ingreso_anual * (5/100)
    print(f"De Q0.00 a Q30,000 el impuesto progresivo es del 5%, total= Q{caso1}")
elif  ingreso_anual >= 30001 and ingreso_anual <= 60000:
    caso2= ingreso_anual* (10/100)
    print(f"De Q30,001 a Q60,000 el impuesto progresivo es del 10%, total=Q{caso2}")



