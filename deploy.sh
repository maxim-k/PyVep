#!/usr/bin/env bash

dockerfile='Dockerfile'

if [[ $1 = 'prod' ]]; then
    echo 'RUN perl INSTALL.pl -a c -s homo_sapiens -y GRCh38 -l --NO_TEST' >> $dockerfile
	echo -n 'RUN perl convert_cache.pl -species all -version all'  >> $dockerfile
fi

docker build -t maayanlab/pyvep:latest .

if [[ $1 = 'prod' ]]; then
    sed -i '' '$d' $dockerfile
    sed -i '' '$d' $dockerfile
fi