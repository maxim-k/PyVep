FROM willmclaren/ensembl-vep:release_88

WORKDIR $HOME
RUN mkdir .vep
WORKDIR $HOME/.vep
USER root
RUN apt-get install python3 -y
USER vep
#WORKDIR $HOME/src/ensembl-vep/