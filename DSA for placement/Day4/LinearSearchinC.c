#include <stdio.h>

int search(int arr[], int n, int num)
{
    for (int i = 0; i < n; i++)
    {
        if (arr[i] == num)
        {
            return i;
        }
    }
    return -1;
}

int main()
{
    // Write C code here
    int arr[] = {1, 2, 3, 4, 5};
    int num = 3;
    int n = sizeof(arr) / sizeof(arr[0]);
    int val = search(arr, n, num);
    printf("%d", val);

    return 0;
}