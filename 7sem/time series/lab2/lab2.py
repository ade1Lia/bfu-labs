import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import warnings

warnings.filterwarnings('ignore')

np.random.seed(42)


def generate_time_series(n=200):
    t = np.arange(n)
    trend = 0.01 * t
    seasonality = 2 * np.sin(2 * np.pi * t / 50) + 1.5 * np.sin(2 * np.pi * t / 20)
    noise = np.random.normal(0, 0.5, n)
    series = trend + seasonality + noise
    return pd.Series(series, index=pd.date_range('2020-01-01', periods=n, freq='D'))


data = generate_time_series(200)
print(f"Длина временного ряда: {len(data)}")
print(f"Первые 5 значений:\n{data.head()}")

plt.figure(figsize=(12, 6))
plt.plot(data)
plt.title('Исходный временной ряд')
plt.xlabel('Дата')
plt.ylabel('Значение')
plt.grid(True)
plt.show()

from statsmodels.tsa.seasonal import seasonal_decompose

result = seasonal_decompose(data, model='additive', period=50)
fig = result.plot()
fig.set_size_inches(12, 8)
plt.show()

train_size = int(len(data) * 0.8)
train_data = data[:train_size]
test_data = data[train_size:]

from statsmodels.tsa.arima.model import ARIMA

try:
    model_arima = ARIMA(train_data, order=(2, 1, 2), seasonal_order=(1, 1, 1, 50))
    results_arima = model_arima.fit()

    train_predict = results_arima.predict(start=1, end=len(train_data) - 1)
    test_predict = results_arima.predict(start=len(train_data),
                                         end=len(data) - 1,
                                         dynamic=True)

    train_predict_series = pd.Series(train_predict, index=train_data.index[1:])
    test_predict_series = pd.Series(test_predict, index=test_data.index)

except Exception as e:
    print(f"Ошибка при построении ARIMA: {e}")

    train_predict_series = train_data.rolling(window=10).mean().dropna()
    test_predict_series = pd.Series(np.zeros(len(test_data)), index=test_data.index)

    simple_forecast = np.mean(train_data[-10:])
    test_predict_series[:] = simple_forecast

train_rmse = np.sqrt(mean_squared_error(train_data[1:], train_predict_series))
test_rmse = np.sqrt(mean_squared_error(test_data, test_predict_series))
train_mae = mean_absolute_error(train_data[1:], train_predict_series)
test_mae = mean_absolute_error(test_data, test_predict_series)
train_r2 = r2_score(train_data[1:], train_predict_series)
test_r2 = r2_score(test_data, test_predict_series)

print(f"\nМетрики качества модели:")
print(f"Обучающая выборка - RMSE: {train_rmse:.4f}, MAE: {train_mae:.4f}, R²: {train_r2:.4f}")
print(f"Тестовая выборка - RMSE: {test_rmse:.4f}, MAE: {test_mae:.4f}, R²: {test_r2:.4f}")

from statsmodels.tsa.holtwinters import ExponentialSmoothing

try:
    hw_model = ExponentialSmoothing(train_data,
                                    seasonal_periods=50,
                                    trend='add',
                                    seasonal='add')
    hw_fit = hw_model.fit()
    hw_forecast = hw_fit.forecast(len(test_data) + 30)

except Exception as e:
    print(f"Ошибка при построении Хольта-Винтерса: {e}")

    last_values = train_data[-10:].values
    forecast_values = np.concatenate([last_values,
                                      np.full(30, last_values.mean())])

    forecast_dates = pd.date_range(start=train_data.index[-10],
                                   periods=len(forecast_values),
                                   freq='D')
    hw_forecast = pd.Series(forecast_values, index=forecast_dates)

future_dates = pd.date_range(start=data.index[-1], periods=31, freq='D')[1:]
future_predictions = pd.Series(hw_forecast[-30:].values, index=future_dates)

plt.figure(figsize=(15, 10))

plt.subplot(3, 1, 1)
plt.plot(data, label='Исходный ряд', alpha=0.7)
plt.plot(train_predict_series, 'r', label='Предсказание на обучении (ARIMA)', alpha=0.7)
plt.plot(test_predict_series, 'g', label='Предсказание на тесте (ARIMA)', alpha=0.7)
plt.title('Моделирование временного ряда с помощью ARIMA')
plt.xlabel('Дата')
plt.ylabel('Значение')
plt.legend()
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(data[-50:], label='Исторические данные', alpha=0.7)
plt.plot(future_predictions, 'orange', label='Прогноз (Хольт-Винтерс)', linewidth=2, alpha=0.7)
plt.fill_between(future_dates,
                 future_predictions.values - test_rmse,
                 future_predictions.values + test_rmse,
                 alpha=0.2, color='orange', label='Доверительный интервал')
plt.title('Прогноз на 30 дней вперед')
plt.xlabel('Дата')
plt.ylabel('Значение')
plt.legend()
plt.grid(True)

plt.subplot(3, 1, 3)
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

plot_acf(data, lags=50, ax=plt.gca())
plt.title('Автокорреляционная функция (ACF)')
plt.grid(True)

plt.tight_layout()
plt.show()

print(f"\nЗАКЛЮЧЕНИЕ:")
print(f"1. Модель ARIMA показала R² = {test_r2:.4f} на тестовой выборке.")
print(f"2. Средняя абсолютная ошибка прогноза составляет {test_mae:.4f}.")

"""Метод Хольта-Винтерса, использованный для построения прогноза на 30 дней,
в совокупности с анализом ACF, выявившим сезонные паттерны с периодом около 50 дней,
позволили получить базовую модель ряда. Для повышения точности моделирования
целесообразно провести тонкую настройку параметров (p,d,q) модели ARIMA,
использовать специализированную кросс-валидацию для временных рядов или применить
более продвинутые методы, такие как Prophet или GARCH. По сравнению с нейросетевыми
подходами, использованные статистические методы обладают ключевыми преимуществами:
они проще в настройке и интерпретации, требуют значительно меньше вычислительных
ресурсов и позволяют строить теоретические доверительные интервалы. Однако их
недостатками являются меньшая гибкость при работе со сложными нелинейными зависимостями,
жёсткое требование стационарности исходного ряда и ограниченная эффективность при
моделировании длинных, сложных паттернов, где нейросетевые архитектуры (например, LSTM)
часто показывают лучшее качество прогнозирования."""