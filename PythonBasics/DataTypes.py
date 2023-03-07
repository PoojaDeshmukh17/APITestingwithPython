# WAP to print Hello
# 1)print("Hello")   -> Hello
# 2)a = 3
#    b = 4
#    print(a+b)

print("*************************************************")

# *Data types in Python:
# 1) Numeric
# a) int:holds signed integers of non-limited length.
# a=100
# print("Int value", a, " is ", type(a))

a = 999999999
b = 999999999
print(a+b)

print("*************************************************")

# b)long-holds long integers(exists in Python 2.x, deprecated in Python 3.x).

print("*************************************************")

# c)float-holds floating precision numbers and it’s accurate up to 15 decimal places.
# b=10.2345
# print("float value", b, " is ", type(b))

print("*************************************************")

# d)complex- holds complex numbers.
c = 100+3j
print("complex value", c, " is ", type(c))

# NOTE: In Python, we need not declare a datatype while declaring a variable like C or C++.
#       We can simply just assign values in a variable.
#       But if we want to see what type of numerical value is it holding right now, we can use type()


print("*************************************************")

# 2)String
str = "Hello"
print(str)

a = "string in a double quote"
b= 'string in a single quote'
print(a)
print(b)

# using ',' to concatenate the two or several strings
print(a,"concatenated with",b)

#using '+' to concate the two or several strings
print(a+" concated with "+b)

#convert int to string
a = 10
print(a)

#st = str(a)
#print(st)

# WAP to print two data types in one statements:
b, c, d = 4, 5.6, "String"
# print("value is"+b) -> error in python ( We cannot concat two diff data types in python)
# To print two data types on one statements we use format method
print("{} {}".format("Value is", d))

# To print what type of variables we pass:
print(type(b))

print(type(c))

print((type(d)))

print("*************************************************")


# 3)List:
# List is data type that allowa multiple valuse and can be diff data types
# Index value start of "0"
values = [1, 2, "Pooja", 4, 5]
print(values[0])
print(values[3])
print(values[-1])               # -1 refers last value of the list
print(values[1:4])              # To print (2, "Rahul", 4)

# If we want to insert "Deshmukh" in the three index value:
values.insert(3, "Deshmukh")
print(values)                    # [1, 2, 'Pooja', 'Deshmukh', 4, 5]

# Append : Append used to add new variable at the end
values.append("End")
print(values)                    # [1, 2, 'Pooja', 'Deshmukh', 4, 5, 'End']

# Update: If we want the update value which is present on the list
values[2] = "pooja"
print(values)                    # [1, 2, 'pooja', 'Deshmukh', 4, 5, 'End']

# Delete: Delete the variable using index value
del values[1]
print(values)                     # [1, 'pooja', 'Deshmukh', 4, 5, 'End']

# split:
name = "My name is pooja"

x = name.split("is ")

print(x)

print("*************************************************")

# 4)Tuple: In tuple we used round bracket().
#          Same as LIST data type but immutable (means we cannot change anything once created).

values = (1, 2, "Pooja", 4, 5)
print(values[0])

print("*************************************************")

# 5) Dictionary:

# syntax: dic = {kay: value}
# 1.If we used string in any arguments then use " "
# 2.We used curly brackets.

dic = {2 : "Hello",6: "777", "a" : "Hello world" }
print(dic[6])
print(dic["a"])

# null

# How to Create Dictionaries at run time and add data into it
dict={}

dict["first name"] = "Pooja"
dict["last name"] = "Deshmukh"
dict["gander"] = "famele"

print(dict)
print(dict["last name"])



