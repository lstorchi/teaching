#include <iostream>

void funcval (int a, int b)
{
  a = 1;
  b = 1;
}

void funcref (int & a, int & b)
{
  a = 1;
  b = 1;
}

int main (int argc, char ** argv)
{
  int a, b;

  a = 0;
  b = 0;

  funcval (a, b);
  std::cout << "a: " << a << " b: " << b << std::endl;

  funcref (a, b);
  std::cout << "a: " << a << " b: " << b << std::endl;
   
  return 0;
}
