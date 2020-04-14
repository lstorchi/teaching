#include <stdio.h>

#define DBGI(a) printf(#a " ==> %d\n", a)

int main () 
{

  struct {
    char a;
    int b;
    double c;
  } pad;

  DBGI(sizeof(char));
  DBGI(sizeof(int));
  DBGI(sizeof(double));
  DBGI(sizeof(pad));

  return 0;
}
