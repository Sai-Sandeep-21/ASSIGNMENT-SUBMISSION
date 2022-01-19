#ASSIGNMENT 1 : TO USE DIFFERENT PRINT STATEMENTS ON 7 TYPES OF VARIABLES
#(1) USING STRING
fruit=input('enter any fruit : ')
print('the fruit is an : ',fruit)
print("the fruit is an : %s"%(fruit))
print('the fruit is an :{}'.format(fruit))
print(f'the fruit is an : {fruit}')
#(2) USING INTEGER
num =int(input('enter an interger : '))
print('the given number is : ',num)
print('the given number is : %s'%num)
print('the given number is : {}'.format(num))
print(f'the given number is :{num}')
#(3) USING FLOATING NUMBER
float_num=float(input('enter any num : '))
print('the given float number is : ',float_num)
print('the given float number is : %s '%float_num)
print('the given float number is : {}'.format(float_num))
print(f'the given float number is : {float_num}')
#(4) USING TUPLE
tuple_val=tuple(input('enter all the elements in tuple:'))
print('the given tuple is : ',tuple_val)
print('the given tuple is : %s'%(tuple_val,))
print('the given tuple is : {}'.format(tuple_val))
print(f'the given tuple is : {tuple_val}')
#(5) USING LIST
list_val=list(('name',1,'place,3.5'))
print('the given list data is : ',list_val)
print('the given list data is : %s'%list_val)
print('the given list data is : {}'.format(list_val))
print(f'the given list data is : {list_val}')
#(6) USING SET
set_val=set(('name',1,'place,3.5'))
print('the given set data is : ',set_val)
print('the given set data is :  %s'%set_val)
print('the given set data is :  {}'.format(set_val))
print(f'the given set data is :  {set_val}')
#(7) USING DICTIONARY
dict_val={ 'name ':'sai','age':21,'nationality ':'Indian'}
print('the given dictionary data is : ',dict_val)
print('the given dictionary data is :  %s'%dict_val)
print('the given dictionary data is :  {}'.format(dict_val))
print(f'the given dictionary data is :  {dict_val}')