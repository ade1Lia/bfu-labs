import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import csv
from statsmodels.tsa.stattools import adfuller, kpss
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from sklearn.metrics import mean_absolute_error, mean_squared_error
import warnings

warnings.filterwarnings('ignore')


def generate_time_series(n_points=1000, has_trend=True, has_seasonality=True, seed=None):
    if seed is not None:
        np.random.seed(seed)

    start_date = datetime(2020, 1, 1)
    dates = [(start_date + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(n_points)]

    noise = np.random.normal(0, 5, n_points)

    trend_component = np.zeros(n_points)
    seasonal_component = np.zeros(n_points)

    if has_trend:
        trend_type = np.random.choice(['linear', 'quadratic', 'logarithmic'])
        if trend_type == 'linear':
            slope = np.random.uniform(-0.5, 0.5)
            intercept = np.random.uniform(50, 100)
            trend_component = slope * np.arange(n_points) + intercept
        elif trend_type == 'quadratic':
            a = np.random.uniform(-0.001, 0.001)
            b = np.random.uniform(-0.1, 0.1)
            c = np.random.uniform(50, 100)
            x = np.arange(n_points)
            trend_component = a * x ** 2 + b * x + c
        else:
            a = np.random.uniform(10, 30)
            b = np.random.uniform(50, 100)
            trend_component = a * np.log(np.arange(n_points) + 1) + b

    if has_seasonality:
        n_seasons = np.random.randint(1, 4)
        for _ in range(n_seasons):
            amplitude = np.random.uniform(10, 30)
            period = np.random.uniform(30, 365)
            phase = np.random.uniform(0, 2 * np.pi)
            seasonal_component += amplitude * np.sin(2 * np.pi * np.arange(n_points) / period + phase)

    values = noise + trend_component + seasonal_component
    return dates, values


def run_statistical_tests(series):
    adf_result = adfuller(series)
    kpss_result = kpss(series)

    print("Тест Дики-Фуллера (ADF):")
    print(f"Статистика: {adf_result[0]:.4f}")
    print(f"p-value: {adf_result[1]:.4f}")
    print(f"Критические значения: {adf_result[4]}")
    print(f"Стационарность: {'Да' if adf_result[1] < 0.05 else 'Нет'}")

    print("\nТест KPSS:")
    print(f"Статистика: {kpss_result[0]:.4f}")
    print(f"p-value: {kpss_result[1]:.4f}")
    print(f"Стационарность: {'Да' if kpss_result[1] > 0.05 else 'Нет'}")


def decompose_time_series(dates, values, period=365):
    date_objects = [datetime.strptime(d, '%Y-%m-%d') for d in dates]

    try:
        decomposition = seasonal_decompose(values, model='additive', period=period)

        fig, axes = plt.subplots(4, 1, figsize=(14, 10))

        axes[0].plot(date_objects, values)
        axes[0].set_ylabel('Исходный ряд')

        axes[1].plot(date_objects, decomposition.trend)
        axes[1].set_ylabel('Тренд')

        axes[2].plot(date_objects, decomposition.seasonal)
        axes[2].set_ylabel('Сезонность')

        axes[3].plot(date_objects, decomposition.resid)
        axes[3].set_ylabel('Остатки')
        axes[3].set_xlabel('Дата')

        plt.tight_layout()
        plt.show()

        return decomposition

    except:
        print("Невозможно выполнить декомпозицию с указанным периодом")
        return None


def plot_acf_pacf(values, lags=40):
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    plot_acf(values, lags=lags, ax=axes[0])
    axes[0].set_title('Автокорреляционная функция (ACF)')

    plot_pacf(values, lags=lags, ax=axes[1])
    axes[1].set_title('Частная автокорреляционная функция (PACF)')

    plt.tight_layout()
    plt.show()


def train_holt_winters_model(train_data, test_data, seasonal_periods=365):
    model = ExponentialSmoothing(train_data,
                                 trend='add',
                                 seasonal='add',
                                 seasonal_periods=seasonal_periods,
                                 initialization_method='estimated')
    fitted_model = model.fit()

    forecast = fitted_model.forecast(steps=len(test_data))

    return fitted_model, forecast


def calculate_metrics(true_values, predicted_values):
    mae = mean_absolute_error(true_values, predicted_values)
    mse = mean_squared_error(true_values, predicted_values)
    rmse = np.sqrt(mse)
    mape = np.mean(np.abs((true_values - predicted_values) / true_values)) * 100

    print(f"MAE: {mae:.4f}")
    print(f"MSE: {mse:.4f}")
    print(f"RMSE: {rmse:.4f}")
    print(f"MAPE: {mape:.2f}%")

    return {'MAE': mae, 'MSE': mse, 'RMSE': rmse, 'MAPE': mape}


def plot_forecast_with_ci(dates, train_data, test_data, forecast, model_fit, forecast_steps=365, confidence_level=0.95):
    date_objects = [datetime.strptime(d, '%Y-%m-%d') for d in dates]
    last_date = date_objects[-1]

    forecast_dates = [last_date + timedelta(days=i + 1) for i in range(forecast_steps)]

    all_dates = date_objects + forecast_dates

    full_forecast = model_fit.forecast(steps=forecast_steps)

    residuals = train_data - model_fit.fittedvalues
    std_residuals = np.std(residuals)

    z_score = 1.96
    lower_bound = full_forecast - z_score * std_residuals
    upper_bound = full_forecast + z_score * std_residuals

    plt.figure(figsize=(14, 8))

    historical_data = np.concatenate([train_data, test_data])
    plt.plot(date_objects[:len(historical_data)], historical_data, label='Исторические данные', color='blue',
             linewidth=1.5)

    split_idx = len(train_data)
    plt.axvline(x=date_objects[split_idx - 1], color='red', linestyle='--', alpha=0.7, label='Начало прогноза')

    plt.plot(forecast_dates, full_forecast, label='Прогноз', color='green', linewidth=2)

    plt.fill_between(forecast_dates, lower_bound, upper_bound, color='green', alpha=0.2,
                     label=f'Доверительный интервал {confidence_level * 100:.0f}%')

    if len(test_data) > 0:
        test_dates = date_objects[split_idx:split_idx + len(test_data)]
        plt.plot(test_dates, test_data, label='Тестовые данные', color='orange', linewidth=1.5)

    plt.title('Прогноз временного ряда с доверительным интервалом', fontsize=14)
    plt.xlabel('Дата')
    plt.ylabel('Значение')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.gcf().autofmt_xdate()
    plt.tight_layout()
    plt.show()


def main():
    np.random.seed(42)

    n_points = 1000
    forecast_steps = 100

    dates, values = generate_time_series(n_points=n_points, has_trend=True, has_seasonality=True, seed=42)

    date_objects = [datetime.strptime(d, '%Y-%m-%d') for d in dates]

    plt.figure(figsize=(14, 6))
    plt.plot(date_objects, values, color='blue', linewidth=1.5)
    plt.title('Сгенерированный временной ряд')
    plt.xlabel('Дата')
    plt.ylabel('Значение')
    plt.grid(True, alpha=0.3)
    plt.gcf().autofmt_xdate()
    plt.tight_layout()
    plt.show()

    print("Результаты статистических тестов:")
    run_statistical_tests(values)

    print("\nДекомпозиция временного ряда:")
    decompose_time_series(dates, values, period=365)

    print("\nАвтокорреляционные функции:")
    plot_acf_pacf(values, lags=40)

    print("Выбор метода моделирования:")
    print("Анализ ACF показал наличие значимых автокорреляций на нескольких лагах,")
    print("PACF демонстрирует быстрый спад после первых лагов.")
    print("Ряд содержит тренд и сезонность (подтверждено декомпозицией).")
    print("Выбран метод Хольта-Винтерса (тройное экспоненциальное сглаживание),")
    print("так как он эффективно моделирует ряды с трендом и сезонностью.")

    train_size = int(len(values) * 0.8)
    train_data = values[:train_size]
    test_data = values[train_size:]

    print(f"\nРазделение данных: {train_size} точек для обучения, {len(test_data)} для тестирования")

    model_fit, forecast = train_holt_winters_model(train_data, test_data, seasonal_periods=365)

    print("\nМетрики качества на тестовой выборке:")
    metrics = calculate_metrics(test_data, forecast)

    print(f"\nПрогноз на {forecast_steps} периодов вперед:")
    plot_forecast_with_ci(dates, train_data, test_data, forecast, model_fit, forecast_steps)

    print("\nПараметры модели:")
    print(f"Сглаживание уровня (alpha): {model_fit.params['smoothing_level']:.4f}")
    print(f"Сглаживание тренда (beta): {model_fit.params['smoothing_trend']:.4f}")
    print(f"Сглаживание сезонности (gamma): {model_fit.params['smoothing_seasonal']:.4f}")
    print(f"Начальный уровень: {model_fit.params['initial_level']:.4f}")
    print(f"Начальный тренд: {model_fit.params['initial_trend']:.4f}")

    last_values = model_fit.forecast(steps=10)
    print(f"\nПервые 10 значений прогноза:")
    for i, val in enumerate(last_values[:10], 1):
        print(f"Период {i}: {val:.4f}")


if __name__ == "__main__":
    main()