number=int(input('enter a Number : '))
copy=number
rev=0
while(number!=0):
    rem=number%10
    rev=rev*10+rem
    number//=10
if copy==rev:
    print('Palindrome Number')
else:
    print('Not a Palindrome Number')
    
