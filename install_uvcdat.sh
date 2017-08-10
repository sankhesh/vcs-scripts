#!/usr/bin/env bash
# Run this script to install uvcdat python packages

UVCDAT_HOME=${HOME}/Projects/uvcdat

build() {
#  find ${UVCDAT_HOME}/src -name build -exec rm -rf {} \;
  pushd ${UVCDAT_HOME}/bld/
  rm -rf ./*
  cmake ${UVCDAT_HOME}/src 
  make -j10
  ${UVCDAT_HOME}/bld/CMake/runtest conda install cdat_info

  install
  
  ctest -R download_sample
  popd
}

install() {
  pushd ${UVCDAT_HOME}/vcs
  ${UVCDAT_HOME}/bld/CMake/runtest python setup.py install -f --old-and-unmanageable
  popd
}

# call arguments verbatim:
$@

#
#source ${UVCDAT_HOME}/bld/install/bin/setup_runtime.sh
#pushd ${UVCDAT_HOME}/src/Packages/vcs
#python setup.py install --prefix=${UVCDAT_HOME}/bld/install/Externals/
#python setup.py install --prefix=${UVCDAT_HOME}/bld/install/
#popd
#
#pushd ${UVCDAT_HOME}/src/Packages/Thermo
#python setup.py install --prefix=${UVCDAT_HOME}/bld/install/
#popd
#
#pushd ${UVCDAT_HOME}/src/Packages/DV3D
#python setup.py install --prefix=${UVCDAT_HOME}/bld/install/
#popd
