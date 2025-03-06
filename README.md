# **FineWine-AI: Quality Prediction and Personalized Wine Recommendations** 🍷

## **Project Overview** 🌟
FineWine-AI is an advanced machine learning model developed to predict the quality of wines based on their chemical properties and provide personalized recommendations for improving their taste, balance, and aroma. The system analyzes key attributes of wines, such as acidity, alcohol content, and sugar levels, to classify the wine as either "Good" or "Bad." It then offers actionable suggestions to enhance the wine's quality, food pairing options, and ideal serving methods. 🍇🍷

---

## **Problem Statement** 🚨
The wine industry traditionally relies on subjective human tasters for quality evaluation. However, wine quality is heavily influenced by chemical properties that are difficult to assess without expertise. **FineWine-AI** solves this problem by providing an AI-powered solution to predict wine quality objectively based on its chemical composition. In addition, it offers recommendations to improve wine quality, ideal food pairings, and serving methods. 🍇🍷

---

## **Key Features** ✨

- **🍷 Wine Quality Prediction**: Classifies the wine as "Good" or "Bad" based on its chemical properties.
- **🛠️ Personalized Recommendations**: Provides actionable ways to enhance the wine’s flavor (e.g., aeration, temperature adjustments).
- **🍴 Food Pairings**: Recommends ideal food pairings to complement the wine’s characteristics.
- **🥂 Serving Tips**: Suggests the best temperature and glassware for optimal tasting.
- **👨‍🍳 User-Friendly Interface**: Designed for wine enthusiasts and professionals alike.

---

## **Data Sources** 📊
The model uses data from publicly available wine datasets. The main dataset includes features like:

- **Fixed Acidity** 🧪
- **Volatile Acidity** 🧪
- **Citric Acid** 🍋
- **Residual Sugar** 🍬
- **Chlorides** 🧂
- **Free Sulphur Dioxide** 💨
- **Total Sulphur Dioxide** 💨
- **Density** ⚖️
- **pH** ⚗️
- **Alcohol Content** 🍷

These features are the foundation for predicting wine quality and providing personalized recommendations. 🍇

---

## **Installation** ⚙️

### Prerequisites 🖥️
Before running the code, make sure to have the following software installed:

- Python 3.10 🐍
- **pip** (Python package installer)

## 📥 Installation & Setup

Clone the repository:
```bash
git clone https://github.com/ldotmithu/FineWine-AI-Quality-Prediction-and-Personalized-Recommendations.git
cd FineWine-AI-Quality-Prediction-and-Personalized-Recommendations
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Run the application:
```bash
streamlit run app.py
```
---
```
### Model Training 📚 🚀
The machine learning model is trained on a dataset that includes features such as acidity levels, alcohol content, and residual sugar. It uses Random Forest for classification tasks to predict the quality of wine based on the input properties.

Data Preprocessing: The dataset is cleaned, normalized, and prepared for training. Missing values are handled, and feature scaling is applied to ensure consistent input for the model.

Model Selection: We use Random Forest for classification due to its robustness and ability to handle complex relationships between features.

Model Evaluation: The model is evaluated using standard metrics such as accuracy score, precision, recall, and F1-score to ensure reliable performance.

### License 📝
This project is licensed under the Apache License 📜



