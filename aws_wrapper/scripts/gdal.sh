#!/usr/bin/env bash

GDAL_VERSION="2.3.3"

# Install GDAL
sudo yum-config-manager --enable epel
sudo yum install gdal-python
sudo yum -y update
sudo yum install make automake gcc gcc-c++ libcurl-devel proj-devel geos-devel autoconf automake gdal
cd /tmp
curl -L http://download.osgeo.org/gdal/${GDAL_VERSION}/gdal-${GDAL_VERSION}.tar.gz | tar zxf -cd gdal-${GDAL_VERSION}/
./configure --prefix=/usr/local --with-python
make -j4
sudo make install
sudo easy_install GDAL
export LD_LIBRARY_PATH="/usr/local/lib:$LD_LIBRARY_PATH"
sudo ldconfig
#cd /usr/local
#
#tar zcvf ~/gdal-${GDAL_VERSION}-amz1.tar.gz *