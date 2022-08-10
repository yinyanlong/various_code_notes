#include <iostream>
#include <string>

int main(int argc, char *argv[]) {
    if (argc < 3) {
        return 0;
    }

    int first = std::stoi(argv[1]);
    int second = std::stoi(argv[2]);

    int result = first + second;

    std::cout << result << std::endl;

    return 0;
}
