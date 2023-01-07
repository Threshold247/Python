from random import randint

names = ["Alex", "Beth", "Caroline", "Eleanor", "Dave", "Freddie"]

students_score = {student: randint(1, 99) for student in names}
print(students_score)

students_passed = {key: value for (key, value) in students_score.items() if value > 60}
print(students_passed)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

result = {item: len(item) for item in sentence.split()}
print(result)

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
weather_f = {key: ((values*9/5) + 32) for (key, values) in weather_c.items()}
print(weather_f)