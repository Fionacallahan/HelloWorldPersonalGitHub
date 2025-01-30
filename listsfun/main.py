#a list is a sequence of items 
#can be oneD or twoD
#1D: single row or column 
#declare a list using [ ] and a comma separated list of values 
#            0 1  2  3
#           -4 -3 -2 -1
list_ints = [0,1,10,20]
#there are unique indexes for each element in the list 
#0-based, last element is at n - 1
print(list_ints[0])
print(list_ints[-4])

#types can be mixed in a list 
list_numbers = [0,0.0, 1, 1.0]
print(list_numbers) 
print(type(list_numbers))
#lists are mutable(they can be changed)
list_numbers[0] = "hello"
print(list_numbers)

#use len() to find out length of list 
print(len(list_numbers)) #use for indexing 
list_numbers.append("another element")
#can use len - 1 for last element 
print(list_numbers[len(list_numbers) - 1])

#empty lists 
empty_list = []
print(len(empty_list))

#we can have lists of lists 
nested_list = [[0,1], [2], [], [4,5]]
#length: 4
print(len(nested_list[0]))
#length: 2

#iterating through lists 
candies = ["twix", "reeses", "oreos", "snickers"]

for candy in candies: #more efficient 
    print(candy)

#while loop 
i = 0
while i < len(candies):
    print(i, candies[i])
    i += 1

#for loop and a range 
i = 0
for i in range(len(candies)):
    print(i, candies[i])

#common list operators 
#list concatenation 
print(candies)
candies += ["m&ms", "starburst"]
print(candies)
#list repetition 
bag_o_candies = 5 * ["twix", "snickers"] #do a lot of twix and snickers 
print(bag_o_candies)

# list slicing 
#grabs sublists of lists 
print(candies[1:3])
#slice operator :
#starting index: inclusive while second index is exclusive 
#if you ever need copy of a list, just use slice operator like this [:]
copy_of_candies = candies[:] #SHALLOW COPY 
copy_of_candies[0] = "TWIX" #does not change original candies 
print(copy_of_candies)

#list methods 
candies.remove("twix")
print(candies)
#LOTS of list methods 

#will go through more of lists in next few classes 

#continuing in class 
food = ["chips", "fish"]
food.append("pizza")
print(food)

#extend (for appending items in another list)
food.extend(["cheese", "crackers"]) #adds all the items in a list as singular items 
print(food)

# += list concatenate and assign 
food+= candies
print(food)

#pop(index) for position based removal 
item = food.pop(1)
print(item, food)


#lists and strings 
#creating a string from a list of strings 
#using the string join method 
list_of_strings = ["co", "m", "pute", "r"]
word = "".join(list_of_strings) #can join strings with anything 
print(word)

#how to make a list from a string 
list_of_strings2 = list(word)
print(list_of_strings2)

#split is a string method 
#from CSV files: used in excel 
comma_separated_word = "co,m,pute,r" 
list_strings3 = comma_separated_word.split(",")
print(list_of_strings)
#able to deconstruct original string 

def add_one_to_each_element(nums_list):
    for i in range(len(nums_list)):
        nums_list[i] = nums_list[i] + 1
    print(nums_list)
test_list = [0,5,10,15,20,25]
add_one_to_each_element(test_list)


#LIST ALIASING 
list1 = [1,2,3,4]
list2 = [1,2,3,4]
#list 2 is a different list object than list 1 (though they have the saem values)
list1[0] = 10
print[list1, list2] 

list3 = list1
list1[0] = 100
#changes list1 AND list3 
#list3 is an "alias" for the same object that list1 refers to (they are the same object in memory )
print(list1, list2, list3)

add_one_to_each_element(list1) #nums_list will be an alias for list1's object
#makes a change to list1 AND list3 
print("after call:", list1, list2, list3)

#to make a copy of a 1D list: use the list copy() method 
list4 = list1.copy() #SHALLOW copy: only goes one layer deep (does not work with 2D)
list[0] = 10000
print(list1, list2, list3, list4)
#python is pass by object reference 
#   functions with a reference to an object passed in can modify the object 
#   big picture 

#a few more words about strings 
#strings are immutable 
#they support 0-based indexing and slicing 
# they have methods, like split() and join()
# strip()
word = "   \t   \n\n  basketball\n    \n"
print(word)
print(repr(word))
word = word.strip()
print(repr(word))
#find()
print(word.find("et")) #returns index of where the string starts 
print(word.find("t"))
print(word.find("z")) #returns -1

