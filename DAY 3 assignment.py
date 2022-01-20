#2ND METHOD
name=input('enter the name : ')
age=int(input('enter the age : '))
address=input('enter the address : ')
qualif=input('enter the qualification : ')
ph_num =int(input('enter phone num : '))

list=[]
list.append(name)
list.append(age)
list.append(address)
list.append(qualif)
list.append(ph_num)
print('this is the list of personal details of a person',list)
print(f'the name of the person is: {list[0]}\n'
      f'the age of the person is : {list[1]}\n'
      f'the person lives in : {list[2]}\n'
      f'the qualification of the person is{list[3]}\n'
      f'the contact of the person is : {list[4]}')