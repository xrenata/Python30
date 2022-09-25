  ### Get 
mylist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(type(mylist))
print(mylist[1])
print(mylist[-1])
print(mylist[2:5])
print(mylist[:4])
if "apple" in mylist:
  print("True")
  ### Add
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
  ### Extend
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
  ### Remove
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
