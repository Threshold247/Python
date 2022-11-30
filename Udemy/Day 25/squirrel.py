import pandas as pd

# reading the data from the csv file
squirrel_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# creating fur data variable with only fur color series
fur_data = squirrel_data["Primary Fur Color"]
# creating
gray_fur_data = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
red_fur_data = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_fur_data = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
print(gray_fur_data, red_fur_data, black_fur_data)

squirrel_fur_data = {
    "Fur Colour": ["Gray", "Red", "Black"],
    "Count": [gray_fur_data, red_fur_data, black_fur_data]
}

data = pd.DataFrame(squirrel_fur_data)
data.to_csv("Squirrel_Color_Data")
