import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import joblib
from datetime import datetime


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Sentinel AI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# DARK CYBERSECURITY THEME
# =========================================================

st.markdown(
    """
    <style>

        .stApp {
            background-color: #050505;
            color: #F5F5F5;
        }

        [data-testid="stSidebar"] {
            background-color: #0A0A0A;
        }

        [data-testid="stMetric"] {
            background-color: #0D0D0D;
            border: 1px solid #292929;
            padding: 15px;
            border-radius: 10px;
        }

        h1, h2, h3 {
            color: #FFFFFF;
        }

        p, label, span {
            color: #D5D5D5;
        }

        .stButton > button {
            background-color: #171717;
            color: white;
            border: 1px solid #444444;
            border-radius: 8px;
        }

        .stButton > button:hover {
            border-color: #00FF88;
            color: #00FF88;
        }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# LOAD TRAINED MODEL
# =========================================================

try:

    model = joblib.load("threat_detection_model.pkl")

    model_loaded = True

except Exception as error:

    model_loaded = False

    model = None

    st.error(
        f"Unable to load the AI model: {error}"
    )


# =========================================================
# SESSION STATE
# =========================================================

if "analysis_results" not in st.session_state:

    st.session_state.analysis_results = None


if "network_data" not in st.session_state:

    st.session_state.network_data = None


if "predictions" not in st.session_state:

    st.session_state.predictions = None


if "analysis_report" not in st.session_state:

    st.session_state.analysis_report = None


if "analysis_time" not in st.session_state:

    st.session_state.analysis_time = None


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("🛡️ SENTINEL AI")

st.sidebar.caption(
    "AI Cyber Threat Detection System"
)

st.sidebar.divider()


pages = [

    "🏠 Dashboard",

    "📚 Project Info",

    "🚨 Threat Detection",

    "🌐 Network Analysis",

    "🔍 Flow Analyzer",

    "🛡️ Threat Response",

    "📥 Security Report",

    "📊 Feature Importance",

    "🧠 AI Model"

]


page = st.sidebar.radio(
    "Navigation",
    pages
)


st.sidebar.divider()


st.sidebar.write("### System Status")


if model_loaded:

    st.sidebar.success(
        "🟢 AI Model Online"
    )

else:

    st.sidebar.error(
        "🔴 AI Model Offline"
    )


st.sidebar.caption(
    "Defensive security simulation only"
)


# =========================================================
# DASHBOARD
# =========================================================

if page == "🏠 Dashboard":

    st.title(
        "🛡️ Sentinel AI Dashboard"
    )

    st.write(
        "An AI-powered network threat detection and response prototype."
    )

    st.divider()


    col1, col2, col3, col4 = st.columns(4)


    col1.metric(
        "AI MODEL",
        "Random Forest"
    )


    col2.metric(
        "MODEL ACCURACY",
        "99.99%",
        "Test Dataset"
    )


    col3.metric(
        "DETECTION TYPE",
        "Network Traffic"
    )


    col4.metric(
        "SYSTEM STATUS",
        "ONLINE" if model_loaded else "OFFLINE"
    )


    st.divider()


    st.subheader(
        "🔐 System Capabilities"
    )


    capability_col1, capability_col2 = st.columns(2)


    with capability_col1:

        st.markdown(
            """
            ### 🔍 Threat Detection

            - Detects suspicious network traffic
            - Classifies network flows
            - Identifies DDoS traffic
            - Supports CSV dataset analysis
            """
        )


    with capability_col2:

        st.markdown(
            """
            ### 🛡️ Threat Response

            - Calculates threat severity
            - Recommends defensive actions
            - Generates simulated security alerts
            - Supports incident response demonstrations
            """
        )


    st.divider()


    st.subheader(
        "📊 Project Workflow"
    )


    st.code(
        """
Network Dataset
       ↓
Data Cleaning
       ↓
Random Forest AI
       ↓
Threat Classification
       ↓
Threat Severity Analysis
       ↓
Response Recommendation
       ↓
Security Report
        """,
        language="text"
    )


# =========================================================
# PROJECT INFO
# =========================================================

elif page == "📚 Project Info":

    st.title(
        "📚 Sentinel AI — Project Information"
    )

    st.write(
        "AI-powered Cyber Threat Detection and Response System"
    )

    st.divider()


    # -----------------------------------------------------
    # PROJECT OBJECTIVE
    # -----------------------------------------------------

    st.subheader(
        "🎯 Project Objective"
    )

    st.markdown(
        """
        Sentinel AI is a machine-learning-based cybersecurity prototype
        designed to identify potentially malicious network traffic.

        The system analyzes network-flow features and uses a trained
        Random Forest classifier to classify traffic as benign or
        potentially malicious.

        After detecting suspicious traffic, Sentinel AI provides a
        simulated defensive response recommendation.
        """
    )

    st.divider()


    # -----------------------------------------------------
    # PROBLEM STATEMENT
    # -----------------------------------------------------

    st.subheader(
        "⚠️ Problem Statement"
    )

    st.markdown(
        """
        Modern computer networks generate a large amount of traffic.

        Manually examining every network flow is difficult and
        time-consuming.

        Cybersecurity teams therefore require automated systems that
        can analyze network traffic and identify suspicious patterns.

        Sentinel AI demonstrates how machine learning can assist this
        process by automatically classifying network traffic.
        """
    )

    st.divider()


    # -----------------------------------------------------
    # PROPOSED SOLUTION
    # -----------------------------------------------------

    st.subheader(
        "💡 Proposed Solution"
    )

    st.markdown(
        """
        Sentinel AI follows a machine-learning pipeline.

        **1. Network Dataset**

        Network-flow data is provided as a CSV dataset.

        **2. Data Cleaning**

        Missing, infinite and invalid numerical values are handled.

        **3. Feature Processing**

        Network traffic features are provided to the trained model.

        **4. Machine Learning**

        A Random Forest classifier predicts the traffic category.

        **5. Threat Analysis**

        Predictions are analyzed to determine the amount of suspicious
        network activity.

        **6. Response Recommendation**

        The system generates simulated defensive recommendations.

        **7. Security Report**

        The analysis results can be exported for further investigation.
        """
    )

    st.divider()


    # -----------------------------------------------------
    # TECHNOLOGIES
    # -----------------------------------------------------

    st.subheader(
        "🛠️ Technologies Used"
    )


    tech_col1, tech_col2, tech_col3 = st.columns(3)


    with tech_col1:

        st.markdown(
            """
            ### 🐍 Programming

            - Python
            - Pandas
            - NumPy
            """
        )


    with tech_col2:

        st.markdown(
            """
            ### 🤖 Machine Learning

            - Scikit-learn
            - Random Forest
            - Classification
            """
        )


    with tech_col3:

        st.markdown(
            """
            ### 🖥️ Application

            - Streamlit
            - Plotly
            - Joblib
            """
        )


    st.divider()


    # -----------------------------------------------------
    # DATASET
    # -----------------------------------------------------

    st.subheader(
        "📊 Dataset"
    )

    st.markdown(
        """
        **Dataset:** CICIDS2017

        The project uses network-flow data from the CICIDS2017
        intrusion-detection dataset.

        The current trained model uses a dataset containing:

        - BENIGN network traffic
        - DDoS network traffic

        The model learns patterns in network-flow features and uses
        those patterns to classify previously unseen flows.
        """
    )

    st.divider()


    # -----------------------------------------------------
    # MACHINE LEARNING MODEL
    # -----------------------------------------------------

    st.subheader(
        "🧠 Machine Learning Model"
    )

    st.markdown(
        """
        Sentinel AI uses a **Random Forest Classifier**.

        Random Forest combines multiple decision trees to make a
        classification decision.

        Instead of relying on one decision tree, the algorithm builds
        many trees and combines their predictions.

        This makes Random Forest a useful machine-learning algorithm
        for classification problems involving many numerical features.
        """
    )

    st.divider()


    # -----------------------------------------------------
    # SYSTEM ARCHITECTURE
    # -----------------------------------------------------

    st.subheader(
        "🏗️ System Architecture"
    )

    st.code(
        """
                CICIDS2017 Dataset
                        │
                        ▼
                Data Preprocessing
                        │
                        ▼
                Feature Selection
                        │
                        ▼
              Random Forest Model
                        │
                        ▼
              Network Prediction
                        │
              ┌─────────┴─────────┐
              ▼                   ▼
          BENIGN              MALICIOUS
              │                   │
              │                   ▼
              │             Threat Analysis
              │                   │
              │                   ▼
              │           Response Recommendation
              │                   │
              └─────────┬─────────┘
                        ▼
                 Security Report
        """,
        language="text"
    )

    st.divider()


    # -----------------------------------------------------
    # ADVANTAGES
    # -----------------------------------------------------

    st.subheader(
        "✅ Advantages"
    )

    st.markdown(
        """
        - Automated network traffic classification
        - Machine-learning-based detection
        - Interactive web dashboard
        - Threat statistics and visualization
        - Individual network-flow analysis
        - Feature-importance analysis
        - Simulated defensive response
        - Downloadable security report
        """
    )

    st.divider()


    # -----------------------------------------------------
    # LIMITATIONS
    # -----------------------------------------------------

    st.subheader(
        "⚠️ Current Limitations"
    )

    st.markdown(
        """
        - The current prototype analyzes CSV datasets rather than
          live network traffic.

        - The model is trained on a specific dataset and attack
          categories.

        - The reported accuracy is based on the project's test split
          and does not represent guaranteed real-world performance.

        - Threat response is simulated and does not automatically
          modify firewall or network configurations.

        - Additional validation is required before deployment in
          a real cybersecurity environment.
        """
    )

    st.divider()


    # -----------------------------------------------------
    # FUTURE ENHANCEMENTS
    # -----------------------------------------------------

    st.subheader(
        "🚀 Future Enhancements"
    )

    st.markdown(
        """
        ### Phase 1 — Live Detection

        Integrate a controlled live network-monitoring pipeline.

        ### Phase 2 — More Attack Classes

        Extend the model to recognize additional types of network
        attacks.

        ### Phase 3 — Advanced Machine Learning

        Compare Random Forest with other machine-learning approaches.

        ### Phase 4 — Real-Time Alerting

        Add controlled notifications for security events.

        ### Phase 5 — Security Operations Dashboard

        Develop a more advanced monitoring interface for cybersecurity
        analysts.
        """
    )

    st.divider()


    # -----------------------------------------------------
    # PROJECT SUMMARY
    # -----------------------------------------------------

    st.subheader(
        "📌 Project Summary"
    )


    summary_col1, summary_col2, summary_col3 = st.columns(3)


    summary_col1.metric(
        "Project Type",
        "AI + Cybersecurity"
    )


    summary_col2.metric(
        "ML Algorithm",
        "Random Forest"
    )


    summary_col3.metric(
        "Application",
        "Streamlit"
    )


    st.success(
        "Sentinel AI demonstrates how machine learning can be used "
        "to support automated network threat detection and defensive "
        "security analysis."
    )


# =========================================================
# THREAT DETECTION
# =========================================================

elif page == "🚨 Threat Detection":

    st.title(
        "🚨 Network Threat Detection"
    )

    st.write(
        "Upload a network traffic CSV file to analyze potential threats."
    )


    uploaded_file = st.file_uploader(
        "Upload Network Traffic CSV",
        type=["csv"]
    )


    if uploaded_file is not None:

        try:

            data = pd.read_csv(
                uploaded_file
            )

            data.columns = data.columns.str.strip()


            st.success(
                "Dataset uploaded successfully."
            )


            st.write(
                "### Dataset Preview"
            )


            st.dataframe(
                data.head(10),
                use_container_width=True
            )


            st.write(
                "### Dataset Information"
            )


            info_col1, info_col2 = st.columns(2)


            info_col1.metric(
                "Rows",
                f"{data.shape[0]:,}"
            )


            info_col2.metric(
                "Columns",
                f"{data.shape[1]:,}"
            )


            if model_loaded:

                expected_features = list(
                    model.feature_names_in_
                )


                missing_features = [

                    feature

                    for feature in expected_features

                    if feature not in data.columns

                ]


                if missing_features:

                    st.error(
                        "The uploaded dataset is missing required model features."
                    )


                    st.write(
                        "Missing features:",
                        missing_features
                    )


                else:

                    if st.button(
                        "🔍 Analyze Network Traffic",
                        use_container_width=True
                    ):

                        with st.spinner(
                            "Sentinel AI is analyzing network traffic..."
                        ):

                            analysis_data = data.copy()


                            if "Label" in analysis_data.columns:

                                analysis_data = analysis_data.drop(
                                    "Label",
                                    axis=1
                                )


                            analysis_data = analysis_data[
                                expected_features
                            ]


                            analysis_data = analysis_data.replace(
                                [np.inf, -np.inf],
                                np.nan
                            )


                            analysis_data = analysis_data.fillna(
                                0
                            )


                            predictions = model.predict(
                                analysis_data
                            )


                            st.session_state.network_data = data


                            st.session_state.predictions = predictions


                            st.session_state.analysis_results = (
                                pd.Series(predictions).value_counts()
                            )


                            st.session_state.analysis_report = pd.DataFrame(
                                {
                                    "Prediction": predictions
                                }
                            )


                            st.session_state.analysis_time = (
                                datetime.now().strftime(
                                    "%Y-%m-%d %H:%M:%S"
                                )
                            )


                        st.success(
                            "Network traffic analysis completed successfully."
                        )


            else:

                st.error(
                    "The AI model is not available."
                )


        except Exception as error:

            st.error(
                f"Error while processing the dataset: {error}"
            )


# =========================================================
# NETWORK ANALYSIS
# =========================================================

elif page == "🌐 Network Analysis":

    st.title(
        "🌐 Network Traffic Analysis"
    )


    if (

        st.session_state.network_data is None

        or st.session_state.predictions is None

    ):

        st.warning(
            "Please analyze a dataset from the Threat Detection page first."
        )


    else:

        data = st.session_state.network_data.copy()

        predictions = st.session_state.predictions


        data["AI Prediction"] = predictions


        total_flows = len(
            predictions
        )


        malicious_flows = sum(

            1

            for prediction in predictions

            if str(prediction).upper() != "BENIGN"

        )


        safe_flows = (
            total_flows - malicious_flows
        )


        threat_percentage = (

            malicious_flows / total_flows * 100

            if total_flows > 0

            else 0

        )


        st.subheader(
            "📊 Security Overview"
        )


        col1, col2, col3, col4 = st.columns(4)


        col1.metric(
            "Total Flows",
            f"{total_flows:,}"
        )


        col2.metric(
            "Safe Flows",
            f"{safe_flows:,}"
        )


        col3.metric(
            "Threats",
            f"{malicious_flows:,}"
        )


        col4.metric(
            "Threat Rate",
            f"{threat_percentage:.2f}%"
        )


        if malicious_flows > 0:

            st.error(
                "🚨 Security Alert: Suspicious network activity detected!"
            )

        else:

            st.success(
                "🟢 No suspicious network activity detected."
            )


        st.divider()


        st.subheader(
            "📈 Threat Distribution"
        )


        prediction_counts = (

            pd.Series(predictions)

            .value_counts()

            .reset_index()

        )


        prediction_counts.columns = [

            "Threat Type",

            "Count"

        ]


        pie_chart = px.pie(

            prediction_counts,

            names="Threat Type",

            values="Count",

            title="Network Traffic Classification",

            hole=0.45

        )


        pie_chart.update_layout(

            template="plotly_dark",

            paper_bgcolor="#050505",

            plot_bgcolor="#050505"

        )


        st.plotly_chart(

            pie_chart,

            use_container_width=True

        )


        st.divider()


        st.subheader(
            "📊 Threat Type Comparison"
        )


        bar_chart = px.bar(

            prediction_counts,

            x="Threat Type",

            y="Count",

            title="Detected Network Traffic Categories",

            text="Count"

        )


        bar_chart.update_layout(

            template="plotly_dark",

            paper_bgcolor="#050505",

            plot_bgcolor="#050505"

        )


        st.plotly_chart(

            bar_chart,

            use_container_width=True

        )


        st.divider()


        st.subheader(
            "🚨 Recent Detected Threats"
        )


        threat_records = data[

            data["AI Prediction"]

            .astype(str)

            .str.upper() != "BENIGN"

        ]


        if len(threat_records) > 0:

            st.write(

                f"Showing the first "
                f"{min(100, len(threat_records))} "
                "detected suspicious records."

            )


            st.dataframe(

                threat_records.head(100),

                use_container_width=True,

                hide_index=True

            )


        else:

            st.success(
                "No malicious records were found."
            )


        st.divider()


        st.subheader(
            "📄 Network Data Preview"
        )


        st.dataframe(

            data.head(100),

            use_container_width=True,

            hide_index=True

        )


# =========================================================
# FLOW ANALYZER
# =========================================================

elif page == "🔍 Flow Analyzer":

    st.title(
        "🔍 Individual Flow Analyzer"
    )


    if (

        st.session_state.network_data is None

        or st.session_state.predictions is None

    ):

        st.warning(
            "Please analyze a dataset from the Threat Detection page first."
        )


    else:

        data = st.session_state.network_data

        predictions = st.session_state.predictions


        flow_number = st.number_input(

            "Select Flow Number",

            min_value=1,

            max_value=len(data),

            value=1,

            step=1

        )


        selected_index = (
            int(flow_number) - 1
        )


        selected_flow = data.iloc[
            selected_index
        ]


        selected_prediction = predictions[
            selected_index
        ]


        st.subheader(
            "📄 Flow Information"
        )


        st.dataframe(

            selected_flow.to_frame("Value"),

            use_container_width=True

        )


        st.subheader(
            "🤖 AI Prediction"
        )


        if str(selected_prediction).upper() == "BENIGN":

            st.success(
                "🟢 BENIGN — No malicious activity detected."
            )

        else:

            st.error(
                f"🔴 THREAT DETECTED — {selected_prediction}"
            )


        if hasattr(model, "predict_proba"):

            expected_features = list(
                model.feature_names_in_
            )


            flow_data = data.iloc[
                [selected_index]
            ].copy()


            if "Label" in flow_data.columns:

                flow_data = flow_data.drop(
                    "Label",
                    axis=1
                )


            flow_data = flow_data[
                expected_features
            ]


            flow_data = flow_data.replace(

                [np.inf, -np.inf],

                np.nan

            )


            flow_data = flow_data.fillna(
                0
            )


            probabilities = model.predict_proba(
                flow_data
            )[0]


            classes = model.classes_


            probability_data = pd.DataFrame(

                {

                    "Class": classes,

                    "Probability": probabilities * 100

                }

            )


            st.subheader(
                "📈 Prediction Confidence"
            )


            st.dataframe(

                probability_data,

                use_container_width=True,

                hide_index=True

            )


# =========================================================
# THREAT RESPONSE
# =========================================================

elif page == "🛡️ Threat Response":

    st.title(
        "🛡️ Automated Threat Response"
    )


    st.write(
        "Sentinel AI analyzes detected threats and recommends "
        "defensive actions."
    )


    if st.session_state.predictions is None:

        st.warning(
            "⚠️ No network traffic has been analyzed yet. "
            "Go to Threat Detection and analyze a dataset first."
        )


    else:

        predictions = st.session_state.predictions


        total_flows = len(
            predictions
        )


        attack_count = sum(

            1

            for prediction in predictions

            if str(prediction).upper() != "BENIGN"

        )


        safe_count = (
            total_flows - attack_count
        )


        threat_percentage = (

            attack_count / total_flows * 100

            if total_flows > 0

            else 0

        )


        st.subheader(
            "📊 Security Status"
        )


        col1, col2, col3 = st.columns(3)


        col1.metric(

            "Total Network Flows",

            f"{total_flows:,}"

        )


        col2.metric(

            "Detected Threats",

            f"{attack_count:,}"

        )


        col3.metric(

            "Threat Percentage",

            f"{threat_percentage:.2f}%"

        )


        st.divider()


        st.subheader(
            "🚨 Threat Level"
        )


        if threat_percentage == 0:

            threat_level = "SAFE"

            st.success(
                "🟢 SAFE — No malicious network activity detected."
            )


        elif threat_percentage < 10:

            threat_level = "LOW"

            st.info(
                "🔵 LOW RISK — A small amount of suspicious activity was detected."
            )


        elif threat_percentage < 30:

            threat_level = "MEDIUM"

            st.warning(
                "🟡 MEDIUM RISK — Multiple suspicious network flows were detected."
            )


        elif threat_percentage < 60:

            threat_level = "HIGH"

            st.error(
                "🟠 HIGH RISK — Significant malicious network activity detected."
            )


        else:

            threat_level = "CRITICAL"

            st.error(
                "🔴 CRITICAL — Large-scale cyber attack activity detected."
            )


        st.divider()


        st.subheader(
            "🤖 AI Response Engine"
        )


        if attack_count == 0:

            st.write(
                "### ✅ Recommended Action"
            )


            st.success(
                "Continue normal network monitoring."
            )


            st.markdown(
                """
                **Recommended defensive actions:**

                - Continue monitoring network traffic
                - Maintain firewall protection
                - Keep security software updated
                - Store network logs for future analysis
                """
            )


        else:

            st.write(
                "### 🚨 Recommended Defensive Actions"
            )


            if threat_level == "LOW":

                st.markdown(
                    """
                    **1. Increase Network Monitoring**

                    Monitor suspicious network flows more closely.

                    **2. Record Suspicious Events**

                    Store suspicious traffic information in security logs.

                    **3. Review Network Activity**

                    Security administrators should inspect unusual activity.
                    """
                )


            elif threat_level == "MEDIUM":

                st.markdown(
                    """
                    **1. Flag Suspicious Network Sources**

                    Potential malicious traffic sources should be flagged.

                    **2. Increase Traffic Monitoring**

                    Enable enhanced network monitoring.

                    **3. Notify Security Administrator**

                    Generate an alert for the cybersecurity team.

                    **4. Preserve Security Logs**

                    Store attack information for investigation.
                    """
                )


            elif threat_level == "HIGH":

                st.markdown(
                    """
                    **1. Isolate Suspicious Network Traffic**

                    Suspicious traffic should be separated from trusted traffic.

                    **2. Review Suspicious Sources**

                    Potential attack sources should be reviewed by administrators.

                    **3. Alert Security Team**

                    Generate a high-priority security notification.

                    **4. Preserve Attack Evidence**

                    Store network logs for forensic investigation.

                    **5. Continue AI Monitoring**

                    Continue analyzing incoming network traffic.
                    """
                )


            else:

                st.markdown(
                    """
                    **1. Activate Emergency Monitoring**

                    Apply strict defensive monitoring procedures.

                    **2. Review Affected Network Segments**

                    Investigate potentially affected network areas.

                    **3. Review Suspicious Traffic**

                    Security administrators should investigate suspicious sources.

                    **4. Generate Critical Security Alert**

                    Notify the cybersecurity response team.

                    **5. Preserve Attack Logs**

                    Store detected traffic for incident investigation.

                    **6. Begin Incident Response**

                    Security personnel should investigate the incident immediately.
                    """
                )


        st.divider()


        st.subheader(
            "⚡ Automated Response Simulation"
        )


        st.caption(
            "This simulation does not modify firewall rules, "
            "network settings, or real devices."
        )


        if attack_count > 0:

            if st.button(

                "🛡️ Activate AI Threat Response",

                use_container_width=True

            ):

                st.success(
                    "Sentinel AI defensive response activated successfully."
                )


                st.write(
                    "### Response Actions"
                )


                st.write(
                    "✅ Malicious traffic identified"
                )


                st.write(
                    "✅ Suspicious network flows flagged"
                )


                st.write(
                    "✅ Security alert generated"
                )


                st.write(
                    "✅ Attack information stored"
                )


                st.write(
                    "✅ Network monitoring increased"
                )


                if threat_level in [

                    "HIGH",

                    "CRITICAL"

                ]:

                    st.write(
                        "✅ Network isolation recommended"
                    )


                st.info(
                    "Simulation complete. No real firewall rules "
                    "or network settings were modified."
                )


        else:

            st.success(
                "No threat response is required."
            )


        st.divider()


        st.subheader(
            "📋 Incident Response Summary"
        )


        response_data = {

            "Total Network Flows": total_flows,

            "Safe Flows": safe_count,

            "Malicious Flows": attack_count,

            "Threat Percentage":
                f"{threat_percentage:.2f}%",

            "Threat Level": threat_level

        }


        response_summary = pd.DataFrame(

            list(response_data.items()),

            columns=[

                "Metric",

                "Value"

            ]

        )


        st.dataframe(

            response_summary,

            use_container_width=True,

            hide_index=True

        )


# =========================================================
# SECURITY REPORT
# =========================================================

elif page == "📥 Security Report":

    st.title(
        "📥 Security Report"
    )


    if st.session_state.analysis_report is None:

        st.warning(
            "Please analyze a dataset from the Threat Detection page first."
        )


    else:

        st.write(
            "### Analysis Summary"
        )


        st.write(

            f"Analysis completed at: "
            f"{st.session_state.analysis_time}"

        )


        report = (
            st.session_state.analysis_report
        )


        total_records = len(
            report
        )


        threat_records = sum(

            1

            for prediction in report["Prediction"]

            if str(prediction).upper() != "BENIGN"

        )


        safe_records = (
            total_records - threat_records
        )


        col1, col2, col3 = st.columns(3)


        col1.metric(

            "Total Records",

            f"{total_records:,}"

        )


        col2.metric(

            "Safe Records",

            f"{safe_records:,}"

        )


        col3.metric(

            "Threat Records",

            f"{threat_records:,}"

        )


        st.divider()


        st.subheader(
            "📄 Prediction Report"
        )


        st.dataframe(

            report.head(1000),

            use_container_width=True

        )


        csv_report = report.to_csv(
            index=False
        ).encode("utf-8")


        st.download_button(

            label="⬇️ Download Security Report",

            data=csv_report,

            file_name="sentinel_ai_security_report.csv",

            mime="text/csv",

            use_container_width=True

        )


# =========================================================
# FEATURE IMPORTANCE
# =========================================================

elif page == "📊 Feature Importance":

    st.title(
        "📊 AI Feature Importance"
    )


    st.write(
        "This page shows which network traffic features influenced "
        "the Random Forest model most strongly."
    )


    if not model_loaded:

        st.error(
            "The AI model is not available."
        )


    elif not hasattr(
        model,
        "feature_importances_"
    ):

        st.warning(
            "Feature importance is not available for this model."
        )


    else:

        feature_names = list(
            model.feature_names_in_
        )


        importance_values = list(
            model.feature_importances_
        )


        importance_data = pd.DataFrame(

            {

                "Feature": feature_names,

                "Importance": importance_values

            }

        )


        importance_data = (
            importance_data.sort_values(
                by="Importance",
                ascending=False
            )
        )


        top_features = (
            importance_data.head(15).copy()
        )


        top_features[
            "Importance Percentage"
        ] = (
            top_features["Importance"] * 100
        )


        st.subheader(
            "🏆 Top 15 Important Features"
        )


        metric_col1, metric_col2, metric_col3 = st.columns(3)


        metric_col1.metric(

            "Total Features",

            len(importance_data)

        )


        metric_col2.metric(

            "Most Important Feature",

            top_features.iloc[0]["Feature"]

        )


        metric_col3.metric(

            "Top Feature Importance",

            f"{top_features.iloc[0]['Importance Percentage']:.2f}%"

        )


        st.divider()


        feature_chart = px.bar(

            top_features.sort_values(

                by="Importance",

                ascending=True

            ),

            x="Importance Percentage",

            y="Feature",

            orientation="h",

            title="Top 15 Network Features",

            labels={

                "Importance Percentage":
                    "Importance (%)",

                "Feature":
                    "Network Feature"

            }

        )


        feature_chart.update_layout(

            template="plotly_dark",

            paper_bgcolor="#050505",

            plot_bgcolor="#050505"

        )


        st.plotly_chart(

            feature_chart,

            use_container_width=True

        )


        st.subheader(
            "📋 Feature Importance Table"
        )


        st.dataframe(

            top_features,

            use_container_width=True,

            hide_index=True

        )


        st.divider()


        st.subheader(
            "🧠 What Does This Mean?"
        )


        st.markdown(
            """
            Feature importance indicates how useful each network feature
            was when the Random Forest model made its decisions.

            Examples of network features include:

            - Flow duration
            - Packet count
            - Packet length
            - Forward and backward traffic
            - Network flow rates

            The model uses combinations of these features to distinguish
            between benign and suspicious network traffic.

            **Important:** Feature importance does not prove that a feature
            directly causes a cyberattack.
            """
        )


        total_top_importance = (

            top_features[
                "Importance Percentage"
            ].sum()

        )


        st.info(

            f"The top 15 features together contribute approximately "
            f"{total_top_importance:.2f}% of the total feature importance."

        )


# =========================================================
# AI MODEL INFORMATION
# =========================================================

elif page == "🧠 AI Model":

    st.title(
        "🧠 AI Model Information"
    )


    st.write(
        "Technical information about the trained machine learning model."
    )


    if model_loaded:

        col1, col2, col3 = st.columns(3)


        col1.metric(
            "Algorithm",
            "Random Forest"
        )


        col2.metric(

            "Number of Trees",

            getattr(
                model,
                "n_estimators",
                "N/A"
            )

        )


        col3.metric(

            "Number of Features",

            len(model.feature_names_in_)

            if hasattr(
                model,
                "feature_names_in_"
            )

            else "N/A"

        )


        st.divider()


        st.subheader(
            "🔧 Model Workflow"
        )


        st.code(
            """
CSV Network Dataset
        ↓
Data Cleaning
        ↓
Feature Selection
        ↓
Random Forest Classifier
        ↓
Threat Prediction
        ↓
Security Response Recommendation
            """,
            language="text"
        )


        st.subheader(
            "📚 Technologies Used"
        )


        st.markdown(
            """
            - Python
            - Pandas
            - NumPy
            - Scikit-learn
            - Random Forest
            - Streamlit
            - Plotly
            - Joblib
            """
        )


        st.subheader(
            "⚠️ Project Limitation"
        )


        st.warning(
            "The reported model accuracy is based on the selected test "
            "dataset and should not be interpreted as real-world accuracy."
        )


    else:

        st.error(
            "The AI model is not available."
        )


# =========================================================
# FOOTER
# =========================================================

st.sidebar.divider()


st.sidebar.caption(
    "SENTINEL AI • AI CYBER THREAT DETECTION SYSTEM"
)