GEOS_VERSION="3.4.2"
PROJ_VERSION="4.9.1"
PROJ_DATUM_VERSION="1.5"
GDAL_VERSION="2.3.3"


# notes
#to get the django app to work with everything it has in it, certain packages had to be
#reduced in version and other things added in through the ec2 instance
#
#for psycopg2, the fix may of been to do this: sudo yum install postgresql postgresql-dev python-dev
#https://stackoverflow.com/questions/11618898/pg-config-executable-not-found
#
#when first importing geos,proj,gdal, the python module may not be able to be found
#things that were done to rectify that were to go into /usr/local/libs and cd into
#/etc/ld.so.conf and do sudo vi /etc/ld.so.conf to open it; from there add the line
#include /etc/ld.so.conf.d/*.conf. afterwards, go into or add /etc/ld.so.conf.d/libc.conf and add
#the line /usr/local/lib and run sudo ldconfig to save changes. Another thing to consider
#is the LD_LIBRARY_PATH which may need to be set to where the librarys ares. You can set the
#path in the terminal but for it to persist after the session, you can do sudo ~/.bash_profile
#and add LD_LIBRARY_PATH=$LD_LIBRARY_PATH:usr/local/lib and add export LD_LIBRARY_PATH

#


# new steps
# 1. first run each fo the sections below individually (for some reason a single script won't cut it)
2.


# somthing along those lines, this will help get things like geos-devel,proj devel, etc.
# Install GEOS
wget http://download.osgeo.org/geos/geos-${GEOS_VERSION}.tar.bz2
tar xjf geos-${GEOS_VERSION}.tar.bz2
cd geos-${GEOS_VERSION}
./configure
make
sudo make install
cd ..

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

# Install GDAL
sudo yum-config-manager --enable epel
sudo amazon-linux-extras install epel

sudo yum install gdal-python
sudo yum -y update
sudo yum install make automake gcc gcc-c++ libcurl-devel proj-devel geos-devel autoconf automake gdal
cd /tmp
curl -L http://download.osgeo.org/gdal/${GDAL_VERSION}/gdal-${GDAL_VERSION}.tar.gz --output gdal-${GDAL_VERSION}
tar zxf gdal-${GDAL_VESRION}
cd gdal-${GDAL_VERSION}
./configure --prefix=/usr/local --with-python
make -j4
sudo make install
cd ~
pip install --global-option=build_ext --global-option="-I/usr/include/gdal" GDAL==${GDAL_VERSION} # https://stackoverflow.com/questions/29852857/no-module-named-osgeo-ogr



