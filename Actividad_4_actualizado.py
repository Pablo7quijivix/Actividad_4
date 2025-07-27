#actividad numero 1
name= input("Ingerese su nombre completo: ")
dpi=input("Ingrese su DPI: ")
deparment= input("Ingrese departamento: ")
yearofbirth= int(input("Ingrese año de nacimiento: "))

mayor_edad= 2025-yearofbirth
dpi2= len(dpi) # numero de caracteres
name2= len(name)

if name2 > 5:
    print("Nombre valido")
    if dpi2 != 13:
        print("DPI Incorrecto")
        if deparment.lower() == "peten" or deparment.lower() == "alta verapaz":
            print("Los departamentos de Petén y Alta Verapaz votan desde los 17 años")




