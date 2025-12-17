import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
import torch.nn.functional as F


def load_mnist_data():
    print("Загрузка данных MNIST...")
    mnist = fetch_openml('mnist_784', version=1, parser='auto')
    X = mnist.data.astype('float32') / 255.0
    y = mnist.target.astype('int64')

    X_train_full = X[:60000]
    y_train_full = y[:60000]
    X_test = X[60000:70000]
    y_test = y[60000:70000]

    X_train, X_val, y_train, y_val = train_test_split(
        X_train_full, y_train_full, test_size=5000, random_state=42
    )

    print(f"Данные загружены: {X_train.shape[0]} обучающих, {X_val.shape[0]} валидационных, {X_test.shape[0]} тестовых")
    return X_train, X_val, X_test, y_train, y_val, y_test


class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(1, 8, kernel_size=3, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(8, 16, kernel_size=3, padding=1)
        self.fc1 = nn.Linear(16 * 7 * 7, 64)
        self.fc2 = nn.Linear(64, 10)
        self.dropout = nn.Dropout(0.25)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 16 * 7 * 7)
        x = self.dropout(x)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return F.log_softmax(x, dim=1)


def train_mlp_model(X_train, X_val, X_test, y_train, y_val, y_test):
    print("\nОбучение MLP...")
    mlp = MLPClassifier(
        hidden_layer_sizes=(256, 128),
        activation='relu',
        solver='adam',
        max_iter=100,
        random_state=42,
        verbose=True,
        batch_size=256,
        learning_rate_init=0.001,
        alpha=0.0001,
        early_stopping=True,
        validation_fraction=0.1,
        n_iter_no_change=10
    )
    mlp.fit(X_train, y_train)

    train_pred = mlp.predict(X_train)
    val_pred = mlp.predict(X_val)
    test_pred = mlp.predict(X_test)

    train_acc = accuracy_score(y_train, train_pred)
    val_acc = accuracy_score(y_val, val_pred)
    test_acc = accuracy_score(y_test, test_pred)

    print(f"Точность MLP - Обучающая: {train_acc:.4f}, Валидационная: {val_acc:.4f}, Тестовая: {test_acc:.4f}")

    return test_pred, mlp.loss_curve_


def train_cnn_model(X_train, X_val, X_test, y_train, y_val, y_test):
    print("\nОбучение CNN...")

    X_train_tensor = torch.FloatTensor(X_train.values.reshape(-1, 1, 28, 28))
    X_val_tensor = torch.FloatTensor(X_val.values.reshape(-1, 1, 28, 28))
    X_test_tensor = torch.FloatTensor(X_test.values.reshape(-1, 1, 28, 28))

    y_train_tensor = torch.LongTensor(y_train.values)
    y_val_tensor = torch.LongTensor(y_val.values)
    y_test_tensor = torch.LongTensor(y_test.values)

    train_dataset = TensorDataset(X_train_tensor, y_train_tensor)
    val_dataset = TensorDataset(X_val_tensor, y_val_tensor)
    test_dataset = TensorDataset(X_test_tensor, y_test_tensor)

    train_loader = DataLoader(train_dataset, batch_size=128, shuffle=True, num_workers=0)
    val_loader = DataLoader(val_dataset, batch_size=500, shuffle=False)
    test_loader = DataLoader(test_dataset, batch_size=1000, shuffle=False)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Используется устройство: {device}")

    model = SimpleCNN().to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)

    train_losses = []
    val_accuracies = []

    for epoch in range(10):
        model.train()
        running_loss = 0.0
        for i, (data, target) in enumerate(train_loader):
            if i % 200 == 0:
                print(f"Эпоха {epoch + 1}, батч {i}/{len(train_loader)}")

            data, target = data.to(device), target.to(device)

            optimizer.zero_grad()
            output = model(data)
            loss = criterion(output, target)
            loss.backward()
            optimizer.step()

            running_loss += loss.item()

        epoch_loss = running_loss / len(train_loader)
        train_losses.append(epoch_loss)

        model.eval()
        val_correct = 0
        val_total = 0
        with torch.no_grad():
            for data, target in val_loader:
                data, target = data.to(device), target.to(device)
                output = model(data)
                _, predicted = torch.max(output.data, 1)
                val_total += target.size(0)
                val_correct += (predicted == target).sum().item()

        val_acc = 100 * val_correct / val_total
        val_accuracies.append(val_acc)

        print(f"Эпоха {epoch + 1}, Loss: {epoch_loss:.4f}, Val Accuracy: {val_acc:.2f}%")

    model.eval()
    cnn_pred = []
    test_correct = 0
    test_total = 0

    with torch.no_grad():
        for data, target in test_loader:
            data = data.to(device)
            output = model(data)
            _, predicted = torch.max(output.data, 1)
            cnn_pred.extend(predicted.cpu().numpy())
            test_total += target.size(0)
            test_correct += (predicted.cpu() == target).sum().item()

    test_acc = 100 * test_correct / test_total
    print(f"Точность CNN на тесте: {test_acc:.2f}%")

    return np.array(cnn_pred), train_losses, val_accuracies


