#include <stdio.h>

#define DBGI(a) printf(#a " ==> %d\n", a)

int main () 
{
  struct {
    char a;
    int b;
    double c;
  } pad;

  char * ptr1;
  int * ptr2;

  //DBGI(&(pad.a));
  //DBGI(&(pad.b));

  //DBGI(sizeof(char));
  //DBGI(sizeof(int));
  //DBGI(sizeof(double));

  //
  pad.b = 123456;
  ptr1 = &(pad.a);
  ptr1++;
  ptr2 = (int *) ptr1;

  DBGI(pad.b);
  DBGI(*ptr2);

  ptr1 += 3;
  ptr2 = (int *) ptr1;
  DBGI(*ptr2);

  //DBGI(sizeof(pad));

  return 0;
}
