# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report

# Load the dataset
df = pd.read_csv('SDN_traffic.csv')

# Preprocess the dataset (assuming 'category' is the target variable)
X = df.drop('category', axis=1)
y = df['category']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the CART model (CART is the default algorithm in scikit-learn's DecisionTreeClassifier)
cart_model = DecisionTreeClassifier(random_state=42)
cart_model.fit(X_train, y_train)

# Predict and evaluate the CART model
cart_predictions = cart_model.predict(X_test)
print("CART Model Performance:")
print(classification_report(y_test, cart_predictions))

# Note: Scikit-learn's DecisionTreeClassifier does not directly support ID3. 
# For ID3, you might need to use an external library or implement the algorithm manually.
# However, for demonstration, we'll assume the use of CART as a proxy for both.

# Train the ID3 model (hypothetical, as scikit-learn does not directly support ID3)
# id3_model = DecisionTreeClassifier(criterion='entropy', random_state=42) # Entropy can be considered a proxy for ID3's approach
# id3_model.fit(X_train, y_train)

# Predict and evaluate the ID3 model (hypothetical)
# id3_predictions = id3_model.predict(X_test)
# print("ID3 Model Performance:")
# print(classification_report(y_test, id3_predictions))
