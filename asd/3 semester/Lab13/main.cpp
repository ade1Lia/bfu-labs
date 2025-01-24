#include <iostream>
#include <fstream>
#include <string>
#include <unordered_map>

// Функция ?хеширования/хешинга/хеш-чето-то-там?
int hashFunction(const std::string& key, int n)
{
    int sum = 0;
    for (char c : key)
        sum += c;
    return sum % n;  // Пример простой хеш-функции, которая делит сумму символов на 10 и возвращает остаток
}
int CountLinesInFile(const std::string& key)
{
    // Объявить экземпляр F, который связан с файлом filename.
    // Файл открывается для чтения в текстовом формате.
    std::ifstream F(key, std::ios::in);
    // Вычислить количество строк в файле
    int count = 0;
    char buffer[100000]; // буфер для сохранения одной строки

    // Цикл чтения строк.
    while (!F.eof())
    {
        count++;
        // Считать одну строку в буфер
        F.getline(buffer, 100000);
    }

    F.close();
    return count;
}

int main()
{
    std::ifstream inputFile("input.txt");  // Открываем входной файл для чтения
    std::ofstream outputFile("output.txt");  // Открываем выходной файл для записи
    if (!inputFile)
    {
        std::cout << "Error. We can't read the file.. :(" << std::endl;
        return 1;
    }
    std::unordered_map<int, std::string> hashTable;  // Создаем хеш-таблицу
    // Чтение текста из файла
    std::string line;
    int n = CountLinesInFile("input.txt");
    while (std::getline(inputFile, line))
    {
        // Наложение на хеш-таблицу
        int key = hashFunction(line,n);
        int c = 0;
        while (c == 0)
        {
            if (hashTable[key].empty())
            {
                hashTable[key] = line;
                c=1;
            }
            else
            {
                if (key<(n-1))
                    key += 1;
                else
                    key = 0;
            }

        }
    }
    // Запись хеш-таблицы в файл
    for (const auto& pair : hashTable)
        outputFile << pair.first << ": " << pair.second << std::endl;
    std::cout << "We have successfully written your wonderful, lovely, delicious hash table into a file output.txt" << std::endl;
    inputFile.close();  // Закрываем входной файл
    outputFile.close();  // Закрываем выходной файл
    return 0;
}
