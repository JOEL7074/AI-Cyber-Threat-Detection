# 🛡️ Sentinel AI

## AI-Powered Cyber Threat Detection and Response System

Sentinel AI is a machine-learning-based cybersecurity prototype designed to detect potentially malicious network traffic.

The system analyzes network-flow data, uses a trained **Random Forest Classifier** to classify network traffic, visualizes detected threats, analyzes individual network flows, and provides simulated defensive response recommendations.

> **Project Type:** AI + Data Science + Cybersecurity
> **Programming Language:** Python
> **Machine Learning:** Random Forest
> **Application:** Streamlit
> **Dataset:** CICIDS2017

---

# 📌 1. Project Overview

Modern computer networks generate huge amounts of network traffic.

Manually analyzing every network connection can be difficult and time-consuming.

Sentinel AI demonstrates how **Artificial Intelligence and Machine Learning** can assist cybersecurity monitoring by automatically analyzing network-flow features and identifying suspicious traffic.

The system currently focuses on:

* BENIGN network traffic
* DDoS network traffic

The project is designed as a **defensive cybersecurity prototype** and does not perform real-world attack actions or automatically modify firewall configurations.

---

# 🎯 2. Project Objective

The main objective of Sentinel AI is to develop an AI-based system capable of:

1. Processing network traffic data
2. Cleaning and preparing the dataset
3. Extracting network-flow features
4. Classifying network traffic using Machine Learning
5. Detecting potentially malicious traffic
6. Visualizing security statistics
7. Analyzing individual network flows
8. Recommending defensive responses
9. Generating downloadable security reports

---

# ⚠️ 3. Problem Statement

Traditional network monitoring can require security analysts to examine large amounts of network traffic.

This creates several challenges:

* Large volumes of network data
* Difficult manual inspection
* Time-consuming threat identification
* Difficulty identifying unusual traffic patterns
* Need for automated security monitoring

Sentinel AI addresses this problem by using a machine-learning model to automatically classify network traffic.

---

# 💡 4. Proposed Solution

Sentinel AI follows the following pipeline:

```text
Network Traffic Dataset
          ↓
Data Cleaning
          ↓
Feature Processing
          ↓
Random Forest Model
          ↓
Threat Classification
          ↓
Threat Analysis
          ↓
Response Recommendation
          ↓
Security Report
```

The system receives network-flow data in CSV format and passes the numerical features to the trained machine-learning model.

The model then predicts whether the traffic is:

```text
BENIGN
```

or

```text
DDoS
```

The prediction results are then displayed through an interactive Streamlit dashboard.

---

# 🏗️ 5. System Architecture

```text
                    CICIDS2017 Dataset
                           │
                           ▼
                  Data Preprocessing
                           │
                           ▼
                   Feature Processing
                           │
                           ▼
                 Random Forest Model
                           │
                           ▼
                  Network Prediction
                           │
                  ┌────────┴────────┐
                  │                 │
                  ▼                 ▼
               BENIGN             DDoS
                  │                 │
                  │                 ▼
                  │          Threat Analysis
                  │                 │
                  │                 ▼
                  │       Response Recommendation
                  │                 │
                  └────────┬────────┘
                           ▼
                    Security Report
```

---

# 🧠 6. Machine Learning Model

Sentinel AI uses a:

## Random Forest Classifier

Random Forest is a supervised machine-learning algorithm used for classification and regression problems.

Instead of relying on a single decision tree, Random Forest creates multiple decision trees.

Each tree makes a prediction and the results are combined to produce the final classification.

Simplified:

```text
                 Network Features
                        │
          ┌─────────────┼─────────────┐
          ▼             ▼             ▼
       Tree 1        Tree 2        Tree 3
          │             │             │
          ▼             ▼             ▼
       BENIGN         DDoS          DDoS
          └─────────────┬─────────────┘
                        ▼
                 Final Prediction
                      DDoS
```

This makes Random Forest suitable for classification problems involving many numerical features.

---

# 📊 7. Dataset

The project uses network-flow data from the:

## CICIDS2017 Dataset

The current model was trained using a dataset containing:

* BENIGN traffic
* DDoS traffic

The selected dataset contains:

```text
Rows:    225,745
Columns: 79
```

After separating the target column:

```text
Input Features: 78
Target:         Label
```

The dataset was divided into:

```text
80% → Training Data
20% → Testing Data
```

The training/testing split was performed using stratification so that the class distribution was preserved.

---

# 🧹 8. Data Preprocessing

Before training the model, the network traffic data is cleaned.

The project handles:

### Missing values

Missing numerical values are replaced with:

