#include <iostream>
#include <cstring>

class String
{
private:
    size_t m_size;
    char* m_str;
public:
    //Базовые конструкторы
    String() : m_size(0), m_str(nullptr)
    {
        std::cout << "Basic constructor 1" << std::endl;
    };

    String(char c, size_t size) : m_size(size), m_str(new char[m_size+1])
    {
        std::cout << "Basic constructor 2" << std::endl;
        std::fill(m_str, m_str + m_size, c);
        m_str[m_size] = 0;
    }

    String(char* str) : m_size(sizeof(str)), m_str(new char[m_size+1])
    {
        std::cout << "Basic constructor 3" << std::endl;
        std::copy(str, str + m_size, m_str);
        m_str[m_size] = 0;
    }
    //копирование
    String(const String& other) : String(other.m_str)
    {
        std::cout << "Copy constructor" << std::endl;
    }
    //присваивание
    String& operator=(String temp)
    {
        std::cout << "Copy assignment operator" << std::endl;
        std::swap(m_size, temp.m_size);
        std::swap(m_str, temp.m_str);
        return *this;
    }
    ~String()
    {
        std::cout << "Destructor" << std::endl;
        if (m_str != nullptr)
        {
            delete[] m_str;
        }
    }
    //+= и +
    String operator+=(const String c)
    {
        std::cout << "Operator +=" << std::endl;
        size_t newSize = c.length();
        char* newStr = new char[m_size + newSize + 1];
        for (size_t i = 0; i < m_size; i++)
        {
            newStr[i] = m_str[i];
        }
        for (size_t i = 0; i < newSize; i++)
        {
            newStr[m_size + i] = c.m_str[i];
        }
        delete m_str;
        m_str = newStr;
        m_size += newSize;
        newStr[m_size] = '\0';
        return m_str;
    }

    String operator+(const String& c)
    {
        std::cout << "Operator +" << std::endl;
        String a = *this;
        a += c;
        return a;
    }
    //[]
    char operator [] (const size_t i)
    {
        std::cout << "Operator []" << std::endl;
        return m_str[i];
    }
    //<,>,==
    bool operator < (String& other) const
    {
        std::cout << "Operator <" << std::endl;
        return (strcmp(this->m_str, other.m_str) < 0);
        //return m_size < other.m_size;
    }

    bool operator > (String& other) const
    {
        std::cout << "Operator >" << std::endl;
        return (strcmp(this->m_str, other.m_str) > 0);
        //return m_size > other.m_size;
    }

    bool operator == (String& other) const
    {
        std::cout << "Operator ==" << std::endl;
        return (strcmp(this->m_str, other.m_str) == 0);
        //return (m_size == other.m_size);
    }
    //find
    int find(char c)
    {
        std::cout << "Method find" << std::endl;
        for (int i = 0; i < m_size; i++)
            if (m_str[i] == c)
            {
                return i;
            }
    }
    //length
    size_t length() const
    {
        std::cout << "length = " << (m_size) << std::endl;
        return m_size;
    }
    //c_str
    char* c_str()
    {
        std::cout << "Method c_str" << std::endl;
        return m_str;
    }
    //at
    char at(size_t i)
    {
        std::cout << "Method at" << std::endl;
        if (i < m_size)
            return m_str[i];
        else
            std::cout << "out of range" << std::endl;;
    }

    friend std::ostream& operator << (std::ostream& out, const String& s);
    friend std::istream& operator >> (std::istream& in, String& s);
};
//ввод и вывод
std::istream& operator>> (std::istream& in, String& s)
{
    char d;
    while (in.get(d))
    {
        if (d == '\n' || d == ' ')
        {
            break;
        }
        char* f = new char[s.m_size + 1];
        std::copy(s.m_str, s.m_str + s.m_size, f);
        f[s.m_size] = d;
        delete[] s.m_str;
        std::copy(f, f + s.m_size + 1, s.m_str);
        s.m_size += 1;
        delete[] f;
    }
    return in;
}

std::ostream& operator<< (std::ostream& out, const String& s)
{
    for (int i = 0; i < s.m_size; i++)
    {
        out << s.m_str[i];
    }
    return out;
};

int main()
{
    String s1('s', 5);
    String s2("Hello ");
    String s3("worldik");
    String s4;
    String s5("Hello worldiksssss");
    std::cout << s1 << " " << s2 << " " << s3 << " " << s4 << " " << s5 << std::endl;
    s4 = s2 + s3;
    s4 += s1;
    std::cout << "s2 + s3 + s1 = " << s4 << std::endl;
    std::cout << s3[2] << std::endl;
    std::cout << (s4 == s5) << std::endl;
    int f = s4.find('e');
    std::cout << f << std::endl;
    std::cout << s2.c_str() << std::endl;
    std::cout << s2.at(2) << std::endl;
    std::cout << s1 << "; " << s2 << "; " << s3 << "; " << s4 << "; " << s5 << std::endl;

    return 0;
}