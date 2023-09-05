#include <iostream>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

int main(int argc, char const *argv[])
{
    int a, b, out;
    a = stoi(argv[1]);
    b = stoi(argv[2]);
    bool c;
    bool c1 = false;
    c = a > b;
    
    if (c ^ c1)
        out = a + 5;
    else
        out = b * 3;

    printf("%d\n", out);

    return 0;
}