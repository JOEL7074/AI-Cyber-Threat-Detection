
# 🛡️ Sentinel AI
## AI-Powered Cyber Threat Detection & Response System

Sentinel AI is a machine learning-based cybersecurity application designed to detect suspicious network activity and identify potential cyber threats using network traffic data.

The system uses a **Random Forest machine learning algorithm** to classify network traffic as either **BENIGN** or **DDoS**.

It provides an interactive cybersecurity dashboard built using **Python and Streamlit**.

---

# 📌 Project Overview

Cyberattacks are becoming increasingly common, and identifying malicious network traffic is an important part of cybersecurity.

Traditional network monitoring systems often require manual analysis of large amounts of network traffic.

Sentinel AI uses machine learning to analyze network traffic and identify potentially harmful activity.

The system provides a simple dashboard where users can:

- Analyze network traffic
- Detect potential DDoS attacks
- View network statistics
- Analyze individual network flows
- View machine learning predictions
- Generate security reports
- Understand important network features

> **Note:** This project is an educational prototype designed for defensive cybersecurity research and learning.

---

# 🎯 Project Objectives

The main objectives of Sentinel AI are:

1. Detect suspicious network traffic using machine learning.
2. Classify traffic as BENIGN or DDoS.
3. Reduce the need for manual traffic analysis.
4. Provide an interactive cybersecurity dashboard.
5. Display network traffic statistics and visualizations.
6. Generate downloadable security reports.
7. Demonstrate the application of AI in cybersecurity.

---

# 🚨 Problem Statement

Modern networks generate large amounts of traffic every second.

Analyzing this traffic manually can be time-consuming and difficult.

Cybersecurity professionals need tools that can help them identify suspicious traffic quickly.

This project aims to develop a machine learning-based system that can analyze network traffic and classify it into different categories.

---

# 💡 Proposed Solution

Sentinel AI uses the following workflow:

1. Load network traffic data from a CSV file.
2. Clean and preprocess the dataset.
3. Separate the input features and target labels.
4. Train a Random Forest classification model.
5. Test the trained model.
6. Save the trained model.
7. Load the model into a Streamlit application.
8. Predict whether network traffic is BENIGN or DDoS.
9. Display the results through a cybersecurity dashboard.

---

# 🧠 Machine Learning Algorithm

## Random Forest Classifier

Sentinel AI uses the **Random Forest Classifier**.

Random Forest is a machine learning algorithm that combines multiple decision trees to make a prediction.

Each decision tree makes a prediction, and the Random Forest combines the results to produce the final prediction.

### Why Random Forest?

- Suitable for classification problems
- Works well with tabular datasets
- Can handle many input features
- Provides feature importance values
- Easy to integrate with Python applications
- Useful for educational intrusion detection prototypes

---

# 📊 Dataset

This project uses network traffic data from the **CICIDS2017 dataset**.

The dataset contains network flow information collected for cybersecurity research.

### Dataset Details

| Property | Value |
|---|---|
| Dataset | CICIDS2017 |
| Dataset File | Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv |
| Total Rows | 225,745 |
| Total Columns | 79 |
| Input Features | 78 |
| Target Column | Label |
| Classes Used | BENIGN, DDoS |
| Training Split | 80% |
| Testing Split | 20% |

### Target Classes

- **BENIGN:** Normal network traffic.
- **DDoS:** Network traffic associated with Distributed Denial-of-Service activity in the dataset.

---

# 🧹 Data Preprocessing

The following preprocessing steps were performed:

1. Loaded the dataset using pandas.
2. Removed unnecessary spaces from column names.
3. Separated the input features from the target column.
4. Replaced infinite values with missing values.
5. Replaced missing values with zero.
6. Divided the dataset into training and testing data.
7. Used stratified sampling to preserve class distribution.

### Preprocessing Code

```python
X = data.drop("Label", axis=1)
y = data["Label"]

X = X.replace([float("inf"), float("-inf")], float("nan"))
X = X.fillna(0)
```

---

# 🤖 Model Training

The Random Forest model was trained using the following configuration:

```python
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)
```

### Training Process

