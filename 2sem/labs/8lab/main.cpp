#include <iostream>

template<typename T>
class Stack {

private:
    size_t m_size = 0; // кол-во элементов
    size_t m_capacity; //размерность
    T* m_stack; //массив элементов

public:
    Stack(size_t size)
    {
        try
        {
            m_stack = new T[size];
            m_capacity = size;
        }
        catch (std::bad_alloc& e) {}
    }
    ~Stack()
    {
        delete[] m_stack;
    }
    size_t Size()
    {
        return m_size;
    }

    bool Empty()
    {
        return m_size == 0;
    }

    void Push(const T& element)
    {
        if (m_size == m_capacity)
        {
            throw std::overflow_error("Can't add new element");
        }
        m_stack[m_size] = element;
        m_size++;
    }

    void Pop(int index)
    {
        if (this->Empty())
            throw std::out_of_range("Stack is empty");
        for (int i = 0; i < m_size; i++)
        {
            if (i >= index)
            {
                m_stack[i] = m_stack[i + 1];
            }
        }
        m_size--;
    }

    T Top()
    {
        if (this->Empty())
            throw std::logic_error("Stack is empty");
        return m_stack[m_size - 1];
    }
};

int main()
{
    Stack<int> s(1);
    std::cout << "Size: " << s.Size() << std::endl;
    try
    {
        s.Push(5);
    }
    catch (const std::overflow_error& e)
    {
        std::cout << "Error: " << e.what() << std::endl;
    }

    try
    {
        s.Push(8);
    }
    catch (const std::overflow_error& e)
    {
        std::cout << "Error: " << e.what() << std::endl;
    }

    std::cout << "Top: " << s.Top() << std::endl;
    try
    {
        s.Pop(0);
    }
    catch (const std::out_of_range& e)
    {
        std::cout << "Error: " << e.what() << std::endl;
    }

    std::cout << "Size: " << s.Size() << std::endl;
    try
    {
        std::cout << s.Top() << std::endl;
    }
    catch (const std::logic_error& e)
    {
        std::cout << "Error: " << e.what() << std::endl;
    }
}