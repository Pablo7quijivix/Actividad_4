#actividad numero 1
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
                print("NO es mayor de edad")
        else:
            print("__________Votante Válido_________")
            print(f"Bienvenido {name} su centro de votación está es {deparment} ")
    else:
        print("DENEGADO POR DPI InValido")
else:
    print(f"======USUARIO NO PUEDE VOTAR POR: =====")
    print("NO es mayor de edad")




