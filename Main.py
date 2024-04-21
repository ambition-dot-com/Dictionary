#Dictionary.
numbers = [1,2,3,4,5]
sample_dict = {
    "name":"summer",
    "age":13,
    "city":"chandigarh"
}
print(sample_dict)
print(sample_dict["name"])
print(sample_dict["city"])

#Getting the list of keys
print(sample_dict.keys())

#getting the list of values
print(sample_dict.values())

for key in sample_dict:
   print(key,sample_dict[key] ) 

#Check if a key exists in a dict
if "country" in sample_dict:
   print("country key exists")
else:
   print("Country key does not exist")

#Adding key value to a dict
sample_dict["country"] = "india"
print(sample_dict)
sample_dict["profession"] = "film director"
print(sample_dict)

#deleting a key value from a dict
del(sample_dict["city"])
print(sample_dict)

#changing value of a dict
sample_dict["profession"] = "detective"
print(sample_dict) 

#storing a list in a dict
sample_dict["marks"] = [20,30,40,50,60]
print(sample_dict)
print(sample_dict["marks"][1])