cmake_minimum_required(VERSION 3.23)
project(project_adelia)

set(CMAKE_CXX_STANDARD 23)

include_directories(/opt/homebrew/Cellar/sfml/2.5.1_2/include)
link_directories(/opt/homebrew/Cellar/sfml/2.5.1_2/lib)


add_executable(project_adelia main.cpp Game.cpp Game.hpp Ball.hpp sunday.ttf Ball.cpp )

target_link_libraries(project_adelia sfml-graphics sfml-window sfml-system)
