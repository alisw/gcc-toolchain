#!/bin/sh -ex
rm -rf binutils* gcc* gdb*
curl -L http://ftp.gnu.org/gnu/binutils/binutils-2.27.tar.gz | tar xzf -
curl -L ftp://ftp.gnu.org/gnu/gcc/gcc-6.2.0/gcc-6.2.0.tar.gz | tar xzf -
curl -L ftp://ftp.gnu.org/gnu/gdb/gdb-7.12.1.tar.xz | tar xJf -
