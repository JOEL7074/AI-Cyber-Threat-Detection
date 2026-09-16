
# 🛡️ Sentinel AI — AI Cyber Threat Detection & Response System

An AI-powered cybersecurity application built with **Python, Machine Learning, and Streamlit** to analyze network traffic and identify potential cyber threats, with a focus on **DDoS attack detection**.

---

## 📌 Project Overview

**Sentinel AI** is a machine-learning-based Cyber Threat Detection and Response System designed to analyze network traffic data and classify network activity as either:

- ✅ **BENIGN** — Normal network traffic
- 🚨 **DDoS** — Potential Distributed Denial-of-Service traffic

The system uses a **Random Forest Machine Learning model** trained on network-flow data from the **CICIDS2017 dataset**.

A Streamlit dashboard provides an interactive interface for uploading network traffic data, detecting threats, analyzing network activity, and generating security reports.

---

## 🎯 Project Objective

The main objective of Sentinel AI is to demonstrate how Machine Learning can assist cybersecurity teams in:

1. Analyzing network traffic
2. Detecting suspicious traffic patterns
3. Classifying potential threats
4. Understanding important network features
5. Visualizing network activity
6. Generating security reports
7. Simulating defensive threat-response actions

---

## 🚨 Problem Statement

Traditional cybersecurity systems often depend heavily on predefined rules and signatures.

However, modern network environments generate huge amounts of traffic, making manual analysis difficult.

Sentinel AI demonstrates a machine-learning approach where network traffic features are analyzed automatically and classified into different traffic categories.

---

## 💡 Proposed Solution

Sentinel AI follows this workflow:

```text
Network Traffic Dataset
        ↓
Data Preprocessing
        ↓
Feature Processing
        ↓
Random Forest Model
        ↓
Threat Prediction
        ↓
Security Dashboard
        ↓
Threat Analysis
        ↓
Simulated Response
        ↓
Security Report
```

---

# 🧠 Machine Learning Model

## Random Forest Classifier

The project uses a **Random Forest Classifier**.

Random Forest is an ensemble machine-learning algorithm that combines multiple decision trees to make predictions.

Instead of depending on a single decision tree, Random Forest combines the results of multiple trees.

### Simple Explanation

Imagine asking 100 security experts:

> "Is this network traffic normal or dangerous?"

Each expert gives an opinion. Random Forest combines their opinions to produce a final prediction.

---

# 📊 Dataset

The project uses network-flow data from the **CICIDS2017 cybersecurity dataset**.

The current project uses:

```text
Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv
```

### Dataset Information

| Property | Value |
|---|---:|
| Total Rows | 225,745 |
| Total Columns | 79 |
| Input Features | 78 |
| Target Column | Label |
| Training Split | 80% |
| Testing Split | 20% |

### Classes

| Class | Description |
|---|---|
| BENIGN | Normal network traffic |
| DDoS | Distributed Denial-of-Service traffic |

### Class Distribution

```text
DDoS     → 128,027
BENIGN   → 97,718
```

---

# 🔧 Data Preprocessing

The following preprocessing steps are performed:

1. Load the CSV dataset
2. Remove whitespace from column names
3. Separate features and labels
4. Handle infinite values
5. Replace missing values
6. Split the data into training and testing sets
7. Train the Random Forest model

Example preprocessing code:

```python
X = X.replace([float("inf"), float("-inf")], float("nan"))
X = X.fillna(0)
```

---

# 🏋️ Model Training

The Random Forest model uses the following configuration:

```python
RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)
```

### Parameter Explanation

| Parameter | Meaning |
|---|---|
| `n_estimators=100` | Uses 100 decision trees |
| `random_state=42` | Helps produce reproducible results |
| `n_jobs=-1` | Uses available CPU cores |

---

# 📈 Model Results

The model was evaluated using a separate 20% test split.

### Test Accuracy

```text
99.9956%
```

### Confusion Matrix

```text
[[19543     1]
 [    1 25604]]
```

