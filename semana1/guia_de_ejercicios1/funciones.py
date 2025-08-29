#1
def saludar(nombre:str)-> None:
    print(f"hola {nombre}")

#2
def operaciones (num1:int,num2:int)->int:
    resultado_suma=num1+num2
    resultado_resta=num1-num2
    resultado_multiplicacion=num1*num2

    print(f"suma {resultado_suma}")
    print(f"resta{resultado_resta}")
    print(f"multiplicacion{resultado_multiplicacion}")

#4
def buscar_mayor(num1:int,num2:int,num3:int):
    if num1 > num2 and num1 >num3:
        if num2 > num3:
            print(f"el numero {num1}  es el mayor")
    elif num2 > num1 and num2 > num3:
        if num1 > num3:
            print(f"el numero {num2} es el mayor")
    else:
        print(f"el numero {num3} es el mayor")


#5 

def es_par(numero:int):
    if numero % 2==0:
        print(f"el numero {numero} es par")
    else:
        print(f"el numero {numero} es impar")


#7

def verificar_acceso(edad):

    if edad >=18:
        print("es mayor de edad.")
    else:
        print("es menor de edad.")





