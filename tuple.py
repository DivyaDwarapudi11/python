"""
tuple is a collections of items/values/elements
they are enclosed within the parenthis or open brackets()seperated by(,)
as tuples are immuatable it mean we cant change
so when the data is fixed we can go with tuples
"""
#eg1:
mytuple = (13,11,12)
print(type(mytuple))#<class tuple>
mytuple2=()#<empty tuple>
print(type(mytuple2))#<class tuple>
mytuple3=(10)
print(type(mytuple3))#<class int>
"""
Note:when you wanna a create a tuple with single value 
it should be created by 
"""
#creation of the tuple
#syntax:tuplevariable=(val1,val2,val3,..valn)
mytuple=(12,23,45,34+78j,[12,34,45],"hello",(123,"ece"))
print(mytuple5)
#creating the tuple with single element
mytuple6=(45,)
print(type(mytuple6))
#creating the tuple with list
t=[23,45,56,"jj"]
print(t)
k=tuple(t)
print(k)
#creating the tuple with "tuple" predefined word



