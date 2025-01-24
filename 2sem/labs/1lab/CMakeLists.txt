cmake_minimum_required(VERSION 3.24)
project(lab1_2semestr)

set(CMAKE_CXX_STANDARD 17)
include_directories(/opt/homebrew/Cellar/sfml/2.5.1_2/include)
link_directories(/opt/homebrew/Cellar/sfml/2.5.1_2/lib)

add_executable(lab1_2semestr main.cpp)


target_link_libraries(lab1_2semestr sfml-graphics sfml-window sfml-system)