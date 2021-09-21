x= 123
def Converter (q_number):
    return int(q_number)
print(Converter(x))


 x = 123.45
 def Converter2 (w_number):
     return int(w_number)
 print (Converter2(x))

x = 123

def Converter3(e_number):
    return float(e_number)

print(Converter3(x))

card_number= int(input("Номер карты: "))
def Card (adc):
    return str(adc)[-4:]
print(Card(card_number))


number= int(input("Любое число: "))
def Number2 (abc):
    a= abc//100
    b= ((abc/10)%10)
    c= abc%10
    return [a+b+c]
print(Number2(number))

a= float(input("Первая сторона "))
b= float(input("Вторая сторона "))
 def square (ab):
     return (0.5(ab)
 print(square(a*b))

num = int(input("Введите целое: "))
sum = 0
while (num != 0):
    sum = sum + num % 10
    num = num // 10
print("Сумма цифр числа равна: ",sum)


nun = int(input("Введите число: "))
 count= 0
 while (nun !=0):
     nun=nun//10
     count=count +1
print("Cумма цифр числа: ", count)






print("Cумма цифр числа: ", n2)
n1 = int(input("Введите целое число: "))
n2 = 0

while n1 > 0:

    n3 = n1 % 10

    n1 = n1 // 10

    n2 = n2 * 10

    n2 = n2 + n3

print('"Обратное" ему число:', n2)



