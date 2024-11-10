num = int(input("enter an integer number : "))
#sum1:مجموع اعدادفرد از صفر تا عدد ورودی
sum1 = 0
#sum2:مجموع اعداد مضرب 5 از صفر تا عدد ورودی
sum2 = 0
for i in range(num):
    if i%2==1:    
        sum1+=i
    if i%5==0:
        sum2 += i
mult = sum1*sum2
print("the multyply of sum1 & sum2 is : ",mult)        