```text
0
```

### Infinite values

Positive and negative infinity values are converted into missing values and then handled.

The preprocessing code includes:

```python
X = X.replace(
    [float("inf"), float("-inf")],
    float("nan")
)

X = X.fillna(0)
```

This prevents invalid numerical values from causing problems during model training.

---

# 🤖 9. Model Training

The Random Forest model was configured with:

```python
RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)
```

### Parameters

| Parameter           |         Value |
| ------------------- | ------------: |
| Algorithm           | Random Forest |
| Number of Trees     |           100 |
| Random State        |            42 |
| Parallel Processing |       Enabled |

The trained model is saved using Joblib:

```text
threat_detection_model.pkl
```

This allows the Streamlit application to load the trained model without retraining it every time.

---

# 📈 10. Model Results

The model achieved approximately:

```text
99.9956%
```

accuracy on the selected test split.

The confusion matrix was:

```text
[[19543     1]
 [    1 25604]]
```

The classification report showed approximately 1.00 precision, recall, and F1-score for both classes on this test split.

### Important Note

This result represents performance on the selected CICIDS2017 test split.

It should **not** be interpreted as guaranteed real-world cybersecurity accuracy.

Real-world performance can vary because network environments, traffic patterns, attack techniques, and datasets can differ significantly.

---

# 🖥️ 11. Application Features

Sentinel AI provides several interactive modules.

## 🏠 Dashboard

Displays:

* AI model status
* Model information
* Detection type
* System workflow
* System capabilities

---

## 📚 Project Info

Provides:

* Project objective
* Problem statement
* Proposed solution
* Technologies
* Dataset information
* ML model explanation
* System architecture
* Advantages
* Limitations
* Future enhancements

---

## 🚨 Threat Detection

Allows users to:

1. Upload a network traffic CSV
2. Validate required features
3. Clean the data
4. Run AI predictions
5. Store the analysis results

---

## 🌐 Network Analysis

Displays:

* Total network flows
* Safe flows
* Detected threats
* Threat percentage
* Threat distribution
* Threat type comparison
* Recent detected threats
* Network data preview

---

## 🔍 Flow Analyzer

Allows users to select an individual network flow and view:

* Flow information
* AI prediction
* Prediction confidence
* Class probabilities

---

## 🛡️ Threat Response

Analyzes detected threats and generates a simulated response.

Threat levels include:

```text
SAFE
LOW
MEDIUM
HIGH
CRITICAL
```

The system can recommend actions such as:

* Increased monitoring
* Security alerts
* Log preservation
* Investigation
* Network isolation recommendations

The response is only a **simulation**.

---

## 📥 Security Report

The system generates a prediction report that can be downloaded as:

```text
sentinel_ai_security_report.csv
```

---

## 📊 Feature Importance

Displays the most important network-flow features used by the Random Forest model.

The feature-importance visualization helps explain which features contributed most strongly to the model's decisions.

> Feature importance does not mean that a particular feature directly causes a cyberattack.

---

## 🧠 AI Model

Displays technical information about:

* Random Forest
* Number of trees
* Number of input features
* Model workflow
* Technologies
* Model limitations

---

# 🛠️ 12. Technologies Used

## Programming

* Python

## Data Processing

* Pandas
* NumPy

## Machine Learning

* Scikit-learn
* Random Forest

## Visualization

* Plotly

## Web Application

* Streamlit

## Model Storage

* Joblib

---

# 📁 13. Project Structure

```text
AI-Cyber-Threat-Detection/
│
├── app.py
│
├── train_model.py
│
├── threat_detection_model.pkl
│
├── README.md
│
└── data/
    │
    └── Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv
```

### File Description

| File                         | Purpose                       |
| ---------------------------- | ----------------------------- |
| `app.py`                     | Streamlit web application     |
| `train_model.py`             | Model training and evaluation |
| `threat_detection_model.pkl` | Saved Random Forest model     |
| `README.md`                  | Project documentation         |
| `data/`                      | Dataset directory             |

---

# ⚙️ 14. Installation

Make sure Python is installed.

Then install the required libraries:

```bash
pip install pandas numpy scikit-learn streamlit plotly joblib
```

---

# ▶️ 15. How to Run

Open the project folder in VS Code.

Run:

```bash
python -m streamlit run app.py
```

Streamlit will start the application locally.

The application will normally be available at:

```text
http://localhost:8501
```

---

# 🧪 16. How to Use

### Step 1

Start Sentinel AI:

```bash
python -m streamlit run app.py
```

### Step 2

Open:

```text
🚨 Threat Detection
```

### Step 3

