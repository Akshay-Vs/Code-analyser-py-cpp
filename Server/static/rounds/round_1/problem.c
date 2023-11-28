#include <stdlib.h>

int main(int arr[], int n) {
    if(n <= 0){
        return -1;
    }

    int max_element = arr[0];
    for (int i=0; i < n; ++i) {
        if(arr[i] > max_element) {
            max_element = arr[i];
        }
    }
    return max_element;
}