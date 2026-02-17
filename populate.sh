#!/bin/sh -ex
rm -rf binutils* gcc* gdb* mpfr* isl* mpc* gmp* autoconf-archive* ccache*
curl -L https://libisl.sourceforge.io/isl-0.27.tar.bz2 | tar -xjf - # isl 0.26 fails to compile intree of gcc, thus stick to old version
curl -L ftp://ftp.gnu.org/gnu/binutils/binutils-2.46.0.tar.xz | tar xJf -
curl -L ftp://ftp.gnu.org/gnu/gcc/gcc-15.2.0/gcc-15.2.0.tar.xz | tar xJf -
curl -L ftp://ftp.gnu.org/gnu/gdb/gdb-17.1.tar.xz | tar xJf -
curl -L ftp://ftp.gnu.org/gnu/mpfr/mpfr-4.2.2.tar.xz | tar xJf -
curl -L ftp://ftp.gnu.org/gnu/mpc/mpc-1.3.1.tar.gz | tar xzf -
curl -L ftp://ftp.gnu.org/gnu/gmp/gmp-6.3.0.tar.xz | tar xJf -
curl -L ftp://ftp.gnu.org/gnu/autoconf-archive/autoconf-archive-2024.10.16.tar.xz | tar xJf -
curl -L https://github.com/ccache/ccache/releases/download/v4.12.3/ccache-4.12.3.tar.xz | tar xJf - # FindZstd.cmake/FindHiredis.cmake is misspelled in this version...
curl -L https://github.com/Kitware/CMake/archive/refs/tags/v4.2.3.tar.gz | tar xzf -

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
