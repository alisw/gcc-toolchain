#!/bin/sh -ex
rm -rf binutils* gcc* gdb* mpfr* isl* mpc* gmp* autoconf-archive*
curl -L http://isl.gforge.inria.fr/isl-0.21.tar.gz | tar xzf -
curl -L http://ftp.gnu.org/gnu/binutils/binutils-2.35.1.tar.xz | tar xJf -
curl -L ftp://ftp.gnu.org/gnu/gcc/gcc-10.2.0/gcc-10.2.0.tar.xz | tar xJf -
curl -L ftp://ftp.gnu.org/gnu/gdb/gdb-10.1.tar.xz | tar xJf -
curl -L https://www.mpfr.org/mpfr-4.0.2/mpfr-4.0.2.tar.xz | tar xJf -
curl -L https://ftp.gnu.org/gnu/mpc/mpc-1.1.0.tar.gz | tar xzf -
curl -L https://gmplib.org/download/gmp/gmp-6.2.0.tar.xz | tar xJf -
curl -L https://ftpmirror.gnu.org/autoconf-archive/autoconf-archive-2021.02.19.tar.xz | tar xJf -

mv binutils* binutils
mv gcc* gcc
mv gdb* gdb
mv autoconf-archive* autoconf-archive
mv mpfr* gcc/mpfr
mv gmp* gcc/gmp
mv isl* gcc/isl
mv mpc* gcc/mpc

rm -fr gcc/.gitignore
