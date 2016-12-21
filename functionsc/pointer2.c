#include <stdio.h>

int main (int argc, char ** argv)
{
  int a[2];
  char * p;

  a[0] = 1868654915;
  a[1] = 0;

  p = (char *) a;
  fprintf (stdout, "%d %d %d %x\n", sizeof(int), 
      sizeof(double), sizeof(p), a);
  fprintf (stdout, "%x %s \n", p, p);
   
  return 0;
}
