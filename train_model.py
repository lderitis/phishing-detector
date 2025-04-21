import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
from features import extract_features

# Load data
df = pd.read_csv("malicious_phish.csv")
df = df[df["type"].isin(["phishing", "benign"])]
X = pd.DataFrame([extract_features(url) for url in df["url"]])
y = df["type"].map({"benign": 0, "phishing": 1})

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
clf = RandomForestClassifier()
clf.fit(X_train, y_train)

# Save model
joblib.dump(clf, "model.pkl")

# Test model
accuracy = accuracy_score(y_test, clf.predict(X_test))
print(f"Model Accuracy: {accuracy:.2f}")
