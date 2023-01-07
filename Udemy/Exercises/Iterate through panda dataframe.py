import pandas as pd

student_dict = {
    "names": ["Angela", "James", "Lilly"],
    "scores": [52, 85, 49]
}

student_dataframe = pd.DataFrame(student_dict)

for (key, value) in student_dataframe.iterrows():
    if value.scores > 50:
        print(value)
