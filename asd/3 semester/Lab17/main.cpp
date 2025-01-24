#include <iostream>
#include <fstream>
#include <string>
#include <stack>

struct Elem
{
    int data;
    int level;
    Elem* left;
    Elem* right;
    Elem* parent;
};
//Создание элемента
Elem* MAKE(int data, Elem* p)
{
    Elem* q = new Elem;
    q->data = data;
    q->left = nullptr;
    q->right = nullptr;
    q->parent = p;
    return q;
}
//Добавление элемента в дерево
void ADD(int data, Elem*& root)
{
    if (root == nullptr)
    {
        root = MAKE(data, nullptr);
        return;
    }
    Elem* v = root;
    while ((data < v->data && v->left != nullptr) || (data > v->data && v->right != nullptr))
    {
        if (data < v->data)
            v = v->left;
        else
            v = v->right;
    }
    if (data == v->data)
        return;
    Elem* u = MAKE(data, v);
    if (data < v->data)
        v->left = u;
    else if (data > v->data)
        v->right = u;
}
//Проход по дереву
void PASS(Elem* v)
{
    if (v == nullptr)
        return;
    PASS(v->left);
    std::cout << v->data << " ";
    PASS(v->right);
}
//поиск в дереве элемента
Elem* SEARCH(int data, Elem* v)
{
    if (v == nullptr)
        return v;
    if (v->data == data)
        return v;
    if (data < v->data)
        return SEARCH(data, v->left);
    else  if (data > v->data)
        return SEARCH(data, v->right);
}
//удаление определенного элемента в дереве
void DELETE(int data, Elem*& root)
{
    Elem* u = SEARCH(data, root);
    if (u == nullptr)
        return;
    if (u->left == nullptr && u->right == nullptr && u == root)
    {
        delete root;
        root = nullptr;
        return;
    }
    if (u->left == nullptr && u->right != nullptr && u == root)
    {
        Elem* t = u->right;
        while (t->left != nullptr)
            t = t->left;
        u->data = t->data;
        u = t;
    }
    if (u->left != nullptr && u->right == nullptr && u == root)
    {
        Elem* t = u->left;
        while (t->right != nullptr)
            t = t->right;
        u->data = t->data;
        u = t;
    }
    if (u->left != nullptr && u->right != nullptr)
    {
        Elem* t = u->right;
        while (t->left != nullptr)
            t = t->left;
        u->data = t->data;
        u = t;
    }
    Elem* t;
    if (u->left == nullptr)
        t = u->right;
    else
        t = u->left;
    if (u->parent->left == u)
        u->parent->left = t;
    else
        u->parent->right = t;
    if (t != nullptr)
        t->parent = u->parent;
    delete u;
}
//Добавление скобочной записи в виде БДП (Бинарное дерево поиска)
void ADD_BY_PARENTHESIS(int data, Elem*& root, bool inLeft)
{
    Elem* v = root;
    Elem* u = MAKE(data, v);
    if (inLeft)
        v->left = u;
    else
        v->right = u;
}
//Заполнение дерева скобочной записью
void FILL_TREE(std::string& bracketEntry, int& i, Elem*& root)
{
    int value = 0;
    while (bracketEntry[i] != '\0')
    {
        switch (bracketEntry[i])
        {
            case '(':
            {
                i++;
                value = 0;
                while ((bracketEntry[i] >= '0') && (bracketEntry[i] <= '9'))
                {
                    value = value * 10 + bracketEntry[i] - '0';
                    i++;
                }
                if (value != 0)
                {
                    ADD_BY_PARENTHESIS(value, root, true);
                    if (bracketEntry[i] == '(')
                        FILL_TREE(bracketEntry, i, root->left);
                }
                value = 0;
                break;
            }
            case ',':
            {
                i++;
                value = 0;
                while ((bracketEntry[i] >= '0') && (bracketEntry[i] <= '9'))
                {
                    value = value * 10 + bracketEntry[i] - '0';
                    i++;
                }
                if (value != 0)
                {
                    ADD_BY_PARENTHESIS(value, root, false);
                    if (bracketEntry[i] == '(')
                        FILL_TREE(bracketEntry, i, root->right);
                }
                value = 0;
                break;
            }
            case ')':
                i++;
                return;
            default:
                break;
        }
    }
}

