from random import randint

names = ["Alex", "Beth", "Caroline", "Eleanor", "Dave", "Freddie"]

# creates a dictionary which consists of student name (key) and a random score (value)
students_score = {student: randint(1, 99) for student in names}
print(students_score)

# creates a dictionary which consists of student name and score where score is higher than 60
students_passed = {key: value for (key, value) in students_score.items() if value > 60}
print(students_passed)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# creates a dictionary that splits a sentence into words(key) and counts the letter for each word (value)
result = {item: len(item) for item in sentence.split()}
print(f"Split sentence with count: {result}")

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

# (temp_c * 9/5) + 32 = temp_f
# creates a dictionary which consists of the day (key) and converted temperature (value)
weather_f = {key: ((values*9/5) + 32) for (key, values) in weather_c.items()}
print(f"Converted weather {weather_f}")
