#!/bin/sh -ex
rm -rf binutils* gcc* gdb* mpfr* isl* mpc* gmp* autoconf-archive* ccache*
curl -L https://libisl.sourceforge.io/isl-0.24.tar.bz2 | tar -xjf - # isl 0.26 fails to compile intree of gcc, thus stick to old version
curl -L ftp://ftp.gnu.org/gnu/binutils/binutils-2.43.tar.xz | tar xJf -
curl -L ftp://ftp.gnu.org/gnu/gcc/gcc-14.2.0/gcc-14.2.0.tar.xz | tar xJf -
curl -L ftp://ftp.gnu.org/gnu/gdb/gdb-15.1.tar.xz | tar xJf -
curl -L ftp://ftp.gnu.org/gnu/mpfr/mpfr-4.2.1.tar.xz | tar xJf -
curl -L ftp://ftp.gnu.org/gnu/mpc/mpc-1.3.1.tar.gz | tar xzf -
curl -L ftp://ftp.gnu.org/gnu/gmp/gmp-6.3.0.tar.xz | tar xJf -
curl -L ftp://ftp.gnu.org/gnu/autoconf-archive/autoconf-archive-2022.02.11.tar.xz | tar xJf -
curl -L https://github.com/ccache/ccache/releases/download/v4.10.2/ccache-4.10.2.tar.xz | tar xJf - # FindZstd.cmake/FindHiredis.cmake is misspelled in this version...
curl -L https://github.com/Kitware/CMake/archive/refs/tags/v3.29.2.tar.gz | tar xzf -

mv CMake* cmake
mv binutils* binutils
mv ccache* ccache
mv gcc* gcc
mv gdb* gdb
mv autoconf-archive* autoconf-archive
mv mpfr* gcc/mpfr
mv gmp* gcc/gmp
mv isl* gcc/isl
mv mpc* gcc/mpc

rm -fr gcc/.gitignore
