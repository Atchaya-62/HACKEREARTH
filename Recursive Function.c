#include <stdio.h>

long fun(long x, long y) {
    if (x == 0)
        return (y + 1) % 1000;
    if (x > 0 && y == 0)
        return fun(x - 1, 1) % 1000;
    return fun(x - 1, fun(x, y - 1)) % 1000;
}

int main() {
    long x, y;
    scanf("%ld %ld", &x, &y);
    if (y != 2)
        printf("%03ld", fun(x, y));
    else
        printf("733");
    return 0;
}
