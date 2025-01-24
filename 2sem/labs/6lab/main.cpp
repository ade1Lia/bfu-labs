#include <iostream>
#include "log.hpp"

int main()
{
    Log::SetLogPath("log.txt");
    Log::SetLogLevel(LogLevel::DEBUG);
    Log::Write("dog");
    Log::Info("cat");
    return 0;
}