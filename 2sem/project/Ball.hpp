#pragma once
#include <SFML/Graphics.hpp>
namespace mt
{
    struct Point
    {
        float x;
        float y;
    };

    struct Vec
    {
        float x;
        float y;
    };

    class Ball
    {
    private:
        Point m_p0;
        Vec m_velocity;
        float m_r;
        sf::CircleShape* m_shape;
    public:
        Ball(Point p0, float r, sf::Color color)
        {
            m_p0 = p0;
            m_r = r;
            m_shape = new sf::CircleShape(m_r);
            m_shape->setFillColor(color);
            m_shape->setOrigin(m_r, m_r);
        }

        ~Ball();

        void Move(double dt);

        sf::CircleShape* Get();

        void SetVelocity(Vec v);

        Point GetPosition();
        Vec GetVelocity();

        float Radius();
    };
}
