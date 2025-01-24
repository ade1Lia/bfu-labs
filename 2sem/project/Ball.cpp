#include "Ball.hpp"
namespace mt
{
    Ball::~Ball()
    {
        delete m_shape;
    }
    void Ball::Move(double dt)
    {
        m_p0.x += m_velocity.x * dt;
        m_p0.y += m_velocity.y * dt;
        m_shape->setPosition(m_p0.x, m_p0.y);
    }
    sf::CircleShape* Ball::Get() { return m_shape; }
    void Ball::SetVelocity(Vec v)
    {
        m_velocity = v;
    }
    Point Ball::GetPosition() { return m_p0; }
    Vec Ball::GetVelocity() { return m_velocity; }
    float Ball::Radius() { return m_r; }
}