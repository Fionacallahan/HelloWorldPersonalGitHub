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




