/* { dg-do run } */

#include "check.h"

void
f ()
{
  unsigned long tmp[4] __attribute__((aligned(64)));
  check (&tmp, 64);
}

int
main()
{
  f();
  return 0;
}
