#include <SFML/Graphics.hpp>
#include <string>
#include <iostream>
class AnimatedText{
private:
    std::string m_text;
    const float m_duration;
    void Screen(sf::RenderWindow& window)
    {
        sf::Event event;
        while (window.pollEvent(event))
            if (event.type == sf::Event::Closed)
                window.close();
    }
public:
    AnimatedText(const std::string& text, float duration) : m_text(text), m_duration(duration) {}
    //float getDuration() { return m_duration; }
    std::string getText() { return m_text; }
    void Play(sf::RenderWindow& window)
    {
        sf::Font font;
        font.loadFromFile("Babylonica-Regular.ttf");
        std::string str = "";
        sf::Text text(str, font, 70);
        text.setPosition(100, 100);
        sf::Time elapsed = sf::Time::Zero;
        while (window.isOpen())
        {
            Screen(window);
            while (elapsed.asSeconds()< m_duration)
            {
                for (int i = 0; i < m_text.length(); i++)
                {
                    str += getText()[i];
                    text.setString(str);
                    elapsed = sf::seconds(elapsed.asSeconds() + m_duration / m_text.length());
                    sf::sleep(elapsed);
                    std::cout << elapsed.asSeconds() << std::endl;
                    window.clear();
                    window.draw(text);
                    window.display();
                }
            }
        }
    }
};
int main() {
    AnimatedText animatedText("Hello, world!", 13.0f);
    sf::RenderWindow window(sf::VideoMode(600, 400), "Animated Text");
    animatedText.Play(window);
    return 0;
}