### Classification Report

| Class | Precision | Recall | F1-Score |
|---|---:|---:|---:|
| BENIGN | 1.00 | 1.00 | 1.00 |
| DDoS | 1.00 | 1.00 | 1.00 |

> ⚠️ **Important:** This performance was measured on a particular CICIDS2017 test split. It should not be interpreted as guaranteed real-world cybersecurity detection accuracy.

---

# 🖥️ Application Features

## 🏠 Dashboard

Provides an overview of the Sentinel AI system, including:

- System status
- Model status
- Threat detection information
- Dataset information
- Application navigation

## 📚 Project Info

Explains the project objective, dataset, machine-learning approach, technologies, and cybersecurity scope.

## 🚨 Threat Detection

Allows users to upload CSV network-traffic data and classify network flows as:

- BENIGN
- DDoS

### Workflow

```text
Upload CSV
    ↓
Validate Data
    ↓
Preprocess Features
    ↓
Machine Learning Model
    ↓
Threat Prediction
```

## 🌐 Network Analysis

Provides visual analysis of uploaded network traffic, including:

- Traffic distribution
- Threat distribution
- Network statistics
- Traffic tables
- Visual analytics

## 🔍 Flow Analyzer

Allows individual network flows to be examined using their feature values.

## 🛡️ Threat Response

Demonstrates simulated defensive response actions after detecting potential threats.

> **Note:** This project does not perform real firewall blocking or modify real network infrastructure.

## 📥 Security Report

Generates downloadable security reports containing prediction results and relevant traffic information.

## 📊 Feature Importance

Displays feature-importance information from the Random Forest model to help identify useful network-flow features.

## 🧠 AI Model

Displays information about the trained model, including:

- Algorithm
- Number of trees
- Dataset information
- Model status
- Prediction workflow

---


# 📸 Application Screenshots

## 🏠 Dashboard

