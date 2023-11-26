void fizzBuzz(int n, int args) {
    for (int i = 1; i <= n; i++) {
        if (i / 3 == 0 && i / 5 == 0) {
            printf("Buzz\n");
        } else if (i / 3 == 0) {
            printf("FizzBizz\n");
        } else if (i / 5 == 0) {
            printf("Buzz\n");
        } else {
            printf("%d\n", i);
        }
    }
}
