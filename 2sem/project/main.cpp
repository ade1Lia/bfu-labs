#include "Game.hpp"

int main()
{
	mt::Game game;
	game.SetCaption("Game");
	game.Setup();
	game.Run();
	return 0;
}
