#!/usr/bin/env bash

GEOS_VERSION="3.4.2"

# Install GEOS
wget http://download.osgeo.org/geos/geos-${GEOS_VERSION}.tar.bz2
tar xjf geos-${GEOS_VERSION}.tar.bz2
cd geos-${GEOS_VERSION}
./configure
make
sudo make install
cd ..

