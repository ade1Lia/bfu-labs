/*Лаба №1 "Задача о скобках"
На вход подаётся строка, состоящая из скобок. Программа должна определить
правильность введённого скобочного выражения. Савкин сказал, что программа должна
работать на русском языке: "Введите строку", "Строка не существует", "Строка существует"
и т.п.
В строке будут все три вида скобок
Пример входа:
()[({}())]*/

#include <iostream>
#include <stack>
#include <string>
//#include <locale.h>

class ChekBrckt {
private:
    std::stack<char> brckt;
public:
    bool check(std::string str) {
        for (char brck : str) {
            if (brck == '(' || brck == '{' || brck == '[') {
                brckt.push(brck); //добавление скобки в стек
            }
            else if (brck == ')' || brck == '}' || brck == ']') {
                if (brckt.empty()) {
                    return false;
                }
                char top = brckt.top(); //верхний элемент
                brckt.pop(); //удаляем его из стека
                if ((top == '(' && brck != ')') || (top == '[' && brck != ']') || (top == '{' && brck != '}') || (top == '<' && brck != '>')) {
                    return false;
                }
            }
        }
        return brckt.empty();
    }
};

int main() {
    //setlocale(LC_ALL, "Rus");
    std::string str;
    std::cout << "Enter the string" << std::endl;
    std::cin >> str;
    ChekBrckt checker;
    if (checker.check(str)) {
        std::cout << "Row exist" << std::endl;
    }
    else {
        std::cout << "Row does not exist" << std::endl;
    }
    return 0;
}
