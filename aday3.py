#calculator 
# x = int(input('first number is '))
# y = int(input('second number is '))
# #for adding
# function1 = input('press + for addition')


# if function1 == '+':
# 	print(x + y) 


#2nd attempt
x , f , z = int(input('first number is ')) , input('operator is ') , int(input('second number is ')) 

if f == '+':
	print('=',x + z)
elif f == '-':
	print('=',x - z)
elif f =='/':
	print('=',x / z)
elif f == '*':
	print('=',x * z)
elif f == '^':
	print('=',x ** z)
else:
	print('operator is not defined yet')
