# data structures and algorithem
#primitive(int,float,boolean,str)&nonpremitive(linear , nonlinear)
#linear(list,tuple,set,dictionary)&nonlinear(linkedlist,tree,graphs)
#list - 2ways to create/list is the collection of dissimilar elements-list("dev","test","production",true,3.5)
        #array is the collection of similar elements-list("dev","test","production")
list_of_items = list()#1
list_of_cloudserver = list(["aws","gcp","azure"])#1
print (type(list_of_items))
list_of_item1 = []#2 list is identified also by squeare brackets
list_of_envroinment = ["dev","test","production","staging","qa"]#2
print (type(list_of_item1))
for a in list_of_envroinment:
    print(a)
print (list_of_cloudserver[0])# we can user range functionality to show specific
print (list_of_cloudserver[2])

for a in list_of_envroinment:
    print("deploying to:")
    print(a)


print(dir(list))#dir help in learning python from python
print (list.insert.__doc__)# will show how insert works can replace insert with others
print (list.append.__doc__)
list_of_envroinment.insert(1,"git")# print(list_of_envroinment.insert(0,"aaa"))wont work will show none
list_of_envroinment.append("git")
print(list_of_envroinment)


