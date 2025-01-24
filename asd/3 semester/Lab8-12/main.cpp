#include <iostream>
#include <algorithm>
void swap(int& a, int& b)
{
    int temp = a;
    a = b;
    b = temp;
}
class Sorting {
private:
public:

    //№8 Корневая
    int getMax(int arr[], int n)
    {
        int mx = arr[0];
        for (int i = 1; i < n; i++)
            if (arr[i] > mx)
                mx = arr[i];
        return mx;
    }
    //Считает появление той или иной цифры в каждом разряде и сортирует вспомогательный массив
    void countSort(int arr[], int n, int exp)
    {
        //Объявляем вспомогательный массив
        int output[n];
        int i, count[10] = {0};
        for (i = 0; i < n; i++)
            count[(arr[i] / exp) % 10]++;
        for (i = 1; i < 10; i++)
            count[i] += count[i - 1];
        //Заполняем вспомогательный массив
        for (i = n - 1; i >= 0; i--) {
            output[count[(arr[i] / exp) % 10] - 1] = arr[i];
            count[(arr[i] / exp) % 10]--;
        }
        //Запихиваем вспомогательный массив в изначальный
        for (i = 0; i < n; i++)
            arr[i] = output[i];
    }
    //Сама сортировка
    void radixSort(int arr[], int n)
    {
        int m = getMax(arr, n);
        for (int exp = 1; m / exp > 0; exp *= 10)
            countSort(arr, n, exp);
    }

    //№9 Пирамидальная

    // Функция для создания кучи (heap) заданного размера
    void heapCreation(int arr[], int n, int i) {
        int largest = i; //Наибольший элемент кучи - корень дерева
        int left = 2 * i + 1; //Левый потомок
        int right = 2 * i + 2; //Правый потомок
        //Если левый потомок больше корня, он становится корнем
        if (left < n && arr[left] > arr[largest]) {
            largest = left;
        }
        // Если правый потомок больше, чем самый большой элемент на данный момент, он становится им
        if (right < n && arr[right] > arr[largest]) {
            largest = right;
        }
        // Если наибольший элемент не корень, делаем, чтоб это было так
        if (largest != i) {
            swap(arr[i], arr[largest]);
            // Рекурсивно строим кучу для поддерева
            (arr, n, largest);
        }
    }

    //Сама функция пирамидальной сортировки (сортировки с использованием хипа
    void heapSort(int arr[], int n) {
        //Построение кучи (по-сути, уже перегруппировка массива)
        for (int i = n / 2 - 1; i >= 0; i--) {
            heapCreation(arr, n, i);
        }
        // Извлекаем элементы по одному из кучи
        for (int i = n - 1; i >= 0; i--) {
            // Перемещаем текущий корень в конец
            swap(arr[0], arr[i]);
            // Вызываем ту же процедуру на уменьшенной куче
            heapCreation(arr, i, 0);
        }
    }
    //№10 Слиянием

    // Функция для слияния двух отсортированных массивов
    void merge(int arr[], int l, int m, int r)
    {
        int i, j, k;
        int n1 = m - l + 1;
        int n2 = r - m;
        // Создаем временные массивы
        int L[n1], R[n2];
        // Копируем данные во временные массивы
        for (i = 0; i < n1; i++)
            L[i] = arr[l + i];
        for (j = 0; j < n2; j++)
            R[j] = arr[m + 1 + j];
        // Слияние временных массивов обратно в arr[l..r]
        i = 0; // Индекс первого подмассива
        j = 0; // Индекс второго подмассива
        k = l; // Индекс объединенного подмассива
        while (i < n1, j < n2)
        {
            if (L[i] <= R[j])
            {
                arr[k] = L[i];
                i++;
            }
            else
            {
                arr[k] = R[j];
                j++;
            }
            k++;
        }
        // Копирование оставшихся элементов L[], если они есть
        while (i < n1) {
            arr[k] = L[i];
            i++;
            k++;
        }
        // Копирование оставшихся элементов R[], если они есть
        while (j < n2)
        {
            arr[k] = R[j];
            j++;
            k++;
        }
    }
// Основная функция, которая сортирует arr[l..r] с использованием merge()
    void mergeSort(int arr[], int l, int r)
    {
        if (l < r)
        {
            // Найдем среднюю точку
            int m = l + (r - l) / 2;
            // Сортируем первую и вторую половины
            mergeSort(arr, l, m);
            mergeSort(arr, m + 1, r);
            // Объединяем отсортированные половины
            merge(arr, l, m, r);
        }
    }

