#include <iostream>
#include <vector>
#include <algorithm>
/*На вход дается одно число х, нужно вывести все числа от 1 до х, удовлетворяющие условию:
3 ^ K * 5 ^ L * 7 ^ M = xi
где K, L, M - натуральные числа (могут быть равны 0)*/

int main() {
    long long x;
    std::cout << "x = ";
    std::cin >> x;
    long long tx = 1;
    std::vector <long long> mas;
    while (tx <= x) {
        long long tf = tx;
        while (tf <= x) {
            long long ts = tf;
            while (ts <= x) {
                mas.push_back(ts);
                ts *= 7;
            }
            tf *= 5;
        }
        tx *= 3;
    }
    std::sort(mas.begin(), mas.end());
    for (int i = 0; i < mas.size(); i++) {
        std::cout << mas.at(i) <<'\n';
    }
}
