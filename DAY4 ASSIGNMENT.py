#1st function should take all data types and print in efficient manner


def data_type(int,flt,str,boolean,list,set,tuple,dict):

    print(f'the integer number in the datatype is   :   {int}\n'
          f'the float number in the data type is    :   {flt}\n'
          f'the string in the data type is          :   {str}\n'
          f'the boolean values in the data type is  :   {boolean}\n'
          f'the list in the data type is            :   {list}\n'
          f'the set in the data type is             :   {set}\n'
          f'the tuple in the data type is           :   {tuple}\n'
          f'the dictionary in the data type is      :   {dict}')


int,flt,str,boolean,list,set,tuple,dict=1,2.6,'this is STRING',True,([1,23,4,'this is LIST']),({1,2,3,'this is A SET'}),((1,3,'this is TUPLE')),({'name' : 'sai','age' : 18})

data_type(int,flt,str,boolean,list,set, tuple, dict)


#2nd function should take a dict and using for loop --> print as a key and value in efficient manner

def iterate_over_dict(a):
    for key,value in a.items():

        print(f'key is : {key} & value is : {value}')

a=({'name' : 'SAI','age' : 11,'place' : 'INDIA','college': 'IND UNIVERSITY','contact info ': 123456 })

iterate_over_dict(a)

#3 FUNCTON3 SHOULD TAKE 2NUMBERS AND PRINT IT AS A LIST


def take_as_list(a,b):
    list=[]
    list.append(a)
    list.append(b)

    print(f'the list is : {list}')

take_as_list(1,2)