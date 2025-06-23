import numpy as np

# 30 days of temperature data (in °C)
temperatures = np.array([
    32.5, 33.2, 31.0, 29.8, 30.5, 28.0, 27.5, 30.2, 32.0, 34.5,
    35.0, 36.1, 31.5, 33.0, 32.3, 31.7, 30.9, 28.8, 29.5, 30.0,
    33.5, 34.0, 36.5, 35.2, 32.8, 31.1, 30.2, 29.0, 28.5, 27.8
])

# Average temperature
avg_temp = np.mean(temperatures)

# Max and min temperature
max_temp = np.max(temperatures)
min_temp = np.min(temperatures)

# Days with above average temperature
above_avg_days = np.sum(temperatures > avg_temp)

# Days with below average temperature
below_avg_days = np.sum(temperatures < avg_temp)

# Print results
print("🌡️ Average temperature:", round(avg_temp, 2), "°C")
print("🔥 Highest temperature:", max_temp, "°C")
print("❄️ Lowest temperature:", min_temp, "°C")
print("📈 Days above average:", above_avg_days)
print("📉 Days below average:", below_avg_days)
