#include <iostream>

class Complex {
private:
    double m_a;
    double m_b;
public:
    Complex() = default;

    Complex(double a = 0.0, double b = 0.0) : m_a(a), m_b(b)
    {
        std::cout << "Basic constructor" << std::endl;
    }

    Complex(const Complex& z)
    {
        m_a = z.m_a;
        m_b = z.m_b;
    }

    Complex operator=(Complex z)
    {
        std::swap(m_a, z.m_a);
        std::swap(m_b, z.m_b);
        return *this;
    }

    Complex &operator+=(const Complex& z)
    {
        (*this).m_a += z.m_a;
        (*this).m_b += z.m_b;
        return *this;
    }

    Complex &operator *= (const Complex &z)
    {
        double k=(*this).m_a;
        (*this).m_a = ((*this).m_a * z.m_a) -  ((*this).m_b * z.m_b);
        (*this).m_b = (k*z.m_b) + ((*this).m_b * z.m_a);
        return *this;
    }

    Complex& operator++()
    {
        this -> m_a++;
        return *this;
    }

    Complex operator++(int)
    {
        Complex temp = *this;
        this -> m_a++;
        return temp;
    }
    Complex operator+ (Complex& z)
    {
        std::cout << "operator + " << std::endl;
        double a = m_a + z.m_a;
        double b = m_b + z.m_b;
        Complex new_z(a, b);
        return new_z;
    }

    friend std::ostream& operator<< (std::ostream& out, const Complex& z);
    friend std::istream& operator>> (std::istream& in, Complex& z);
    ~Complex(){}
};

Complex operator* (const Complex& z1, const Complex& z2)
{
    Complex temp = z1;
    temp *= z2;
    return temp;
}

std::ostream& operator<<(std::ostream& out, const Complex& z)
{
    out << z.m_a << "+" << z.m_b << "i" << std::endl;
    return out;
}

std::istream& operator>>(std::istream& in, Complex& z)
{
    in >> z.m_a >> z.m_b;
    return in;
}

int main()
{
    Complex z1(4, 7), z2(3, 2), z3(2, 4), z4(1, 8);
    std::cout << z1 << z2 << z3 << z4 <<  std::endl;
    z3 += z4;
    std::cout << "sum of 3 and 4 numbers = " << z3 << std::endl;
    std::cout << "sum of 1 and 2 numbers = " << (z4 = z1 + z2) << std::endl;
    z1 *= z2;
    std::cout << "multiplication of 1 and 2 numbers = " << z1 << std::endl;
    std::cout << "multiplication of 2 and 3 numbers = " << z2 * z3 << std::endl;

    return 0;

}
