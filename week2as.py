#create an empty list called "my_list"
my_list=[]
#append 10, 20, 30, 40 to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)
#insert 15 at second position
my_list.insert(1,15)
print(my_list)
#extend the list with another list [50,60,70]
another_list=[50,60,70]
my_list.extend(another_list)
print(my_list)
#remove the last element from the list
my_list.pop(-1)
print(my_list)
#sort the list in ascending order
my_list.sort()
print(my_list)
#print the index of 30 in the list
print(my_list.index(30))