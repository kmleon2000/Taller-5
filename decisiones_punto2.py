num1 = int(input("Ingrese el primer valor: "))
num2 = int(input("Ingrese el segundo valor: "))
num3 = int(input("Ingrese el tercer valor: "))

if(num1 < num2):
    if(num2 < num3):
        print("El mayor de los valores es: ",num3)
    else:
        print("El mayor de los valores es: ",num2)
else:
    if(num1 < num3):
        print("El mayor de los valores es: ",num3)
    else:
        print("El mayor de los valores es: ",num1)