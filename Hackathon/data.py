import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("Hackathon\energy_noisy_train.csv")
df.head()
df.groupby(["Orientation"])
# def extract_figures(text, position=-3):
#     # text <- string to extract information from
#     # position <- integer that tells the position of number in string
#     listOfWords = text.split()
#     word = listOfWords[position]
#     return word


# def create_correlation_map(df):
#     plt.figure(figsize=(16, 6))
#     # Store heatmap object in a variable to easily access it when you want to include more features (such as title).
#     # Set the range of values to be displayed on the colormap from -1 to 1, and set the annotation to True to display the correlation values on the heatmap.
#     heatmap = sns.heatmap(df.corr(), vmin=-1, vmax=1, annot=True)
#     # Give a title to the heatmap. Pad defines the distance of the title from the top of the heatmap.
#     heatmap.set_title('Correlation Heatmap', fontdict={'fontsize': 12}, pad=12)


# def pretty_print_coefficients(model, columns):
#     # Function to display estimated coefficients in a more human-readable way

#     # coef -> np.array: estimated regression coefficients
#     # columns -> list of str: columns used for prediction

#     coefDf = pd.DataFrame({"Feature": columns, "Coefficients": model.coef_[0]})
#     coefDf.head(len(columns))
#     return coefDf
