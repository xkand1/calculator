def Summirovanie(x, y):
   return x + y
def Vychitanie(x, y):
   return x - y
def Umnojenie(x, y):
   return x * y

print("Vyberite zadachu.")
print("1.Summirovanie")
print("2.Vychitanie")
print("3.Umnojenie")

choice = input("Выберите одно(1/2/3/4):")
num1 = int(input("Введите первое число: "))
num2 = int(input("ВВедите второе число: "))

if choice == '1':
   print(num1,"+",num2,"=", Summirovanie(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", Vychitanie(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", Umnojenie(num1,num2))