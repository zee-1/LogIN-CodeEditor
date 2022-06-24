#include <stdio.h>

void hey();

int main(){
      freopen("output.txt", "w", stdout);
      return 0;
}

void hey(){printf("Hello World");}