def Summirovanie(x, y):
   return x + y

print("Vyberite zadachu.")
print("1.Summirovanie")


choice = input("Выберите одно(1/2/3/4):")
num1 = int(input("Введите первое число: "))
num2 = int(input("ВВедите второе число: "))

if choice == '1':
   print(num1,"+",num2,"=", Summirovanie(num1,num2))

