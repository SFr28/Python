ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#List: List items are ordered, changeable, and allow duplicate values
ft_list[1] = "World!"

#Tuple: Tuple items are ordered, unchangeable, and allow duplicate values.
tmp = list(ft_tuple)
tmp[1] = "France!"
ft_tuple = tuple(tmp)

#Set: Set items are unordered, unchangeable, and do not allow duplicate values
#Contrary to tuple, we can still add and remove items in a set
ft_set.remove("tutu!")
ft_set.add("Paris!")

#Dictionary: Dictionary items are ordered, changeable, and do not allow duplicates
#Dictionary items are presented in key:value pairs, and can be referred to by using the key name
ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)