def main():
    X_train, X_val, X_test, y_train, y_val, y_test = load_mnist_data()

    mlp_pred, mlp_losses = train_mlp_model(X_train, X_val, X_test, y_train, y_val, y_test)
    cnn_pred, cnn_losses, cnn_val_acc = train_cnn_model(X_train, X_val, X_test, y_train, y_val, y_test)

    print("\n" + "=" * 60)
    print("ИТОГОВЫЕ РЕЗУЛЬТАТЫ")
    print("=" * 60)

    mlp_accuracy = accuracy_score(y_test, mlp_pred)
    cnn_accuracy = accuracy_score(y_test, cnn_pred)

    print(f"\nMLP (scikit-learn):")
    print(f"  Точность: {mlp_accuracy:.4f}")

    print(f"\nCNN (PyTorch):")
    print(f"  Точность: {cnn_accuracy:.4f}")

    print(f"\nРазница (CNN - MLP): {cnn_accuracy - mlp_accuracy:.4f}")

    print("\n" + "=" * 60)
    print("СРАВНИТЕЛЬНЫЙ АНАЛИЗ")
    print("=" * 60)

    print("\nОтчет по классификации MLP:")
    print(classification_report(y_test, mlp_pred, digits=4))

    print("\nОтчет по классификации CNN:")
    print(classification_report(y_test, cnn_pred, digits=4))

    print("\n" + "=" * 60)
    print("ВЫВОДЫ")
    print("=" * 60)
    print("""
1. CNN показывает более высокую точность благодаря:
   - Использованию сверточных слоев для извлечения пространственных признаков
   - Инвариантности к малым трансформациям изображений
   - Более эффективной архитектуре для работы с изображениями

2. MLP проще в реализации и быстрее обучается, но:
   - Теряет пространственную информацию при flattening
   - Требует больше параметров для аналогичной точности
   - Менее эффективен для задач компьютерного зрения

Для классификации изображений использовать CNN
Для табличных данных можно использовать MLP
CNN лучше справляется с обобщением на новых данных
""")

    fig, axes = plt.subplots(2, 3, figsize=(15, 10))

    axes[0, 0].plot(mlp_losses)
    axes[0, 0].set_title('MLP: Кривая обучения')
    axes[0, 0].set_xlabel('Итерация')
    axes[0, 0].set_ylabel('Loss')
    axes[0, 0].grid(True)

    axes[0, 1].plot(cnn_losses)
    axes[0, 1].set_title('CNN: Loss по эпохам')
    axes[0, 1].set_xlabel('Эпоха')
    axes[0, 1].set_ylabel('Loss')
    axes[0, 1].grid(True)

    axes[0, 2].plot(cnn_val_acc)
    axes[0, 2].set_title('CNN: Точность на валидации')
    axes[0, 2].set_xlabel('Эпоха')
    axes[0, 2].set_ylabel('Accuracy (%)')
    axes[0, 2].grid(True)

    cm_mlp = confusion_matrix(y_test, mlp_pred)
    sns.heatmap(cm_mlp, annot=True, fmt='d', ax=axes[1, 0], cmap='Blues', cbar=False)
    axes[1, 0].set_title('MLP: Матрица ошибок')
    axes[1, 0].set_xlabel('Предсказанный класс')
    axes[1, 0].set_ylabel('Истинный класс')

    cm_cnn = confusion_matrix(y_test, cnn_pred)
    sns.heatmap(cm_cnn, annot=True, fmt='d', ax=axes[1, 1], cmap='Blues', cbar=False)
    axes[1, 1].set_title('CNN: Матрица ошибок')
    axes[1, 1].set_xlabel('Предсказанный класс')
    axes[1, 1].set_ylabel('Истинный класс')

    axes[1, 2].bar(['MLP', 'CNN'], [mlp_accuracy, cnn_accuracy])
    axes[1, 2].set_title('Сравнение точности')
    axes[1, 2].set_ylabel('Accuracy')
    axes[1, 2].set_ylim([0.9, 1.0])
    axes[1, 2].grid(True, axis='y')

    for i, (model_name, acc) in enumerate([('MLP', mlp_accuracy), ('CNN', cnn_accuracy)]):
        axes[1, 2].text(i, acc + 0.005, f'{acc:.4f}', ha='center')

    plt.tight_layout()
    plt.savefig('mnist_comparison.png', dpi=100, bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    main()