# Bike Share Demand Prediction


This project is a machine learning model built to predict the total number of daily bike rentals (`cnt`) for a bike-sharing company based on seasonal and weather data.

---

## Live Demo

You can view and interact with the deployed Streamlit app here:

**[Live App Link](https://your-streamlit-app-url.streamlit.app/)** *(Note: You will get this URL after you deploy it on Streamlit Community Cloud)*

---

## Project Findings

The final model is a **Linear Regression** that successfully explains **~86% (R² = 0.859)** of the variance in bike demand.

Based on the model's coefficients, the **top 3 most significant variables** predicting bike demand are:

1.  **Weather Situation (Light Snow/Rain)**: This is by far the strongest predictor. Bad weather (light snow, rain, or thunderstorms) causes a massive *decrease* in bike rentals.
2.  **Season (Winter)**: This had the largest positive impact, indicating that bike rental demand in winter is significantly higher *compared to the baseline (Spring)*.
3.  **Season (Summer)**: This was the second-strongest positive predictor, also showing a high demand *compared to Spring*.

Other significant factors included temperature (`temp`), humidity (`hum`), and whether the day was a holiday (`holiday`).

---

## How to Run This Project Locally

### Prerequisites
- Python 3.10+
- `pip` (Python package installer)

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/Bike-Share-Demand-Prediction.git](https://github.com/your-username/Bike-Share-Demand-Prediction.git)
cd Bike-Share-Demand-Prediction