    //№11 Быстрая
    void quickSort(int arr[], int left, int right, int n)
{
    int i = left ; //Первый элемент массива
    int j = right; //Последний элемент массива
    int pivot = arr[(left + right) / 2]; //Средний элемент массива
    while (i <= j)
    {
        while (arr[i] < pivot) //Пока элемент из правой части меньше среднего, идём дальше
        {
            i++;
        }
        while (arr[j] > pivot) //Пока элемент из левой части больше среднего, идём дальше
        {
            j--;
        }
        if (i <= j) //Mеняем местами элементы, которые не прошли проверку))
        {
            swap(arr[i], arr[j]);
            i++;
            j--;
        }
    }//Потом функция вызывает саму себя для каждой из двух частей
    if (left < j)
    {
        quickSort(arr, left, j, n);
    }
    if (i < right)
    {
        quickSort(arr, i, right, n);
    }
}
    //№12 Внешняя многофазная

//Функция для разделения входного массива на подмассивы и их сортировки
    void externalSort(int* arr, int size, int chunkSize)
    {
        int numChunks = (size + chunkSize - 1) / chunkSize; //вычисление количества частей, на которые будет разделен исходный массив
        int* result = new int[size];                        //временный массив для отсортированных элементов
        int* index = new int[numChunks];                    //временныймассив индексов для хранения текущей позиции в каждой части
        //Сортировка каждой части
        for (int i = 0; i < size; i += chunkSize)
        {
            std::sort(arr + i, arr + std::min(i + chunkSize, size));
        }
        // Установка начальных позиций для каждой части в массиве индексов
        for (int i = 0; i < numChunks; i++)
        {
            index[i] = i * chunkSize;
        }

        for (int i = 0; i < size; i++)
        {
            int minIndex = -1;
            for (int j = 0; j < numChunks; j++)
            {//Если текущий элемент в части не превышает границы этой части и его значение меньше значения минимального элемента
                if (index[j] < (j + 1) * chunkSize && (minIndex == -1 || arr[index[j]] < arr[index[minIndex]]))
                {//Обновляем индекс части с минимальным текущим элементом
                    minIndex = j;
                }
            }
            result[i] = arr[index[minIndex]];
            index[minIndex]++;
        }
        //Копируем отсортированные элементы из временного массива в исходный
        for (int i = 0; i < size; i++)
        {
            arr[i] = result[i];
        }
    }
};

int main()
{
    int sizeOfYou;
    std::cout << "What number of elements do you want?" << std::endl;
    std::cin >> sizeOfYou;
    const int size = sizeOfYou;
    int mass[size];
    std::cout << "Enter your lovely " << size << " character array." << std::endl;
    for (int i = 0; i < size; i++)
    {
        std::cin >> mass[i];
    }
    Sorting test;
    //test.bubbleSort(mass, size);
    //test.insertionSort(mass, size);
    //test.selectionSort(mass, size);
    //test.shellSort(mass, size);
    //test.radixSort(mass, size);
    //test.heapSort(mass, size);
    //test.mergeSort(mass, size); (№10 Слиянием)
    //test.quickSort(mass, 0, size-1, size);
    //test.externalSort(mass,size,5); (№12 Внешняя многофазная)
    std::cout << "Here is your delicious sorted array:" << std::endl;
    for (int i = 0; i < size; i++)
    {
        std::cout << mass[i] << " ";
    }
    return 0;
}