Upload a compatible network-flow CSV file.

### Step 4

Click:

```text
🔍 Analyze Network Traffic
```

### Step 5

Open:

```text
🌐 Network Analysis
```

to view the results.

### Step 6

Use:

```text
🔍 Flow Analyzer
```

to inspect individual flows.

### Step 7

Use:

```text
🛡️ Threat Response
```

to view defensive recommendations.

### Step 8

Use:

```text
📥 Security Report
```

to download the analysis.

---

# 🔐 17. Cybersecurity Scope

Sentinel AI is designed as a **defensive cybersecurity project**.

The current system:

* Analyzes network-flow datasets
* Detects potentially malicious traffic
* Classifies traffic using Machine Learning
* Generates security alerts
* Recommends defensive actions

The current prototype does **not**:

* Launch cyberattacks
* Exploit systems
* Perform unauthorized network access
* Automatically modify firewall configurations
* Automatically block real devices
* Capture real network traffic

The threat-response functionality is simulated for demonstration purposes.

---

# ⚠️ 18. Current Limitations

The current prototype has several limitations.

### 1. Dataset-Based Detection

The system currently analyzes CSV network-flow data rather than continuously monitoring live network traffic.

### 2. Limited Attack Categories

The current model focuses on the classes available in the selected training dataset.

### 3. Dataset Dependency

Machine-learning performance depends on the quality and characteristics of the training data.

### 4. Real-World Generalization

Performance on one dataset does not guarantee the same performance in another network environment.

### 5. Simulated Response

The current response engine provides recommendations and demonstrations rather than modifying real network infrastructure.

---

# 🚀 19. Future Enhancements

Possible future improvements include:

## Phase 1 — Live Network Monitoring

Integrate a controlled network-monitoring pipeline.

## Phase 2 — Additional Attack Classes

Extend the training data to include additional intrusion categories.

## Phase 3 — Model Comparison

Compare multiple machine-learning algorithms.

Possible models include:

* Logistic Regression
* Decision Tree
* Random Forest
* Gradient Boosting
* Support Vector Machine

## Phase 4 — Real-Time Alerting

Add controlled notifications when suspicious traffic is detected.

## Phase 5 — Advanced Security Dashboard

Add:

* Real-time traffic charts
* Historical threat statistics
* Alert management
* Security event timelines

## Phase 6 — Advanced AI

Experiment with advanced machine-learning and deep-learning techniques after establishing a strong baseline.

---

# 🎓 20. Academic Significance

This project combines multiple areas of Artificial Intelligence and Data Science:

```text
Python
   +
Data Processing
   +
Machine Learning
   +
Data Visualization
   +
Cybersecurity
   +
Web Application Development
```

It demonstrates a complete machine-learning workflow:

```text
Dataset
   ↓
Preprocessing
   ↓
Training
   ↓
Testing
   ↓
Evaluation
   ↓
Prediction
   ↓
Visualization
   ↓
Application
```

---

# 🎤 21. Simple Project Explanation

If an evaluator asks:

### "Explain your project."

You can say:

> Sentinel AI is an AI-powered cyber threat detection and response system. It uses network-flow data from the CICIDS2017 dataset and applies data preprocessing before passing the network features to a Random Forest classifier. The model classifies network traffic as benign or potentially malicious, particularly DDoS traffic in the current implementation. The predictions are displayed through a Streamlit dashboard where we can analyze network traffic, inspect individual flows, view feature importance, and generate simulated defensive response recommendations. The project demonstrates how machine learning can assist automated cybersecurity monitoring.

---

# 🧠 22. One-Line Explanation

If the evaluator asks:

### "What does your project do?"

Answer:

> **Sentinel AI uses Machine Learning to analyze network traffic and identify potentially malicious network activity.**

---

# 📌 23. Key Project Keywords

Important terms to understand before the project presentation:

```text
Artificial Intelligence
Machine Learning
Cybersecurity
Network Intrusion Detection
CICIDS2017
Network Flow
Data Preprocessing
Feature Engineering
Random Forest
Decision Tree
Classification
Training Data
Testing Data
Accuracy
Precision
Recall
F1 Score
Confusion Matrix
Feature Importance
Streamlit
Python
Pandas
NumPy
Scikit-learn
Plotly
Joblib
```

---

# 👨‍💻 24. Author

**Sentinel AI**

AI & Data Science Final-Year Project

---

# 📜 25. Disclaimer

This project is an academic cybersecurity prototype intended for defensive security research and educational demonstration.

The reported machine-learning results are specific to the selected dataset and test methodology and should not be interpreted as guaranteed performance in real-world networks.
