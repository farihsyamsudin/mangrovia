# -*- coding: utf-8 -*-
"""Mangrovia.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13L6QhCBpLKvqDdUMN0IcuCQ1gLPFJhJJ

TES AI DECISION TREE MANGROVIA
"""

import pandas as pd

df = pd.read_csv('../../Raw Data/data.csv')

from sklearn.tree import DecisionTreeClassifier, export_text
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from joblib import dump

X = df[['sst', 'salinity', 'substrat']]
y = df['output_mangrove']

# One-hot encode categorical variable 'substrat'
ct = ColumnTransformer(
    transformers=[('encoder', OneHotEncoder(), ['substrat'])],
    remainder='passthrough'
)
X = pd.DataFrame(ct.fit_transform(X), columns=ct.get_feature_names_out())

# Bagi data menjadi data latih dan data uji
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Membuat model Decision Tree
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Tampilkan struktur pohon keputusan
tree_rules = export_text(model, feature_names=list(X.columns))
print("Decision Tree Rules:\n", tree_rules)

# Visualisasi pohon keputusan
plt.figure(figsize=(12, 8))
plot_tree(model, feature_names=list(X.columns), class_names=model.classes_, filled=True, rounded=True)
plt.show()

accuracy = model.score(X_test, y_test)
print(f'Accuracy: {accuracy * 100:.2f}%')

# Input data baru untuk diprediksi
new_data = {'sst': 27, 'salinity': 28, 'substrat': 'lumpur'}

# Ubah data input menjadi DataFrame
new_data_df = pd.DataFrame([new_data])

# One-hot encode categorical variable 'substrat'
new_data_encoded = pd.DataFrame(ct.transform(new_data_df), columns=ct.get_feature_names_out())

# Lakukan prediksi menggunakan model
prediction = model.predict(new_data_encoded)

print(f'Predicted Mangrove Type: {prediction[0]}')

dump([model, ct], 'modelMangrovia.sav')