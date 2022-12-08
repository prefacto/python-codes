d={"virat kohli":52,"sachin":100,"dhoni":28}
for key in d:
    print("centuries scored by",key,"=",d[key])
         
            #1#
car = {"brand": "Ford","model": "Mustang","year": 1964}
x = car.keys()
print(x)
car["color"] = "white"
print(x)

            #3#
car = {"brand": "Ford","model": "Mustang","year": 1964}
x = car.values()
print(x)
car["year"] = 2020
print(x)

                #4#
thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")           

                 #5#
hisdict = {"brand": "Ford","model": "Mustang","year": 1964}
thisdict.update({"year": 2020})
                 #6#
thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
mydict = thisdict.copy()
print(mydict)
                 #7#
myfamily = {"child1" : {"name" : "Emil","year" : 2004},"child2" : {"name" : "Tobias","year" : 2007},"child3" : {"name" : "Linus","year" : 2011}}

                #8#
thisdict = {"brand": "Ford","model": "Mustang","year": 1964}
thisdict.clear()
print(thisdict)

                 #9#
# Creating a Dictionary
# with Integer Keys
Dict = {1: 'Computer', 2: 'Engg', 3: 'Python'}
print("\nDictionary with the use of Integer Keys: ")
print(Dict)

# Creating a Dictionary
# with Mixed keys
Dict = {'Name': 'Computer', 1: [1, 2, 3, 4]}
print("\nDictionary with the use of Mixed Keys: ")
print(Dict)
# Creating an empty Dictionary
Dict = {}
print("Empty Dictionary: ")
print(Dict)

# Creating a Dictionary
# with dict() method
Dict = dict({1: 'Computer', 2: 'Engg', 3: 'Python'})
print("\nDictionary with the use of dict(): ")
print(Dict)

# Creating a Dictionary
# with each item as a Pair
Dict = dict([(1, 'Computer'), (2, 'Engg')])
print("\nDictionary with each item as a pair: ")
print(Dict)

# Creating a Nested Dictionary
# as shown in the below image
Dict = {1: 'Computer', 2: 'Engg',
3: {'A': 'Welcome', 'B': 'To', 'C': 'Python'}}
print(Dict)

# Creating an empty Dictionary
Dict = {}
print("Empty Dictionary: ")
print(Dict)

# Adding elements one at a time
Dict[0] = 'Computer'
Dict[2] = 'Engg'
Dict[3] = 1
print("\nDictionary after adding 3 elements: ")
print(Dict)

# Adding set of values
# to a single Key
Dict['Value_set'] = 2, 3, 4
print("\nDictionary after adding 3 elements: ")
print(Dict)

# Updating existing Key's Value
Dict[2] = 'Welcome'
print("\nUpdated key value: ")
print(Dict)

# Adding Nested Key value to Dictionary
Dict[5] = {'Nested': {'1': 'Computer', '2': 'Engg'}}
print("\nAdding a Nested Key: ")
print(Dict)

# Python program to demonstrate
# accessing a element from a Dictionary

# Creating a Dictionary
Dict = {1: 'Computer', 'name': 'For', 3: 'Engg'}

# accessing a element using key
print("Accessing a element using key:")
print(Dict['name'])

# accessing a element using key
print("Accessing a element using key:")
print(Dict[1])
# Creating a Dictionary
Dict = {1: 'Computer', 'name': 'For', 3: 'Engg'}

# accessing a element using get()
# method
print("Accessing a element using get:")
print(Dict.get(3))


#Accessing an element of a nested dictionary
#In order to access the value of any key in the nested dictionary, use indexing [] syntax.

# Creating a Dictionary
Dict = {'Dict1': {1: 'Computer'},
'Dict2': {'Name': 'For'}}
# Accessing element using key
print(Dict['Dict1'])
print(Dict['Dict1'][1])
print(Dict['Dict2']['Name'])


#Dictionary methods
# demo for all dictionary methods
dict1 = {1: "Python", 2: "Java", 3: "Ruby", 4: "Scala"}

# copy() method
dict2 = dict1.copy()
print(dict2)

# clear() method
dict1.clear()
print(dict1)

# get() method
print(dict2.get(1))

# items() method
print(dict2.items())

# keys() method
print(dict2.keys())

# pop() method
dict2.pop(4)
print(dict2)

# popitem() method
dict2.popitem()
print(dict2)

# update() method
dict2.update({3: "Scala"})
print(dict2)

# values() method
print(dict2.values())
