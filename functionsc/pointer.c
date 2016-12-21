#include <stdio.h>

void func (int * a, int * b)
{
  *a = 1;
  *b = 1;
}

int main (int argc, char ** argv)
{
  int a, b;

  a = 0;
  b = 0;

  func (&a, &b);
  fprintf (stdout, "a: %d b: %d \n", a, b);
   
  return 0;
}
