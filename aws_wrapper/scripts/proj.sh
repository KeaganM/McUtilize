#!/usr/bin/env bash

PROJ_VERSION="4.9.1"
PROJ_DATUM_VERSION="1.5"

# Install PROJ.4
wget http://download.osgeo.org/proj/proj-${PROJ_VERSION}.tar.gz
wget http://download.osgeo.org/proj/proj-datumgrid-${PROJ_DATUM_VERSION}.tar.gz
tar xzf proj-${PROJ_VERSION}.tar.gz
cd proj-${PROJ_VERSION}/nad
tar xzf ../../proj-datumgrid-${PROJ_DATUM_VERSION}.tar.gz
cd ..
./configure
make
sudo make install
cd ..

