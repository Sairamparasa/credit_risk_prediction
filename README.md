# Credit Risk Scoring Project 🏦


An end-to-end machine learning solution that predicts credit risk for loan applicants using German credit data. This project demonstrates the complete ML pipeline from data exploration to model deployment with an interactive web application.

## 🎯 Project Overview

Financial institutions need to assess the creditworthiness of loan applicants to minimize default risk.This project builds a predictive model that classifies applicants as "good" or "bad" credit risks based on their personal and financial information.

**Key Achievements:**
- Built a Random Forest classifier with high accuracy for credit risk prediction
- Developed an interactive web application for real-time risk assessment
- Implemented proper data preprocessing and feature engineering
- Created a production-ready ML pipeline with model persistence


### 1. **Data Analysis & Exploration**
- Performed comprehensive EDA on German credit dataset (1000+ records)
- Analyzed feature distributions and correlations
- Identified key risk factors and patterns in credit defaults
- Handled missing values and data quality issues

### 2. **Machine Learning Pipeline**
- **Data Preprocessing**: Label encoding for categorical variables (Sex, Housing, Account status)
- **Feature Engineering**: Optimized feature selection for model performance
- **Model Training**: Implemented Random Forest classifier for robust predictions
- **Model Evaluation**: Achieved reliable performance metrics for credit risk assessment
- **Model Persistence**: Saved trained models and encoders for production use

### 3. **Web Application Development**
- Built interactive Streamlit application for user-friendly predictions
- Created intuitive form inputs for all applicant features
- Implemented real-time prediction with instant results
- Designed clean UI/UX for non-technical users

### 4. **Production-Ready Architecture**
- Organized codebase with proper project structure
- Implemented error handling and input validation
- Created reproducible environment with requirements management
- Documented complete setup and usage instructions

## 📊 Dataset Information    

**Source**:  German Credit Data
**Size**:  1000+ credit applications
**Target**:  Binary classification (Good/Bad credit risk)

### Input Features:
| Feature | Type | Description | Range/Values |
|---------|------|-------------|--------------|
| Age | Numerical | Applicant's age | 18-80 years |
| Sex | Categorical | Gender | male, female |
| Job | Numerical | Job category | 0-3 scale |
| Housing | Categorical | Housing situation | own, free, rent |
| Saving accounts | Categorical | Savings status | little, moderate, quite rich, rich |
| Checking account | Categorical | Checking status | little, moderate, rich |
| Credit amount | Numerical | Requested loan amount | Variable |
| Duration | Numerical | Loan duration | 1-30 months |

## 🛠️ Technical Stack

- **Machine Learning**: scikit-learn, Random Forest Classifier
- **Data Processing**: pandas, numpy
- **Visualization**: matplotlib, seaborn
- **Web Framework**: Streamlit
- **Model Persistence**: joblib
- **Development**: Jupyter Notebooks


## 📁 Project Structure
```
credit_risk_project/
├── data/                    # Dataset files
│   └── german_credit_data.csv
├── models/                  # Trained models and encoders
│   ├── random_forest_credit_model.pkl
│   ├── Sex_encoder.pkl
│   ├── Housing_encoder.pkl
│   ├── saving_accounts_encoder.pkl
│   ├── checking_account_encoder.pkl
│   └── target_encoder.pkl
├── src/                     # Source code
│   └── app.py              # Streamlit web application
├── notebooks/               # Jupyter notebooks
│   └── EDA.ipynb           # Exploratory data analysis
├── requirements.txt         # Python dependencies
└── README.md               # Project documentation
```

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation & Setup
1. **Clone or download the project**
   ```bash
   git clone <repository-url>
   cd credit_risk_project
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run src/app.py
   ```

5. **Access the app**
   - Open your browser and go to `http://localhost:8501`
   - Enter applicant information in the form
   - Click "Predict Risk" to get the credit risk assessment

## 💡 How It Works

1. **User Input**: Enter applicant details through the web interface
2. **Data Processing**: Categorical variables are encoded using pre-trained label encoders
3. **Prediction**: Random Forest model processes the features and outputs risk probability
4. **Result**: Display "Good" or "Bad" credit risk classification

## 🎯 Use Cases

- **Banks & Financial Institutions**: Automate loan approval processes
- **Credit Unions**: Assess member loan applications
- **Fintech Companies**: Integrate into lending platforms
- **Risk Management**: Portfolio risk assessment and monitoring

## 📈 Future Enhancements

- [ ] Add model performance metrics and validation scores
- [ ] Implement additional ML algorithms for comparison
- [ ] Add feature importance visualization
- [ ] Create API endpoints for integration
- [ ] Add batch prediction capabilities
- [ ] Implement model retraining pipeline

## 🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

**Built with ❤️ for better credit risk assessment**
