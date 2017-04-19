#!/usr/bin/env bash

$dockerfile='Dockerfile'

if [[ $1 = 'prod' ]]; then
	refs='RUN perl INSTALL.pl -a c -s homo_sapiens -y GRCh38 -l --NO_TEST'
	convert_cahce='RUN perl convert_cache.pl -species all -version all'
	printf '%s\n%s' $refs $convert_cahce > $dockerfile
fi

docker build -t maayanlab/pyvep:latest .

if [[ $1 = 'prod' ]]; then
    sed -i '' '$d' $dockerfile
    sed -i '' '$d' $dockerfile
fi