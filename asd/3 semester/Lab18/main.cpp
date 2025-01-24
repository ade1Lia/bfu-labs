#include <iostream>
#include <vector>

class Tree
{
public:
    int value;
    Tree* left;
    Tree* right;
    Tree(int value)
    {
        this->value = value;
        this->left = nullptr;
        this->right = nullptr;
    }
};

Tree* insertElement(Tree* root, int value)
{
    if (root == nullptr)
    {
        return new Tree(value);
    }
    if (value < root->value)
    {
        root->left = insertElement(root->left, value);  //записываем в левого ребёнка, если меньше родителя
    }
    else
    {
        root->right = insertElement(root->right, value);    //записываем в правого ребёнка, если больше родителя
    }
    return root;
}

void centralPass(Tree* root, std::vector<int>& sortedArr)
{
    if (root)   //если есть ветвь, т.е. не nullptr
    {
        centralPass(root->left, sortedArr);
        sortedArr.push_back(root->value);
        centralPass(root->right, sortedArr);
    }
}

std::vector<int> sortBST(std::vector<int>& arr)
{
    Tree* root = nullptr;
    for (int value : arr)
    {
        root = insertElement(root, value);
    }
    std::vector<int> sorted_arr;
    centralPass(root, sorted_arr);
    return sorted_arr;
}

int main()
{
    std::vector<int> arr = { 5, 3, 8, 6, 2, 7, 1, 4, 9};    //наше дерево, записанное в массив
    std::vector<int> sortedArr = sortBST(arr);
    std::cout << "Sorted BST: \n";
    for (int value : sortedArr) {
        std::cout << value << " ";
    }
    return 0;
}
