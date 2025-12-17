import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelBinarizer
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns


class SigmoidActivation:
    @staticmethod
    def function(x):
        return 1 / (1 + np.exp(-np.clip(x, -100, 100)))

    @staticmethod
    def derivative(x):
        sigmoid = SigmoidActivation.function(x)
        return sigmoid * (1 - sigmoid)


class Neuron:
    def __init__(self, input_size, learning_rate=0.01):
        self.weights = np.random.randn(input_size) * 0.1
        self.bias = np.random.randn() * 0.1
        self.learning_rate = learning_rate
        self.last_input = None
        self.last_output = None
        self.delta = None

    def forward(self, x):
        self.last_input = x
        z = np.dot(x, self.weights) + self.bias
        self.last_output = SigmoidActivation.function(z)
        return self.last_output

    def backward(self, error):
        grad = error * SigmoidActivation.derivative(
            np.dot(self.last_input, self.weights) + self.bias
        )
        self.delta = grad
        self.weights -= self.learning_rate * grad * self.last_input
        self.bias -= self.learning_rate * grad
        return grad * self.weights


class Layer:
    def __init__(self, input_size, num_neurons, learning_rate=0.01):
        self.neurons = [Neuron(input_size, learning_rate) for _ in range(num_neurons)]
        self.last_input = None
        self.last_output = None

    def forward(self, x):
        self.last_input = x
        outputs = [neuron.forward(x) for neuron in self.neurons]
        self.last_output = np.array(outputs)
        return self.last_output

    def backward(self, errors):
        weight_gradients = []
        for i, neuron in enumerate(self.neurons):
            grad = neuron.backward(errors[i])
            weight_gradients.append(grad)
        return np.sum(weight_gradients, axis=0)


class NeuralNetwork:
    def __init__(self, layer_sizes, learning_rate=0.01):
        self.layers = []
        for i in range(len(layer_sizes) - 1):
            layer = Layer(layer_sizes[i], layer_sizes[i + 1], learning_rate)
            self.layers.append(layer)

    def forward(self, x):
        current_input = x
        for layer in self.layers:
            current_input = layer.forward(current_input)
        return current_input

    def backward(self, error):
        current_error = error
        for layer in reversed(self.layers):
            current_error = layer.backward(current_error)

    def train(self, X, y, epochs=1000):
        losses = []
        for epoch in range(epochs):
            total_loss = 0
            for i in range(len(X)):
                output = self.forward(X[i])
                error = output - y[i]
                self.backward(error)
                total_loss += np.mean(error ** 2)
            losses.append(total_loss / len(X))
            if epoch % 100 == 0:
                print(f"Epoch {epoch}, Loss: {losses[-1]:.4f}")
        return losses


def load_and_prepare_data():
    iris = load_iris()
    X = iris.data[:, :2]
    y = iris.target

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    lb = LabelBinarizer()
    y_binary = lb.fit_transform(y)

    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y_binary, test_size=0.2, random_state=42, stratify=y
    )

    return X_train, X_test, y_train, y_test, X_scaled, y, scaler


def train_single_neuron(X_train, y_train):
    network = NeuralNetwork([2, 3], learning_rate=0.1)
    losses = network.train(X_train, y_train, epochs=1000)
    return network, losses


def train_two_layer_network(X_train, y_train):
    network = NeuralNetwork([2, 10, 3], learning_rate=0.1)
    losses = network.train(X_train, y_train, epochs=1000)
    return network, losses


def evaluate_model(model, X_test, y_test):
    predictions = []
    for x in X_test:
        output = model.forward(x)
        predictions.append(np.argmax(output))

    y_true = np.argmax(y_test, axis=1)
    accuracy = accuracy_score(y_true, predictions)

    print(f"Accuracy: {accuracy:.4f}")
    print("\nClassification Report:")
    print(classification_report(y_true, predictions, target_names=load_iris().target_names))

    cm = confusion_matrix(y_true, predictions)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                xticklabels=load_iris().target_names,
                yticklabels=load_iris().target_names)
    plt.title('Confusion Matrix')
    plt.ylabel('True Label')
    plt.xlabel('Predicted Label')
    plt.tight_layout()
    plt.show()

    return predictions, accuracy


def plot_decision_boundary(model, X, y, title, scaler):
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02),
                         np.arange(y_min, y_max, 0.02))

    grid_scaled = scaler.transform(np.c_[xx.ravel(), yy.ravel()])

    Z = []
    for point in grid_scaled:
        output = model.forward(point)
        Z.append(np.argmax(output))
    Z = np.array(Z).reshape(xx.shape)

    plt.figure(figsize=(10, 8))
    plt.contourf(xx, yy, Z, alpha=0.8, cmap=plt.cm.RdYlBu)
    scatter = plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k', cmap=plt.cm.RdYlBu)
    plt.xlabel('Sepal Length')
    plt.ylabel('Sepal Width')
    plt.title(title)
    plt.legend(handles=scatter.legend_elements()[0],
               labels=load_iris().target_names.tolist())
    plt.colorbar(scatter)
    plt.tight_layout()
    plt.show()


def main():
    X_train, X_test, y_train, y_test, X_scaled, y, scaler = load_and_prepare_data()

    print("=" * 60)
    print("1. Один нейрон (один слой)")
    print("=" * 60)
    single_neuron_model, losses1 = train_single_neuron(X_train, y_train)

    plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
    plt.plot(losses1)
    plt.title('Loss - Один нейрон')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')

    predictions1, acc1 = evaluate_model(single_neuron_model, X_test, y_test)
    plot_decision_boundary(single_neuron_model, X_scaled, y,
                           'Decision Boundary - Один нейрон', scaler)

    print("\n" + "=" * 60)
    print("2. Нейросеть из 2 слоев (10 нейронов в скрытом слое)")
    print("=" * 60)
    two_layer_model, losses2 = train_two_layer_network(X_train, y_train)

    plt.subplot(1, 2, 2)
    plt.plot(losses2)
    plt.title('Loss - Два слоя')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.tight_layout()
    plt.show()

    predictions2, acc2 = evaluate_model(two_layer_model, X_test, y_test)
    plot_decision_boundary(two_layer_model, X_scaled, y,
                           'Decision Boundary - Два слоя', scaler)

    print("\n" + "=" * 60)
    print("Сравнение моделей")
    print("=" * 60)
    print(f"Один нейрон: Accuracy = {acc1:.4f}")
    print(f"Два слоя: Accuracy = {acc2:.4f}")

    print("\nРазница в accuracy: {:.4f}".format(acc2 - acc1))
    if acc2 > acc1:
        print("Нейросеть с двумя слоями показала лучший результат.")
    elif acc1 > acc2:
        print("Один нейрон показал лучший результат.")
    else:
        print("Модели показали одинаковый результат.")


if __name__ == "__main__":
    main()