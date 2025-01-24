#include <iostream>
#include <stack>
#include <string>

using namespace std;
bool function(std::string str) // проверка на скобки
{
    stack<char> st;
    for (char ch : str)
    {
        if (ch == '(' || ch == '{' || ch == '[')
        {
            st.push(ch);
        }
        else if (ch == ')' || ch == '}' || ch == ']')
        {
            if (st.empty())
            {
                return false;
            }
            else if ((ch == ')' && st.top() != '(') ||
                     (ch == '}' && st.top() != '{') ||
                     (ch == ']' && st.top() != '['))
            {
                return false;
            }
            st.pop();
        }
    }
    return st.empty();
}
std::string length(std::string str, int& j)
{
    std::string len;
    for (int i = j; (str[i] >= '0') && (str[i] <= '9'); i++)
    {
        len += str[i];
        j++;
    }
    j--;
    return len;
}
bool ravno(std::string str)// проверка на равно
{
    if (str[str.size() - 1] == '=')
        return 1;
    else
        return 0;
}
int count(std::string str) // подсчитываем выражение
{
    std::stack <std::string> numbers;
    std::stack <char> elements;
    int a = 0;
    int b = 0;
    str += '=';
    for (int i = 0; str[i] != '='; i++)
    {
        if (str[i] != '+' && str[i] != '-' && str[i] != '/' && str[i] != '*' && str[i] != '(' && str[i] != ')' && str[i] != '{' && str[i] != '}' && str[i] != '[' && str[i] != ']')
        {
            numbers.push(length(str, i));
        }

        if (str[i] == '+' || str[i] == '-' || str[i] == '/' || str[i] == '*')
        {
            if (!elements.empty())
            {
                if ((str[i] == '*' || str[i] == '/') && (elements.top() == '*' || elements.top() == '/') && numbers.size() >= 2)
                {
                    b = stoi(numbers.top());
                    numbers.pop();
                    a = stoi(numbers.top());
                    numbers.pop();
                    if (b == '0' && elements.top() == '/')
                    {
                        std::cout << " !!! ZERO !!! ";
                        return 0;
                    }
                    if (elements.top() == '/')
                    {
                        numbers.push(std::to_string(a / b));
                    }
                    if (elements.top() == '*')
                    {
                        numbers.push(std::to_string(a * b));
                    }
                    elements.pop();
                }
            }
            if (!elements.empty())
            {
                if ((str[i] == '+' || str[i] == '-') && (elements.top() == '+' || elements.top() == '-') && numbers.size() >= 2)
                {
                    b = stoi(numbers.top());
                    numbers.pop();
                    a = stoi(numbers.top());
                    numbers.pop();
                    if (elements.top() == '+') { numbers.push(std::to_string(a + b)); }
                    if (elements.top() == '-') { numbers.push(std::to_string(a - b)); }
                }
            }
        }
        if (str[i] == '(')
        {
            std::string str2;
            int left_boarder = 1;
            int right_boarder = 0;
            for (int j = i + 1; left_boarder != right_boarder; j++)
            {
                str2 += str[j];
                if (str[j] == '(')
                    left_boarder += 1;
                if (str[j] == ')')
                    right_boarder += 1;
                i++;
            }
            str2.pop_back();
            numbers.push(std::to_string(count(str2)));
        }
        if (str[i] == '{')
        {
            std::string str2;
            int left_boarder = 1;
            int right_boarder = 0;
            for (int j = i + 1; left_boarder != right_boarder; j++)
            {
                str2 += str[j];
                if (str[j] == '{')
                    left_boarder += 1;
                if (str[j] == '}')
                    right_boarder += 1;
                i++;
            }
            if (str[i] == '[')
            {
                std::string str2;

                int left_boarder = 1;
                int right_boarder = 0;
                for (int j = i + 1; left_boarder != right_boarder; j++)
                {
                    str2 += str[j];
                    if (str[j] == '[')
                        left_boarder += 1;
                    if (str[j] == ']')
                        right_boarder += 1;
                    i++;
                }
                str2.pop_back();
                numbers.push(std::to_string(count(str2)));
            }
            str2.pop_back();
            numbers.push(std::to_string(count(str2)));
        }
        if (!elements.empty())
        {
            if ((str[i] == '/' || str[i] == '*') && (elements.top() == '/' || elements.top() == '*'))
            {
                b = stoi(numbers.top());
                numbers.pop();
                a = stoi(numbers.top());
                numbers.pop();
                // проверка деления на 0
                if (b == '0' && elements.top() == '/')
                {
                    std::cout << " !!! ZERO !!! ";
                    return 0;
                }
                if (elements.top() == '/' && b != '0') { numbers.push(std::to_string(a / b)); }
                if (elements.top() == '*') { numbers.push(std::to_string(a * b)); }
                elements.pop();
                elements.push(str[i]);
            }
            if ((str[i] == '/' || str[i] == '*') && (elements.top() == '+' || elements.top() == '-')) { elements.push(str[i]); }
            if ((str[i] == '+' || str[i] == '-') && (elements.top() != '/' && elements.top() != '*')) { elements.push(str[i]); }
        }
        if ((elements.empty() && (str[i] < '0' || str[i]>'9')) && str[i] != ')' && str[i] != '}' && str[i] != ']') { elements.push(str[i]); }
    }
    while (!elements.empty() && numbers.size() >= 2)
    {
        b = stoi(numbers.top());
        numbers.pop();
        a = stoi(numbers.top());
        numbers.pop();
        if (b == 0 && elements.top() == '/')      // проверка деления на 0
        {
            std::cout << " !!! ZERO !!! ";
            return 0;
        }
        if (elements.top() == '/' && b != '0') { numbers.push(std::to_string(a / b));}
        if (elements.top() == '*') { numbers.push(std::to_string(a * b)); }
        if (elements.top() == '+') { numbers.push(std::to_string(a + b)); }
        if (elements.top() == '-') { numbers.push(std::to_string(a - b)); }
        elements.pop();
    }
    return stoi(numbers.top());
}
int main()
{
    std::string stroka;
    std::cin >> stroka;
    if (ravno(stroka) && function(stroka))
        std::cout << "Result = " << count(stroka);
    else
        std::cout << "neravno or problems with ()[]{}";
    return 0;
}