![Sentinel AI Dashboard](https://raw.githubusercontent.com/JOEL7074/AI-Cyber-Threat-Detection/main/screenshots/dashboard.png)

---

## 🚨 Threat Detection

![Threat Detection](https://raw.githubusercontent.com/JOEL7074/AI-Cyber-Threat-Detection/main/screenshots/threat-detection.png)

---

## 🌐 Network Analysis

![Network Analysis](https://raw.githubusercontent.com/JOEL7074/AI-Cyber-Threat-Detection/main/screenshots/network-analysis.png)

---

## 📊 Feature Importance

![Feature Importance](https://raw.githubusercontent.com/JOEL7074/AI-Cyber-Threat-Detection/main/screenshots/feature-importance.png)

---

## 🛡️ Threat Response

![Threat Response](https://raw.githubusercontent.com/JOEL7074/AI-Cyber-Threat-Detection/main/screenshots/threat-response.png)
---

# 🏗️ Project Architecture

```text
                    ┌─────────────────────┐
                    │   Network Dataset   │
                    └──────────┬──────────┘
                               │
                               ↓
                    ┌─────────────────────┐
                    │ Data Preprocessing  │
                    └──────────┬──────────┘
                               │
                               ↓
                    ┌─────────────────────┐
                    │ Feature Processing  │
                    └──────────┬──────────┘
                               │
                               ↓
                    ┌─────────────────────┐
                    │   Random Forest     │
                    │   ML Classifier     │
                    └──────────┬──────────┘
                               │
                               ↓
                    ┌─────────────────────┐
                    │ Threat Prediction   │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              ↓                ↓                ↓
       Threat Detection   Network Analysis   Reports
              │
              ↓
       Simulated Response
```

---

# 🛠️ Technologies Used

- **Python**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **Random Forest**
- **Streamlit**
- **Plotly**
- **Joblib**
- **Visual Studio Code**
- **Git**
- **GitHub**

---

# 📁 Project Structure

```text
AI-Cyber-Threat-Detection/
│
├── app.py
├── train_model.py
├── threat_detection_model.pkl
├── README.md
├── .gitignore
│
├── data/
│   └── Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv
│
└── screenshots/
    ├── dashboard.png
    ├── threat-detection.png
    ├── network-analysis.png
    ├── feature-importance.png
    └── threat-response.png
```

---

# ⚙️ Installation and Setup

## 1. Clone the Repository

```bash
git clone https://github.com/JOEL7074/AI-Cyber-Threat-Detection.git
```

Move into the project directory:

```bash
cd AI-Cyber-Threat-Detection
```

## 2. Install Required Libraries

```bash
pip install pandas numpy scikit-learn streamlit plotly joblib
```

## 3. Train the Model

```bash
python train_model.py
```

The trained model will be saved as:

```text
threat_detection_model.pkl
```

## 4. Run the Application

```bash
python -m streamlit run app.py
```

Open the application at:

```text
http://localhost:8501
```

---

# 🔄 System Workflow

```text
CSV Network Traffic
        ↓
Data Cleaning
        ↓
Feature Processing
        ↓
Random Forest
        ↓
Threat Prediction
        ↓
BENIGN / DDoS
        ↓
Visualization
        ↓
Security Report
        ↓
Simulated Defensive Response
```

---

# 🔐 Cybersecurity Scope

This project is designed for **defensive cybersecurity and academic demonstration**.

It focuses on:

- Network traffic analysis
- Machine-learning-based threat detection
- DDoS classification
- Security visualization
- Threat reporting
- Simulated response

It does not include:

- Real-world attack execution
- Exploit development
- Malware
- Credential theft
- Unauthorized access
- Real firewall modification
- Offensive network operations

---

# ⚠️ Limitations

1. The model is trained on a specific portion of the CICIDS2017 dataset.
2. The current implementation focuses primarily on BENIGN and DDoS traffic.
3. The application analyzes uploaded CSV data instead of monitoring live network traffic.
4. Threat-response actions are simulated.
5. Test-split performance may not represent performance on unseen real-world traffic.

---

# 🚀 Future Enhancements

- Real-time network monitoring
- Additional attack classifications
- Larger and more diverse datasets
- Advanced anomaly detection
- Automated alerting
- SIEM integration
- Explainable AI
- Model retraining pipelines
- Cloud deployment
- Production-grade monitoring

---

# 🎓 Academic Significance

This project combines:

```text
Artificial Intelligence
        +
Machine Learning
        +
Data Science
        +
Cybersecurity
        +
Python
        +
Web Application Development
```

It provides practical exposure to:

- Data preprocessing
- Classification
- Model training
- Model evaluation
- Feature importance
- Data visualization
- Machine-learning deployment
- Cybersecurity analytics

---

# 👶 Simple Explanation

Imagine a security guard watching thousands of cars entering a city.

The guard cannot manually inspect every car, so we train an AI system using examples of normal and dangerous traffic.

```text
Normal traffic     → BENIGN
Potential DDoS     → DDoS
```

When new traffic arrives, the AI analyzes its characteristics and predicts its category.

The result is displayed on the Sentinel AI cybersecurity dashboard.

---

# 💬 One-Line Project Explanation

> Sentinel AI is a machine-learning-based cybersecurity system that analyzes network traffic and detects potential DDoS threats using a Random Forest classifier.

---

# 🧑‍💻 Key Project Keywords

```text
Python
Machine Learning
Artificial Intelligence
Cybersecurity
Network Security
Intrusion Detection
DDoS Detection
Random Forest
Scikit-learn
Pandas
NumPy
Streamlit
Plotly
Data Analysis
Feature Importance
Threat Detection
Security Analytics
```

---

# 👨‍💻 Author

**JOEL**

B.Tech — Artificial Intelligence & Data Science

---

# ⚠️ Disclaimer

This project is developed for educational, research, and defensive cybersecurity demonstration purposes.

The reported machine-learning performance is based on the selected CICIDS2017 dataset and test split. It should not be interpreted as guaranteed real-world cybersecurity performance.