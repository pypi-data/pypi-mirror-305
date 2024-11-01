#!/bin/bash
echo "configure.."
./configure CXX=g++ --prefix=`pwd` --enable-half-emulation --disable-dependency-tracking
echo "make install.."
make install