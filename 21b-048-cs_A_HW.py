# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1uwsqZbHf8pa0NIoKMLaHb-gxijgWyspd
"""

df = pd.read_excel('/content/Job_Scheduling.xlsx')
# Fill missing values in 'Arrival Time' with the mean
df['Arrival Time'].fillna(df['Arrival Time'].mean(), inplace=True)
df.dropna(inplace=True)
# Label the data based on a hypothetical criteria (e.g., Arrival Time <= 0.8 as successful)
df['Outcome'] = (df['Arrival Time'] <= 0.8).astype(int)

# Define features and target variable
X = df[['Burst time', 'Arrival Time', 'Preemptive', 'Resources']]
y = df['Outcome']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Naïve Bayes Classifier
nb_classifier = GaussianNB()
nb_classifier.fit(X_train, y_train)

# Predictions
y_pred = nb_classifier.predict(X_test)

# Evaluate the performance
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

"""# New section"""

pip install ucimlrepo

from ucimlrepo import fetch_ucirepo

# fetch dataset
dermatology = fetch_ucirepo(id=33)

# data (as pandas dataframes)
X = dermatology.data.features
y = dermatology.data.targets

# metadata
print(dermatology.metadata)

# variable information
print(dermatology.variables)

import pandas as pd
Xframe=pd.DataFrame(X)
Yframe=pd.DataFrame(y)



import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score

# Load the dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/dermatology/dermatology.data"
columns = ["erythema", "scaling", "definite borders", "itching", "koebner phenomenon",
           "polygonal papules", "follicular papules", "oral mucosal involvement",
           "knee and elbow involvement", "scalp involvement", "family history",
           "melanin incontinence", "eosinophils in the infiltrate", "PNL infiltrate",
           "fibrosis of the papillary dermis", "exocytosis", "acanthosis",
           "hyperkeratosis", "parakeratosis", "clubbing of the rete ridges",
           "elongation of the rete ridges", "thinning of the suprapapillary epidermis",
           "spongiform pustule", "munro microabcess", "focal hypergranulosis",
           "disappearance of the granular layer", "vacuolisation and damage of basal layer",
           "spongiosis", "saw-tooth appearance of retes", "follicular horn plug",
           "perifollicular parakeratosis", "inflammatory monoluclear inflitrate",
           "band-like infiltrate", "Age", "Class"]
data = pd.read_csv(url, names=columns, na_values="?")
data.dropna(inplace=True)

# Convert class labels to integers
data["Class"] = data["Class"].astype(int)

# Separate features (X) and target variable (y)
X = data.drop("Class", axis=1)
y = data["Class"]

# Split the data into training and testing sets with varying splits
splits = [(0.6, 0.4), (0.7, 0.3), (0.8, 0.2)]

for train_size, test_size in splits:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size)

    # Initialize and train the Naïve Bayes classifier
    classifier = GaussianNB()
    classifier.fit(X_train, y_train)

    # Predict the target variable
    y_pred = classifier.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy with train/test split {train_size}/{test_size}: {accuracy}")

    # Display confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    print(f"Confusion Matrix with train/test split {train_size}/{test_size}:")
    print(cm)



import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score

# Load the dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00267/data_banknote_authentication.txt"
columns = ["variance", "skewness", "curtosis", "entropy", "class"]
data = pd.read_csv(url, names=columns)

# Separate features (X) and target variable (y)
X = data.drop("class", axis=1)
y = data["class"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)

# Initialize and train the KNN classifier
knn_classifier = KNeighborsClassifier()
knn_classifier.fit(X_train, y_train)

# Initialize and train the Naïve Bayes Classifier
nb_classifier = GaussianNB()
nb_classifier.fit(X_train, y_train)

# Predictions
knn_pred = knn_classifier.predict(X_test)
nb_pred = nb_classifier.predict(X_test)

# Evaluation
knn_accuracy = accuracy_score(y_test, knn_pred)
nb_accuracy = accuracy_score(y_test, nb_pred)

print("K-Nearest Neighbors Classifier Accuracy:", knn_accuracy)
print("Naïve Bayes Classifier Accuracy:", nb_accuracy)

# Confusion matrices
knn_cm = confusion_matrix(y_test, knn_pred)
nb_cm = confusion_matrix(y_test, nb_pred)

print("\nConfusion Matrix for K-Nearest Neighbors Classifier:")
print(knn_cm)
print("\nConfusion Matrix for Naïve Bayes Classifier:")
print(nb_cm)

from sklearn.datasets import load_wine, load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, f1_score
import pandas as pd

# Function to evaluate classifiers for a dataset
def evaluate_dataset(X, y, dataset_name):
    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train Naïve Bayes classifier
    nb_classifier = GaussianNB()
    nb_classifier.fit(X_train, y_train)

    # Initialize and train KNN classifier
    knn_classifier = KNeighborsClassifier()
    knn_classifier.fit(X_train, y_train)

    # Predictions
    nb_pred = nb_classifier.predict(X_test)
    knn_pred = knn_classifier.predict(X_test)

    # Calculate accuracy and F1-score for Naïve Bayes classifier
    nb_accuracy = accuracy_score(y_test, nb_pred)
    nb_f1 = f1_score(y_test, nb_pred, average='weighted')

    # Calculate accuracy and F1-score for KNN classifier
    knn_accuracy = accuracy_score(y_test, knn_pred)
    knn_f1 = f1_score(y_test, knn_pred, average='weighted')

    # Print results
    print(f"Results for {dataset_name} Dataset:")
    print("Naïve Bayes Classifier:")
    print(f"  Accuracy: {nb_accuracy:.4f}")
    print(f"  F1-Score: {nb_f1:.4f}")
    print("K-Nearest Neighbors (KNN) Classifier:")
    print(f"  Accuracy: {knn_accuracy:.4f}")
    print(f"  F1-Score: {knn_f1:.4f}")
    print()

# Load the Wine dataset
wine_data = load_wine()
X_wine = wine_data.data
y_wine = wine_data.target

# Evaluate classifiers for the Wine dataset
evaluate_dataset(X_wine, y_wine, "Wine")