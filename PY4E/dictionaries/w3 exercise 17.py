# Write a Python program to remove duplicates from Dictionary


student_data = {'id1':
                {'name': ['Sara'],
                 'class': ['V'],
                    'subject_integration': ['english, math, science']
                 },
                'id2':
                {'name': ['David'],
                    'class': ['V'],
                    'subject_integration': ['english, math, science']
                 },
                'id3':
                {'name': ['Sara'],
                    'class': ['V'],
                    'subject_integration': ['english, math, science']
                 },
                'id4':
                {'name': ['Surya'],
                    'class': ['V'],
                    'subject_integration': ['english, math, science']
                 },
                }
mydict = {}

for key, value in student_data.items():
    if value not in mydict.values(): #if the key, value pair is not in the dictionary, add it
        mydict[key] = value
print(mydict)
