#include <stdio.h>
#include <stdlib.h>

int main (int argc, char ** argv)
{
  int i;

  i = 4;

  switch (i)
  {
    case 1:
      printf("vale uno \n");
      break;
    case 2:
      printf("vale due \n");
      break;
    default:
      printf("non uno non due\n");
      break;
  }

  return 0;
}
