/*Дана последовательность чисел. Отсортировать и вывести последовательность чисел,
определённым методом. Метод: Посредством выбора*/


#include <iostream>

void Sort(int arr[], int n) {
    int i, j, min_idx;
    for (i = 0; i < n-1; i++) {
        min_idx = i;
        for (j = i+1; j < n; j++)
            if (arr[j] < arr[min_idx])
                min_idx = j;
        std::swap(arr[min_idx], arr[i]);
    }
}

int main() {
    int n, i;
    std::cout << "Enter the number of elements: ";
    std::cin >> n;
    int arr[n];
    std::cout << "Enter elements:" << std::endl;
    for(i = 0; i < n; i++)
        std::cin >> arr[i];
    Sort(arr, n);
    std::cout << "Sorted array: " << std::endl;
    for(i = 0; i < n; i++)
        std::cout << arr[i] << " ";
    return 0;
}