//Определение глубины элемента в дереве
int DEPTH(int data, Elem* v, int k)
{
    if (v == nullptr)
    {
        return -15;
    }
    if (v->data == data)
    {
        return k;
    }
    if (data < v->data)
        return DEPTH(data, v->left, k + 1);
    if (data > v->data)
        return DEPTH(data, v->right, k + 1);
}
//Очистка памяти, выделенной под дерево.
void CLEAR(Elem*& v) {
    if (v == nullptr)
        return;
    CLEAR(v->left);
    CLEAR(v->right);
    delete v;
    v = nullptr;
}
//Прямой рекурсивный обходик
void straightOrder(Elem* root)
{
    if (root == nullptr)
        return;
    std::cout << root->data << std::endl;
    straightOrder(root->left);
    straightOrder(root->right);
}
//Вывод элементов в консоль
void PRINT(Elem* root)
{
    if (root == nullptr)
    {
        std::cout << std::endl;
        return;
    }
    PRINT(root->right);
    for (int i = root->level; i > 0; i--)
    {
        std::cout << '\n';
    }
    std::cout << root->data << std::endl;
    PRINT(root->left);
}
void menu(Elem* root)
{
    std::cout << "This is the main menu, handsome. Welcome!" << std::endl;
    bool work = false;
    int action;
    while (!work)
    {
        std::cout << "Choose the surgery you need, dear: " << std::endl;
        std::cout << "Come in, welcome! (Addition) *click 1*\n"
                     "Get out! (Deletion) *click 2*\n"
                     "Where the hell is this? (Search) *click 3*\n"
                     "I'm getting the hell out of here.. (Exit) *click 4*" << std::endl;
        std::cin >> action;
        switch (action)
        {
            case 1:
            {
                int value;
                std::cout << "Enter the value to add: ";
                std::cin >> value;
                ADD(value, root);
                break;
            }
            case 2:
            {
                int value;
                std::cout << "Enter the value to erase: ";
                std::cin >> value;
                DELETE(value, root);
                break;
            }
            case 3:
            {
                int value;
                std::cout << "Enter the value you need to find: ";
                std::cin >> value;

                Elem* e = nullptr;
                e = SEARCH(value, root);
                if (e == nullptr)
                    std::cout << "He's not here. Are you sure that's where you put it?" << std::endl;
                else
                    std::cout << "Oh, yes, it's here.  It looks so cute in this tree, don't you think?" << std::endl;
                break;
            }
            case 4:
                work = true;
                break;
            default:
                break;
        }
    }
    //PRINT(root);
}

int main()
{
    Elem* root = nullptr;//начальное значение корня
    std::string bracketEntry;//создание скобочной записи
    std::cout << "Enter your line-bracket entry:" << std::endl;
    std::cin >> bracketEntry;
    int digit = 0;
    int i = 0;
    while ((bracketEntry[i] >= '0') && (bracketEntry[i] <= '9'))
    {
        digit += digit * 10 + bracketEntry[i] - '0';
        i++;
    }
    ADD(digit, root);
    FILL_TREE(bracketEntry, i, root);
    //PASS(root);
    std::cout << "----------" << std::endl;
    menu(root);
    straightOrder(root);
    CLEAR(root);
    std::cout << "I've put your tree on the screen for the last time. Bye-bye, honey *the name of the programmer*.. I'll miss you, come in and program some more." << std::endl;
    std::cout << "----------" << std::endl;
    return 0;
}

//8(3(1,6(4,7)),10(,14(13,))) - пример
