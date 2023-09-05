list_of_envroinment = ["dev","test","production","staging","qa"]
key = "test"

for i in list_of_envroinment:
    if i == key:
        print("found")

# advanceed

    list_of_envroinment = ["dev","test","production","staging","qa"]
    key = "test" # change spelling of test to testing to see changes in in line 19 if statement


    is_found = False
    for i in list_of_envroinment:
        if i == key:
            is_found = True
        if is_found:
            print("found")
        else:
            print("not found")
        


#linearsearch as function for function.py

#list_of_envroinment = ["dev","test","production","staging","qa"]
#key = "test" # change spelling of test to testing to see changes in in line 19 if statement

def leanearsearch_function(list_of_envroinment,key):
    is_found = False
    for i in list_of_envroinment:
        if i == key:
            is_found = True
        if is_found:
            print("found")
        else:
            print("not found")
        
list_of_envroinment = ["dev","test","production","staging","qa"]
key = "test"
leanearsearch_function(list_of_envroinment,key)
    


    