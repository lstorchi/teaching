#include <stdio.h>
#include <stdlib.h>

#define N 10 
#define DBGF(a) printf(#a " ==> %f\n", a)

int main (int argc, char ** argv)
{
  int i;
  float a[N], b[N], s;
  unsigned int seed = 10;

  srand(seed);

  for (i=0; i<N; ++i)
  {
    a[i] = (float)rand()/(float)(RAND_MAX/N); 
    b[i] = (float)rand()/(float)(RAND_MAX/N); 
  }

  for (i=0; i<N; ++i)
  {
    DBGF(a[i]);
    DBGF(b[i]);
  }

  s = 0.0;
  for (i=0; i<N; ++i)
  {
    s = s + a[i]*b[i]; 
  }

  printf("%f \n", s);

  return 0;
}
