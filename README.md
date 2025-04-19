# 🌦️ Weather Forecasting with LSTM & Random Forest

This project utilizes both **deep learning (LSTM)** and **machine learning (Random Forest Regressor)** to forecast temperature and precipitation based on historical weather data.

---

## 🔍 Overview

- 📅 **Dataset**: Historical weather data with temperature (`tmin`, `tmax`, `tavg`) and precipitation (`prcp`).
- 📈 **LSTM**: Used to predict maximum temperature (`tmax`) for future dates using sequential patterns.
- 🌧️ **Random Forest**: Predicts future precipitation based on historical temperature trends and calendar features.
- 🧼 Data preprocessing includes: handling missing values, removing duplicates, normalization, and feature engineering.

---

## 🧰 Technologies Used

- Python
- Google Colab + Google Drive
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- Keras / TensorFlow (LSTM)
- RandomForestRegressor

---

## 📂 Dataset

Expected format: `weather.csv`

Columns:
- `time` (Date)
- `tavg` (Average temperature)
- `tmin` (Min temperature)
- `tmax` (Max temperature)
- `prcp` (Precipitation)

---

## 📊 LSTM Temperature Prediction

### 🧠 Model Details:
- Input: past 20 days of `tmax`
- Output: `tmax` forecast 100 days into the future
- Layers:
  - 3 LSTM layers (32 units each)
  - Dropout for regularization
  - Final Dense output layer

### 🔁 Workflow:
1. Load and clean data
2. Normalize using `StandardScaler`
3. Create time-series sequences
4. Train on past data
5. Predict future values for ~600 business days
6. Plot original vs predicted `tmax`

### 📉 Loss:
- Trained for 30 epochs
- Training + Validation loss plotted

---

## 🌧️ Random Forest Precipitation Forecast

### 🎯 Features:
- Year, Month, Day
- `tmax`, `tmin`, `tavg`

### 🔮 Targets:
- `prcp` (precipitation)

### 📈 Model Performance:
- Mean Squared Error: ~43.7
- R² Score: ~0.22

### 📆 Future Predictions:
- Generate calendar features for next 365 days
- Use monthly average temperature stats for seasonal mapping
- Predict `predicted_precipitation` for each future day

---

## 📈 Visualizations

- 📉 `Actual vs Predicted` temperature (`tmax`)
- 📊 `Actual vs Predicted` precipitation
- 📆 `Predicted Precipitation` for next year

---

## 🚀 How to Use

1. Upload `weather.csv` to your Google Drive.
2. Mount Google Drive in Colab.
3. Run all cells in the notebook to:
   - Train models
   - Forecast future weather
   - Visualize results

---

## 🧪 Results Snapshot

```text
trainX shape == (6568, 20, 1)
trainY shape == (6568, 1)
LSTM final validation loss: ~0.31
Random Forest R² Score: 0.22



⸻

⚠️ Notes
	•	This model is for educational purposes and may not generalize well to real-world meteorological forecasting.
	•	Precipitation is harder to predict and inherently more noisy than temperature data.
	•	You may improve results by incorporating humidity, pressure, or external climate data.

⸻
