#pragma once
#include <fstream>
#include <iostream>
#include <chrono>
#include <windows.h>
enum class LogLevel {
    DEBUG,
    RELEASE
};

class Log
{
private:
    static std::ofstream m_out;
    static LogLevel m_logLevel;
    static HANDLE m_a;
public:
    Log()
    {
        std::cout << "const" << std::endl;
    }

    static void SetLogLevel(LogLevel logLevel)
    {
        m_logLevel = logLevel;
    }

    static void SetLogPath(const std::string& path)
    {
        m_out.open(path);
    }

    static void Write(const std::string& msg)
    {
        time_t t = time(0);
        char* dt = ctime(&t);
        if (m_logLevel == LogLevel::DEBUG)
        {
            m_a = GetStdHandle(STD_OUTPUT_HANDLE);
            SetConsoleTextAttribute(m_a, 20);
            std::cerr << dt << msg << std::endl;
        }
        m_out << dt << msg << std::endl;
        m_out.flush();
    }

    static void Info(const std::string& msg)
    {
        time_t t = time(0);
        char* dt = ctime(&t);
        if (m_logLevel == LogLevel::RELEASE)
        {
            m_a = GetStdHandle(STD_OUTPUT_HANDLE);
            SetConsoleTextAttribute(m_a, 1);
            std::cerr << dt << msg << std::endl;
        }
        m_out << dt << msg << std::endl;
        m_out.flush();
    }

    static void Error(const std::string& msg)
    {
        time_t t = time(0);
        char* dt = ctime(&t);
        if (m_logLevel == LogLevel::DEBUG)
        {
            m_a = GetStdHandle(STD_OUTPUT_HANDLE);
            SetConsoleTextAttribute(m_a, 50);
            std::cerr << dt << msg << std::endl;
        }
        m_out << dt << msg << std::endl;
        m_out.flush();
    }

    ~Log()
    {
        std::cout << "Destr" << std::endl;
    }
};