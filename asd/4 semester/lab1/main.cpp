#include <iostream>
#include <vector>

/*Требуется ввести N точек своими координатами (x,y). Затем требуется определить,
существует ли выпуклая оболочка заданного множества точек. При этом можно использовать:
или алгоритм Грэхема, или алгоритм Джарвиса, или метод «разделяй и властвуй»*/

//алгоритм Джарвиса

struct Point {
    float x, y;
};

//проверка на ориентацию поворота
int orientation(Point p, Point q, Point r)
{
    float val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y);
    if (val == 0) return 0; //коллинеарны
    return (val > 0) ? 1 : 2; //по часовой или против часовой стрелки
}

//поиск выпуклой оболочки
void convexHull(std::vector<Point>& points)
{
    int n = points.size();
    if (n < 3) return;

    std::vector<Point> hull;

    //находим самую левую точку
    int leftmost = 0;
    for (int i = 1; i < n; i++)
    {
        if (points[i].x < points[leftmost].x)
            leftmost = i;
    }

    int p = leftmost, q;
    //цикл do-while, который выполняется до тех пор, пока мы не вернемся к стартовой точке leftmost.
    //движение против часовой стрелки
    do {
        hull.push_back(points[p]);
        q = (p + 1) % n;
        //цикл проходит по всем остальным точкам и проверяет их отношение к текущей линии, образованной точками p и q.
        for (int i = 0; i < n; i++)
        {
            //Здесь мы проверяем, что точка points[i] находится слева от линии, образованной точками p и q.
            if (orientation(points[p], points[i], points[q]) == 2)
            {
                q = i;
            }
        }
        p = q;
    } while (p != leftmost);

    auto isOnLine = [](const Point& p1, const Point& p2, const Point& p3) -> bool {
        return (p3.x - p1.x) * (p2.y - p1.y) == (p2.x - p1.x) * (p3.y - p1.y);
    };


    for (int i = 2; i < hull.size(); ++i) {
        if (isOnLine(hull[i - 2], hull[i - 1], hull[i])) {
            hull.erase(hull.begin() + i - 1);
            i--;
        }
    }
    // Выводим вершины выпуклой оболочки
    std::cout << "Vertices of the convex hull: " << std::endl;
    for (Point point : hull) {
        std::cout << "(" << point.x << ", " << point.y << ")" << std::endl;
    }
}

int main() {
    int n;
    std::cout << "Enter the number of dots: ";
    std::cin >> n;

    std::vector<Point> points(n);
    std::cout << "Enter the coordinates of the points (x, y):" << std::endl;
    for (int i = 0; i < n; i++) {
        std::cin >> points[i].x >> points[i].y;
    }

    convexHull(points);

    return 0;
}
