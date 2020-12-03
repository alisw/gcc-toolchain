#!/bin/sh -ex
rm -rf binutils* gcc* gdb*
curl -L http://ftp.gnu.org/gnu/binutils/binutils-2.35.1.tar.xz | tar xJf -
curl -L ftp://ftp.gnu.org/gnu/gcc/gcc-9.3.0/gcc-9.3.0.tar.xz | tar xJf -
curl -L ftp://ftp.gnu.org/gnu/gdb/gdb-10.1.tar.xz | tar xJf -
ln -nfs binutils* binutils
ln -nfs gcc* gcc
ln -nfs gdb* gdb
