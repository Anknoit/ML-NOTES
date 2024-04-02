thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

#This will return the items from position 2 to 5.

#Remember that the first item is position 0,
#and note that the item in position 5 is NOT included

print(thislist[:4]) #from first to 4th array

print(thislist[2:]) #from 2nd array to last array

thislist[2] = "Ankit" #cherry is now Ankit

print(thislist[2])
if "kiwi" in thislist:
    print("Yes, kiwi is in the list")
    
print(len(thislist))

thislist.append("lemon")    #will add lemon to the list in the END
print(thislist)

thislist.insert(3, "pattharchatta") #will add object at specific array location
print(thislist)

#REMOVING SHITS FROM LIST
thislist.remove("orange")   #removes a specified obj
print(thislist)

thislist.pop(4)             #removes a specified obj by array
print(thislist)             #if no array then it will remove last obj



"""
Method	    Description
-----------------------------------------------------
append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()  	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position   
            list.insert(pos, elmnt)
pop()   	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()   	Sorts the list
            list.sort(reverse=True|False, key=myFunc)
            Parameter	Description
            reverse	Optional. reverse=True will sort the list descending. Default is reverse=False
            key	Optional. A function to specify the sorting criteria(s)
"""
_runnerup = [3,6,3,7,8,4,2,5]
_runnerup.sort()
_runnerup.append(17)
_runnerup.pop(2)                #Remove using element array position
_runnerup.remove(8)             #Remove using the element itself.....Numeric value without ""
_findpos = _runnerup.index(4)   #Find the position of specific element....string,number, list etc.
_runnerup.insert(3,"Waah Bhaiya") #Insert element in specific position
print("\nPosition of element:",_findpos)
print("\n",_runnerup)

"""
TUPLE
"""
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
