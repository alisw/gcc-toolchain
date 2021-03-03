#!/bin/sh -ex
rm -rf binutils* gcc* gdb* mpfr* isl* mpc* gmp*
curl -l http://isl.gforge.inria.fr/isl-0.21.tar.gz | tar xzf -
curl -L http://ftp.gnu.org/gnu/binutils/binutils-2.35.1.tar.xz | tar xJf -
curl -L ftp://ftp.gnu.org/gnu/gcc/gcc-9.3.0/gcc-9.3.0.tar.xz | tar xJf -
curl -L ftp://ftp.gnu.org/gnu/gdb/gdb-10.1.tar.xz | tar xJf -
curl -l https://www.mpfr.org/mpfr-4.0.2/mpfr-4.0.2.tar.xz | tar xJf -
curl -l https://ftp.gnu.org/gnu/mpc/mpc-1.1.0.tar.gz | tar xzf -
curl -l https://gmplib.org/download/gmp/gmp-6.2.0.tar.xz | tar xJf -

ln -nfs binutils* binutils
ln -nfs gcc* gcc
ln -nfs gdb* gdb
ln -nfs ../mpfr* gcc/mpfr
ln -nfs ../isl* gcc/isl
ln -nfs ../mpc* gcc/mpc
ln -nfs ../gmp* gcc/gmp
ln -nfs mpfr* mpfr
ln -nfs isl* isl
ln -nfs mpc* mpc
ln -nfs gmp* gmp
