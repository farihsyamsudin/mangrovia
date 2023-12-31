import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.model_selection import train_test_split
from joblib import dump

df = pd.read_csv('../../Raw Data/data.csv')
df.head(10)

X = df[['sst', 'salinity', 'tss']]
y = df['output_mangrove']

# Bagi data menjadi data latih dan data uji
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Membuat model Decision Tree
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Akurasi
accuracy = model.score(X_test, y_test)
print(f'Accuracy: {accuracy * 100:.2f}%')

# Tampilkan struktur pohon keputusan
tree_rules = export_text(model, feature_names=list(X.columns))
# print("Decision Tree Rules:\n", tree_rules)

# Visualisasi pohon keputusan
# plt.figure(figsize=(12, 8))
# plot_tree(model, feature_names=list(X.columns), class_names=model.classes_, filled=True, rounded=True)
# plt.show()

dump([model, tree_rules, accuracy], 'modelMangrovia.sav')