#include <iostream>
#include <string>
#include <vector>
using std::string;
using std::vector;

vector<int> parseInput(std::istream & s){
    vector<int> numbers{};
    while(!s.eof()){
        int value;
        string input;
        s >> input;
        value = std::stoi(input);
        numbers.push_back(value);
    }
    return numbers;
}

int main()
{
    // Read through all input provided.
    vector<int> numbers = parseInput(std::cin);
    for(int i = 0; i < numbers.size(); i++){
        for(int j = 0; j < i; j++){
            if (i != j && numbers[i] + numbers[j] == 2020){
                std::cout << "Part 1 solution: " << numbers[i] * numbers[j] << std::endl;
            }
        }
    }
    for(int i = 0; i < numbers.size(); i++){
        for(int j = 0; j < i; j++){
            for(int k = 0; k < j; k++){
                if (i != j && j != k && i != k && numbers[i] + numbers[j] + numbers[k] == 2020){
                    std::cout << "Part 2 solution: " << numbers[i] * numbers[j] * numbers[k] << std::endl;
                }
            }
        }
    }

}