n1 = float(input("enter first number; "))
n2 = float(input("enter second number: "))
n3 = float(input("enter third number: "))
n4 = float(input("enter forth number: "))
n5 = float(input("enter fifth number: "))
n6 = float(input("enter sixth number: "))
ave = (n1+n2+n3+n4+n5+n6)//6
print(f'average is: {ave}')
if  ave<0 :
    print('average is negetive')
elif 0<= ave <= 10 :
    print('the average is between 0&10')
elif 11<= ave <= 20 :
    print('the average is between 11&20')
elif ave > 20:
    print('the average is bigger than 20' )
