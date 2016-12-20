#include <stdio.h>

int main (int argc, char ** argv)
{
  int i = 0, N = 10;

  do
  {
    printf("%d \n", i);
    i++;
  } while (i >= N);

  return 0;
}
