# Creating a Set 
set1 = set([1, 2, 3, 4, 5, 6,  
            7, 8, 9, 10]) 
print("Intial Set: ") 
print(set1) 
  
# Removing elements from Set 
# using Remove() method 
set1.remove(5) 
print("\nSet after Removal of 5: ") 
print(set1) 
  
# Removing elements from Set 
# using Discard() method 
set1.discard(8) 
print("\nSet after Discarding 8: ") 
print(set1) 
  
# Removing elements from Set 
# using iterator method 
for i in range(1, 5): 
    set1.remove(i) 
print("\nSet after Removing a range of elements: ") 
print(set1) 
