# Write a Python script to concatenate following dictionaries to create a new one. Go to the editor

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic4 = dict()

for dict in (dic1, dic2, dic3):
    print(dict)
    dic4.update(dict)
print(dic4)
