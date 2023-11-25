#include <stdio.h>

void print_diamond_pattern(int n) {
    // Upper half of the diamond
    for (int i = 1; i <= n; i += 2) {
        int spaces = (n - i) / 2 + 1;
        for (int s = 0; s < spaces; s++) {
            printf(" ");
        }
        for (int j = 0; j < i; j++) {
            printf("%d", i - j);
        }
        printf("\n");
    }

    // Lower half of the diamond
    for (int i = n - 2; i > 0; i -= 2) {
        int spaces = (n - i) / 2;
        for (int s = 0; s < spaces; s++) {
            printf(" ");
        }
        for (int j = 0; j < i; j++) {
            printf("%d", i + j);
        }
        printf("\n");
    }
}

int main() {
    // Example usage
    print_diamond_pattern(5);
    return 0;
}
