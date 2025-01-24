/*Дана последовательность чисел. Отсортировать и вывести последовательность чисел,
определённым методом. Метод: Пузырек*/

#include <iostream>

int main() {
    int n, temp;
    std::cout << "n = "; //количество чисел
    std::cin >> n;
    int arr[n]; //создание массива нужного размера
    std::cout << "enter numbers: ";
    for(int i = 0; i < n; i++) {
        std::cin >> arr[i];
    }
    for(int i = 0; i < n-1; i++) {
        for(int j = 0; j < n-i-1; j++) {
            if(arr[j] > arr[j+1]) {
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
    for(int i = 0; i < n; i++) {
        std::cout << arr[i] << " ";
    }
    return 0;
}
