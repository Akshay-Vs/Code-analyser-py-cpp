#include <stdlib.h>

int* main(int arr[], int n) {
    int* sorted_arr = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        sorted_arr[i] = arr[i];
    }
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (sorted_arr[j] > sorted_arr[j + 1]) {
                int temp = sorted_arr[j];
                sorted_arr[j] = sorted_arr[j + 1];
                sorted_arr[j + 1] = temp;
            }
        }
    }
    return sorted_arr;
}