```text
Dataset
   │
   ▼
Data Cleaning
   │
   ▼
Feature Selection
   │
   ▼
Train-Test Split
   │
   ▼
Random Forest Training
   │
   ▼
Model Evaluation
   │
   ▼
Saved Machine Learning Model
```

The trained model is saved as:

```text
threat_detection_model.pkl
```

---

# 📈 Model Performance

The model was evaluated using the test data.

### Evaluation Result

| Metric | Result |
|---|---|
| Test Accuracy | Approximately 99.9956% |
| Algorithm | Random Forest |
| Evaluation Dataset | CICIDS2017 test split |

### Confusion Matrix

```text
                 Predicted
              BENIGN    DDoS

Actual BENIGN   19543      1

Actual DDoS         1  25604
```

### Important Note

The reported accuracy was obtained on a specific test split of the CICIDS2017 dataset.

This result does **not** represent guaranteed real-world cybersecurity performance.

Real-world performance may differ because of:

- Different network environments
- New attack patterns
- Data distribution changes
- Dataset limitations
- Previously unseen traffic

---

# 🖥️ Application Features

## 🏠 Dashboard

The dashboard provides an overview of the Sentinel AI system.

It displays:

- System status
- Model availability
- Network traffic statistics
- Threat-related information
- Navigation to different modules

## 📚 Project Information

This section explains:

- Project objectives
- Dataset details
- Machine learning algorithm
- System workflow
- Project limitations

## 🚨 Threat Detection

Users can upload a CSV file containing network traffic data.

The application:

1. Reads the uploaded file.
2. Checks whether the required features are available.
3. Prepares the data for prediction.
4. Uses the trained model to classify network traffic.
5. Displays the prediction results.

## 🌐 Network Analysis

This section provides visualizations of the network traffic data.

It can display:

- Traffic distribution
- BENIGN and DDoS counts
- Network traffic statistics
- Summary tables
- Interactive charts

## 🔍 Flow Analyzer

The Flow Analyzer allows users to inspect individual network flow records.

Users can examine network features and view the model's prediction for a selected flow.

## 🛡️ Threat Response

This section demonstrates a simulated response workflow.

It can display:

- Threat status
- Recommended defensive actions
- Alert information
- Simulated response messages

> The response functionality is simulated for educational purposes. The application does not automatically block traffic or modify real firewall rules.

## 📥 Security Report

Users can generate and download a CSV report containing network traffic predictions.

The report can be used for:

- Basic analysis
- Documentation
- Academic demonstrations
- Security monitoring experiments

## 📊 Feature Importance

The application displays important features used by the Random Forest model.

Feature importance helps users understand which input variables contributed most to the model's decisions.

## 🧠 AI Model

This section provides information about:

- The trained model
- The machine learning algorithm
- Model configuration
- Dataset information
- Model evaluation

---

# 🏗️ System Architecture

```text
                  ┌───────────────────────┐
                  │   Network Flow Data   │
                  │       CSV File        │
                  └───────────┬───────────┘
                              │
                              ▼
                  ┌───────────────────────┐
                  │    Data Cleaning      │
                  │  Missing Value Fixes  │
                  └───────────┬───────────┘
                              │
                              ▼
                  ┌───────────────────────┐
                  │   Feature Processing  │
                  └───────────┬───────────┘
                              │
                              ▼
                  ┌───────────────────────┐
                  │   Random Forest AI    │
                  │        Model          │
                  └───────────┬───────────┘
                              │
                              ▼
                  ┌───────────────────────┐
                  │   Threat Prediction   │
                  │   BENIGN / DDoS       │
                  └───────────┬───────────┘
                              │
                              ▼
                  ┌───────────────────────┐
                  │   Sentinel AI Web App │
                  │      Streamlit        │
                  └───────────────────────┘
```

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Pandas | Data loading and preprocessing |
| NumPy | Numerical data processing |
| Scikit-learn | Machine learning model |
| Random Forest | Network traffic classification |
| Streamlit | Interactive web application |
| Plotly | Data visualization |
| Joblib | Model saving and loading |
| Git | Version control |
| GitHub | Project hosting |

