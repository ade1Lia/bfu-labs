#pragma once
#include <string>
#include <iostream>
#include <SFML/Graphics.hpp>
#include "Ball.hpp"

namespace mt
{
    class Game
    {
    private:
        const int m_width = 1200;
        const int m_height = 800;
        std::string m_caption;
        sf::RenderWindow* m_window = nullptr;

    public:
        Game() {}
        ~Game();
        void SetCaption(const std::string& caption);
        void SetResolution(int width, int height);
        void Setup();
        void Run();
    };
}
