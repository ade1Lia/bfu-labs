/*Дана последовательность чисел. Отсортировать и вывести последовательность чисел,
определённым методом. Метод: Вставками*/

#include <iostream>

void Sort(int arr[], int n) {
    int i, key, j;
    for (i = 1; i < n; i++) {
        key = arr[i];
        j = i - 1;
        while (j >= 0 && arr[j] < key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}

int main() {
    int n, i;
    std::cout << "Enter the number of elements: ";
    std::cin >> n;
    int arr[n];
    std::cout << "Enter elements: ";
    for (i = 0; i < n; i++)
        std::cin >> arr[i];
    Sort(arr, n);
    std::cout << "Sorted array: ";
    for (i = 0; i < n; i++)
        std::cout << arr[i] << " ";

    return 0;
}