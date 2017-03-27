FROM willmclaren/ensembl-vep:release_88

WORKDIR $HOME
RUN mkdir .vep
WORKDIR $HOME/.vep
RUN wget -i ftp://ftp.ensembl.org/pub/release-87/variation/VEP/homo_sapiens_vep_87_GRCh38.tar.gz
RUN tar xfz homo_sapiens_vep_87_GRCh37.tar.gz
RUN rm homo_sapiens_vep_87_GRCh37.tar.gz
WORKDIR $HOME/src/ensembl-vep/