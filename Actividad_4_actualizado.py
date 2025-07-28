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
from pickletools import read_string1, read_uint2

#CODIGO 2 CALCULADORA DE IMPUESTOS PROGRESIVOS + DEDUCCIONES
ingreso_anual= float(input("Digite su ingreso anual: "))
no_dependientes= float(input("Digite su numero de dependientes: "))

no_dependientes2 = no_dependientes * 1000

des1= float(ingreso_anual * 0.05)
des2 = float (ingreso_anual *0.1)
des3 = float(ingreso_anual * 0.15)
des4 = float (ingreso_anual * 0.2)
if 0 <= ingreso_anual <= 30000:
    if 30001 <= ingreso_anual <= 60000:
        if 60001 <= ingreso_anual >=100000:
            if ingreso_anual > 100000:
                if ingreso_anual < 40000 and no_dependientes > 2:
                    print("=======CALCULADORA DE IMPUESTOS PROGRESIVOS + DEDUCCIONES=======")
                    print("=====RESUMEN DE CALCULOS=====")
                    print(f"NO PAGA IMPUESTOS POR INGRESOS MENORES A {ingreso_anual} Y DEPENDIENTES MAYORES A 2")
                else:
                     pass
            else:
                print("=======CALCULADORA DE IMPUESTOS PROGRESIVOS + DEDUCCIONES=======")
                print("=====RESUMEN DE CALCULOS=====")
                print(f"==DESCUENTO DEL 20% + Q1,000.00 POR DEPENDIENTE==\n POR ENDE PAGA UN TOTAL: {des4} ")
        else:
            print(f"=======CALCULADORA DE IMPUESTOS PROGRESIVOS + DEDUCCIONES =======")
            print(f"====RESUMEN DE CALCULOS====")
            print(f"==DESCUENTO DEL 15% + Q1,000.00 POR DEPEDIENTE==\n POR ENDE PAGA UN TOTAL: {des3}")
    else:
        print(f"=======CALCULADORA DE IMPUESTOS PROGRESIVOS + DEDUCCIONES =======")
        print(f"====RESUMEN DE CALCULOS====")
        print(f"==DESCUENTO DEL 10% + Q1,000.00 POR DEPEDIENTE==\n POR ENDE PAGA UN TOTAL: {des2}")
else:
    print(f"=======CALCULADORA DE IMPUESTOS PROGRESIVOS + DEDUCCIONES =======")
    print(f"====RESUMEN DE CALCULOS====")
    print(f"==DESCUENTO DEL 5% + Q1,000.00 POR DEPEDIENTE==\n POR ENDE PAGA UN TOTAL: {des1}")





