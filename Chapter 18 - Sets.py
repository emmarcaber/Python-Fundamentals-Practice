# CHAPTER 18
# set = collection which is underored, undindexed. 
#       No duplicate values

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

# utensils.add("napkin") # adds "napkin" to utensils set
# utensils.remove("fork") # removes "fork" from utensils set
# utensils.clear() # removes all the elements inside the utensils set
# utensils.update(dishes) # concatenates dishes set to utensils set
# dinner_table = utensils.union(dishes) # shows the union of the sets

# shows the the difference between the sets utensils and dishes
print(dishes.difference(utensils))

# shows the similarities and intersections between the sets
# utensils and dishes
print(dishes.intersection(utensils))

# for x in dinner_table:
#     print(x)