# dictonary will have key and value, they are denoted by {} this brackets
dictionary_of_items = {
    "env":" dev",
    "server":"aws linux2",
    "ram":8096,
    "cpu":4,
    "active":True,
}

dictionary_of_items2 = {
    "env":" production",
    "server":"aws linux2",
    "ram":2096,
    "cpu":6,
    "active":False,
}


#if dictionary_of_items .get("active"):
# or 
if dictionary_of_items["active"]: #like in list we write index numbr,here we give key
    print ("serverdetails")
    print ("environment: ",dictionary_of_items["env"])

#next step code
environment_details = [dictionary_of_items,dictionary_of_items2]

for a in environment_details:
    print(a)
    for b,c in a.items():
        print(b,c)
# or
for env in environment_details:
    print(env)
    for key,value in a.items():
        if key=="active" and value==True:
            
            print(env.values())

        