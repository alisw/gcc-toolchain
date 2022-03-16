#!/bin/sh -ex
rm -rf binutils* gcc* gdb* mpfr* isl* mpc* gmp* autoconf-archive*
curl -L https://gcc.gnu.org/pub/gcc/infrastructure/isl-0.24.tar.bz2 | tar -xjf -
curl -L ftp://ftp.gnu.org/gnu/binutils/binutils-2.38.tar.xz | tar xJf -
curl -L ftp://ftp.gnu.org/gnu/gcc/gcc-11.2.0/gcc-11.2.0.tar.xz | tar xJf -
curl -L ftp://ftp.gnu.org/gnu/gdb/gdb-11.2.tar.xz | tar xJf -
curl -L ftp://ftp.gnu.org/gnu/mpfr/mpfr-4.1.0.tar.xz | tar xJf -
curl -L ftp://ftp.gnu.org/gnu/mpc/mpc-1.2.1.tar.gz | tar xzf -
curl -L ftp://ftp.gnu.org/gnu/gmp/gmp-6.2.1.tar.xz | tar xJf -
curl -L ftp://ftp.gnu.org/gnu/autoconf-archive/autoconf-archive-2022.02.11.tar.xz | tar xJf -

mv binutils* binutils
mv gcc* gcc
mv gdb* gdb
mv autoconf-archive* autoconf-archive
mv mpfr* gcc/mpfr
mv gmp* gcc/gmp
mv isl* gcc/isl
mv mpc* gcc/mpc

rm -fr gcc/.gitignore
