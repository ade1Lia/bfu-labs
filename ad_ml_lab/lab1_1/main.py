import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def read_data(filename):
    "Чтение данных из CSV-файла"
    return pd.read_csv(filename)


def show_statistics(data, x_col, y_col):
    "Вывод статистической информации о данных"
    stats = {
        'Количество': len(data),
        'Минимум': data.min(),
        'Максимум': data.max(),
        'Среднее': data.mean()
    }
    print(pd.DataFrame(stats))


def linear_regression(x, y):
    "Реализация метода наименьших квадратов"
    x_mean = np.mean(x)
    y_mean = np.mean(y)

    numerator = np.sum((x - x_mean) * (y - y_mean))
    denominator = np.sum((x - x_mean) ** 2)

    b1 = numerator / denominator
    b0 = y_mean - b1 * x_mean

    return b0, b1


def create_plots(x, y, x_col, y_col, b0, b1):
    "Создание интерактивных графиков"
    fig = make_subplots(rows=1, cols=3, subplot_titles=(
        'Исходные данные',
        'Линейная регрессия',
        'Квадраты ошибок'
    ))

    # 1. Исходные данные
    fig.add_trace(
        go.Scatter(x=x, y=y, mode='markers', name='Данные'),
        row=1, col=1
    )

    # 2. Регрессионная прямая
    y_pred = b0 + b1 * x
    fig.add_trace(
        go.Scatter(x=x, y=y, mode='markers', name='Данные'),
        row=1, col=2
    )
    fig.add_trace(
        go.Scatter(x=x, y=y_pred, mode='lines', name='Регрессия'),
        row=1, col=2
    )

    # 3. Квадраты ошибок
    fig.add_trace(
        go.Scatter(x=x, y=y, mode='markers', name='Данные'),
        row=1, col=3
    )
    fig.add_trace(
        go.Scatter(x=x, y=y_pred, mode='lines', name='Регрессия'),
        row=1, col=3
    )

    # Добавляем квадраты ошибок
    for xi, yi, ypi in zip(x, y, y_pred):
        if yi > ypi:
            fig.add_shape(
                type="rect",
                x0=xi - 0.05, x1=xi + 0.05,
                y0=ypi, y1=yi,
                fillcolor="green",
                opacity=0.2,
                line_width=0,
                row=1, col=3
            )
        else:
            fig.add_shape(
                type="rect",
                x0=xi - 0.05, x1=xi + 0.05,
                y0=yi, y1=ypi,
                fillcolor="green",
                opacity=0.2,
                line_width=0,
                row=1, col=3
            )

    fig.update_layout(
        height=500,
        width=1500,
        showlegend=False,
        xaxis_title=x_col,
        yaxis_title=y_col,
        xaxis2_title=x_col,
        yaxis2_title=y_col,
        xaxis3_title=x_col,
        yaxis3_title=y_col
    )

    return fig


def main():
    filename = input("Введите имя CSV-файла: ")
    data = read_data(filename)

    print("Доступные столбцы:", list(data.columns))
    x_col = input("Выберите столбец для X: ")
    y_col = input("Выберите столбец для Y: ")

    x = data[x_col].values
    y = data[y_col].values

    show_statistics(data[[x_col, y_col]], x_col, y_col)
    b0, b1 = linear_regression(x, y)
    print(f"\nУравнение регрессионной прямой: y = {b0:.2f} + {b1:.2f}x")

    fig = create_plots(x, y, x_col, y_col, b0, b1)
    fig.show()


if __name__ == "__main__":
    main()