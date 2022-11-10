import pandas as pd
from neuralprophet import NeuralProphet
import matplotlib.pyplot as plt

# Data is from https://www.kaggle.com/sumanthvrao/daily-climate-time-series-data
df = pd.read_csv("DailyDelhiClimateTest.csv", parse_dates=["date"])

# meantemp	humidity	wind_speed	meanpressure


df = df[["date", "meanpressure"]]
df.rename(columns={"date": "ds", "meanpressure": "y"}, inplace=True)


model = NeuralProphet()
#if you're using default variables below.

# model = NeuralProphet(
#     growth="linear",  # Determine trend types: 'linear', 'discontinuous', 'off'
#     changepoints=None, # list of dates that may include change points (None -> automatic )
#     n_changepoints=5,
#     changepoints_range=0.8,
#     trend_reg=0,
#     trend_reg_threshold=False,
#     yearly_seasonality="auto",
#     weekly_seasonality="auto",
#     daily_seasonality="auto",
#     seasonality_mode="additive",
#     seasonality_reg=0,
#     n_forecasts=1,
#     n_lags=0,
#     num_hidden_layers=0,
#     d_hidden=None,     # Dimension of hidden layers of AR-Net
#     # ar_sparsity=None,  # Sparcity in the AR coefficients
#     learning_rate=None,
#     epochs=40,
#     loss_func="Huber",
#     normalize="auto",  # Type of normalization ('minmax', 'standardize', 'soft', 'off')
#     impute_missing=True,
#     # log_level=None, # Determines the logging level of the logger object
# )

metrics = model.fit(df, freq="D")
future = model.make_future_dataframe(df, periods=365, n_historic_predictions=len(df))
forecast = model.predict(future)

fig, ax = plt.subplots(figsize=(14, 10))
model.plot(forecast, xlabel="Date", ylabel="Temp", ax=ax)
ax.set_title("Mean Temperature in Delhi", fontsize=28, fontweight="bold")

plt.show()


#fig, ax = plt.subplots(figsize=(14, 10))
#ax.plot(metrics["MAE"], 'ob', linewidth=6, label="Training Loss")
#ax.plot(metrics["MAE_val"], '-r', linewidth=2, label="Validation Loss")
# You can use metrics["SmoothL1Loss"] and metrics["SmoothL1Loss_val"] too.

