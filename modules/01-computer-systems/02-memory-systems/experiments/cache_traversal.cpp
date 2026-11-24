// Starter experiment: implement and compare two traversal orders.
#include <chrono>
#include <cstdint>
#include <iostream>
#include <vector>
int main() {
    constexpr std::size_t n = 2048;
    std::vector<std::uint32_t> a(n*n, 1);
    // TODO: implement row-major and column-major sums, warmup and repeated timing.
    // Keep results observable, check sums match, and vary working-set sizes.
    std::cout << "Matrix elements: " << a.size() << '\n';
}
