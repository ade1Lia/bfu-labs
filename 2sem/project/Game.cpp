#include "Game.hpp"
#include "Ball.hpp"
namespace mt
{
    Game::~Game()
    {
        if (m_window != nullptr)
            delete m_window;
    }

    void Game::SetCaption(const std::string& caption)
    {
        m_caption = caption;
    }


    void Game::Setup() {
        m_window = new sf::RenderWindow(sf::VideoMode(m_width, m_height), m_caption);
    }

    void Game::Run() {
        std::vector<mt::Ball*> balls;

        balls.emplace_back(new mt::Ball({ 900,0 }, 10, sf::Color::White));

        balls[0]->SetVelocity({ 100,150 });

        sf::Clock timer;

        sf::Font font;
        font.loadFromFile("/Users/polina/Desktop/С++/project-adelia/sunday.ttf");
        sf::Text txt;
        txt.setFont(font);
        txt.setPosition(200, 250);
        txt.setString("GAME OVER");
        txt.setCharacterSize(150);
        txt.setColor(sf::Color::Yellow);
        txt.setStyle(sf::Text::Bold);

        sf::RectangleShape rectangle(sf::Vector2f(160.f, 10.f));
        rectangle.setPosition(350, 600);

        rectangle.setFillColor(sf::Color(128,0,0));

        while (m_window->isOpen()) {
            sf::Event event;
            while (m_window->pollEvent(event)) {
                if (event.type == sf::Event::Closed)
                    m_window->close();
            }

            if (sf::Keyboard::isKeyPressed(sf::Keyboard::Right))
            {
                rectangle.move(0.5, 0.f);
            }
            if (sf::Keyboard::isKeyPressed(sf::Keyboard::Left))
            {
                rectangle.move(-0.5, 0.f);
            }


            for (int i = 0; i < balls.size(); i++) {
                Point p = balls[i]->GetPosition();
                float r = balls[i]->Radius();
                Vec v = balls[i]->GetVelocity();

                if (p.y - r < 0 && v.y < 0)
                    balls[i]->SetVelocity({ v.x, -v.y });

                if (p.x + r >= m_width && v.x > 0)
                    balls[i]->SetVelocity({ -v.x, v.y });

                if (p.x - r <= 0 && v.x < 0)
                    balls[i]->SetVelocity({ -v.x, v.y });

            }

            sf::Time dt = timer.restart();

            for (int i = 0; i < balls.size(); i++)
                balls[i]->Move(dt.asSeconds());

            Vec v = balls[0]->GetVelocity();
            sf::FloatRect boundingBox = (*balls[0]->Get()).getGlobalBounds();
            sf::FloatRect otherBox = rectangle.getGlobalBounds();
            if (boundingBox.intersects(otherBox))
            {
                balls[0]->SetVelocity({ v.x, -v.y });
            }

            m_window->clear();

            m_window->draw(rectangle);
            m_window->draw(*balls[0]->Get());
            for (int i = 0; i < balls.size(); i++)
            {
                Point p = balls[i]->GetPosition();
                float r = balls[i]->Radius();
                Vec v = balls[i]->GetVelocity();
                if (p.y + r > m_height && v.y > 0)
                    m_window->draw(txt);
            }

            m_window->display();
        }

        for (int i = 0; i < balls.size(); i++)
            delete balls[i];
    }
}
