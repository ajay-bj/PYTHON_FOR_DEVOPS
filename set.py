set_of_num1 = {11,11,1,2,3,4,5,6,7,8,9,9,9,10,66,45}
print(set_of_num1) #set is similar to dictionary in -{}, it cannot tolatate  dublicate, shorts automaticsally
set_of_item = {None}# it will always have none in empty-{none}
set_of_num2 = {1,2,3,4,5,6,7,8}# the are like in maths set( 10th set like intersection etc)
print(set_of_num1.intersection(set_of_num2))
print(set_of_num1.union(set_of_num2))
# we can use property" of set to remove duplicates
list_of_env = ["staging","dev","test","test","staging", "production"]
list_of_env = list(set(list_of_env))
print(list_of_env)
