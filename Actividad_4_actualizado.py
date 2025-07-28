#actividad numero 1
'''
name= input("Ingerese su nombre completo: ")
dpi=input("Ingrese su DPI: ")
deparment= input("Ingrese departamento: ")
yearofbirth= int(input("Ingrese año de nacimiento: "))

mayor_edad= 2025-yearofbirth
dpi2= len(dpi) # numero de caracteres
name2= len(name)

if name2 > 5:
    #print("Nombre valido")
    if dpi2 == 13:
        #print("DPI Correcto")
        if deparment.lower() == "peten" or deparment.lower() == "alta verapaz":
           # print("Los departamentos de Petén y Alta Verapaz votan desde los 17 años")
            if mayor_edad >= 18:
                print("__________Votante Válido_________")
                print(f"Bienvenido {name} su centro de votación está es {deparment} ")
            else:
                print(f"======USUARIO NO PUEDE VOTAR POR: =====")
                print("---NO ES MAYOR DE EDAD---")
        else:
            print("__________Votante Válido_________")
            print(f"Bienvenido {name} su centro de votación está es {deparment} ")
    else:
        print(f"======USUARIO NO PUEDE VOTAR POR: =====")
        print("---DPI INVALIDO---")
else:
    print(f"======USUARIO NO PUEDE VOTAR POR: =====")
    print("---NO es mayor de edad---")
'''


#CODIGO 2 CALCULADORA DE IMPUESTOS PROGRESIVOS + DEDUCCIONES
ingreso_anual= int(input("Digite su ingreso anual: "))
no_dependientes= int(input("Digite su numero de dependientes: "))
no_dependientes2 = no_dependientes * 1000

if 0 <= ingreso_anual <= 30000:
    descuento1= ingreso_anual * 0.05 #descuento1 del 5%
    if 30001 <= ingreso_anual >= 60000:
        descuento2 = ingreso_anual *0.1 #descuento2 del 10%
        if 60001 <= ingreso_anual >=100000:
            descuento3 = ingreso_anual * 0.15 #descuento3 del 15%
            if ingreso_anual > 100000:
                descuento4 = ingreso_anual * 0.2 #descuento4 del 20%
                if ingreso_anual < 40000 and no_dependientes > 2:
                    print(f"NO PAGA IMPUESTOS")
                else:
                    pass
            else:





