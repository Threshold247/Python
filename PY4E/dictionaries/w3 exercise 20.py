# Write a Python program to print all unique values in a dictionary.
# Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}

sampleData = {"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {
    "VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}
myKeys = set(key for dic in sampleData for key in dic.keys()) #checks for unique keys in data set
myValues = set(val for dic in sampleData for val in dic.values()) #checks for unique values in data set
myItems = sorted(set((key, values)
                     for dic in sampleData for (key, values) in dic.items()))
print(myKeys)
print(myValues)
print(myItems)
