#include <stdio.h>

int func(int, int);

void main() {
    int n = 2;
    int m = 3;
    printf("%d\n", func(n, m));
}

int func(int m, int n) {
    if (m == 0) return n + 1;
    if (n == 0) return func(m - 1, 1);
    return func(m - 1, func(m, n - 1));
}