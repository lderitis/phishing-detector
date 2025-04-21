import argparse
import joblib
from features import extract_features

# Load trained model
model = joblib.load("model.pkl")

# Set up CLI arguments
parser = argparse.ArgumentParser(description="Phishing URL Detector")
parser.add_argument("url", help="Enter a URL to classify")
args = parser.parse_args()

# Extract features from the input URL
features = extract_features(args.url)
x = [list(features.values())]

# Make prediction
result = model.predict(x)[0]

# Output result
if result == 1:
    print("⚠️  This URL is likely PHISHING.")
else:
    print("✅  This URL appears LEGITIMATE.")