---

# 📂 Project Structure

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

## 2. Open the Project Folder

```bash
cd AI-Cyber-Threat-Detection
```

## 3. Install Required Libraries

```bash
pip install pandas numpy scikit-learn streamlit plotly joblib
```

## 4. Train the Model

If the model file does not already exist, run:

```bash
python train_model.py
```

This will train the model and generate:

```text
threat_detection_model.pkl
```

## 5. Run the Application

On Windows, use:

```bash
python -m streamlit run app.py
```

The application will open in your browser at:

```text
http://localhost:8501
```

---

# 📸 Application Screenshots

## 🏠 Dashboard

![Sentinel AI Dashboard](screenshots/dashboard.png)

---

## 🚨 Threat Detection

![Threat Detection](screenshots/threat-detection.png)

---

## 🌐 Network Analysis

![Network Analysis](screenshots/network-analysis.png)

---

## 📊 Feature Importance

![Feature Importance](screenshots/feature-importance.png)

---

## 🛡️ Threat Response

![Threat Response](screenshots/threat-response.png)

---

# 🔐 Cybersecurity Scope

This project focuses exclusively on **defensive cybersecurity**.

The system is designed to demonstrate:

- Network traffic classification
- Intrusion detection concepts
- Machine learning in cybersecurity
- Threat monitoring
- Security reporting
- Simulated incident response

The project does not include:

- Real-world packet interception
- Automatic firewall modification
- Real network blocking
- Offensive security operations
- Exploit development
- Malware deployment

---

# ⚠️ Project Limitations

1. The model is trained on a specific dataset.
2. Only BENIGN and DDoS classes are used in this prototype.
3. The application does not process live network traffic.
4. The response module is simulated.
5. The model may not perform equally well on unseen network environments.
6. The reported accuracy is specific to the selected test split.
7. The system is not intended for production cybersecurity deployment.

---

# 🚀 Future Enhancements

Possible future improvements include:

- Live network traffic monitoring
- Support for additional attack categories
- Real-time alert notifications
- Improved data preprocessing
- Model comparison and optimization
- Explainable AI techniques
- Continuous model evaluation
- Integration with security monitoring platforms
- Improved anomaly detection
- More extensive validation using independent datasets

---

# 🎓 Academic Significance

This project demonstrates the practical application of:

- Artificial Intelligence
- Machine Learning
- Data Science
- Cybersecurity
- Network Traffic Analysis
- Classification Algorithms
- Data Preprocessing
- Data Visualization
- Python Application Development

It can be used as an educational project for understanding how machine learning can support cybersecurity monitoring.

---

# 👶 Simple Explanation of the Project

Imagine a security guard watching thousands of vehicles entering a city.

Some vehicles are normal, while others may be dangerous.

Instead of making the security guard check every vehicle manually, we train an AI system using examples of normal and suspicious traffic.

The AI learns patterns from the examples.

When new network traffic is provided, the AI predicts whether the traffic is normal or potentially related to a DDoS attack.

This is the basic idea behind Sentinel AI.

---

# 💬 One-Line Project Explanation

> Sentinel AI is a machine learning-based cybersecurity application that analyzes network traffic and classifies it as BENIGN or DDoS using a Random Forest model.

---

# 🔑 Important Project Keywords

- Artificial Intelligence
- Machine Learning
- Cybersecurity
- Network Intrusion Detection
- DDoS Detection
- Random Forest Classifier
- CICIDS2017 Dataset
- Python
- Streamlit
- Data Preprocessing
- Network Traffic Analysis
- Feature Importance
- Security Monitoring
- Threat Detection
- Defensive Cybersecurity

---

# 👨‍💻 Author

**JOEL**

GitHub: [JOEL7074](https://github.com/JOEL7074)

Project Repository: [AI Cyber Threat Detection](https://github.com/JOEL7074/AI-Cyber-Threat-Detection)

---

# ⚖️ Disclaimer

This project is intended for educational and academic purposes only.

It is a machine learning prototype and should not be used as a replacement for professional cybersecurity monitoring or incident-response systems.