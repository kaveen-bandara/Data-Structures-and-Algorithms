#include <iomanip>
#include <iostream>

int main() 
{
    std::string fruits[3];
    double prices[] = {40.25, 50.50, 30.00};

    fruits[0] = "Apple";
    fruits[1] = "Orange";
    fruits[2] = "Banana";

    std::cout << std::fixed << std::setprecision(2);

    for (int i = 0; i < 3; i++)
    {
        std::cout << fruits[i] << " is Rs. " << prices[i] << std::endl;
    }
}
