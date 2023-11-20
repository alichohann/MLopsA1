from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

# Load the MNIST dataset
mnist = fetch_openml("mnist_784")
X, y = mnist["data"], mnist["target"]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
  X, y, test_size=0.2, random_state=42
)

model = LogisticRegression(max_iter=100)
model.fit(X_train, y_train)

# Evaluate the model
accuracy = model.score(X_test, y_test)
print("Test accuracy: {:.2f}%".format(accuracy * 100))

# Save the trained model to a pickle file
joblib.dump(model, "mnist_model.pkl")
