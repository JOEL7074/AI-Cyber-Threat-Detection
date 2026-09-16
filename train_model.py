import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib

# 1. Load the dataset
file_path = "data/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv"

data = pd.read_csv(file_path)

# 2. Clean column names
data.columns = data.columns.str.strip()

print("Dataset loaded successfully!")
print("Rows:", len(data))
print("Columns:", len(data.columns))

# 3. Separate features and target
X = data.drop("Label", axis=1)
y = data["Label"]

# 4. Clean infinity and missing values
X = X.replace([float("inf"), float("-inf")], float("nan"))
X = X.fillna(0)

print("\nData cleaned successfully!")

# 5. Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\nTraining data:", X_train.shape)
print("Testing data:", X_test.shape)

# 6. Create AI model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

# 7. Train AI
print("\nTraining AI model...")

model.fit(X_train, y_train)

print("AI model trained successfully!")

# 8. Make predictions
print("\nTesting AI model...")

y_pred = model.predict(X_test)

# 9. Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\n==============================")
print("AI MODEL RESULTS")
print("==============================")

print("Accuracy:", accuracy)

# 10. Detailed report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# 11. Confusion matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# 12. Save the trained model
joblib.dump(model, "threat_detection_model.pkl")

print("\nModel saved successfully!")
print("File: threat_detection_model.pkl")