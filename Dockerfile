FROM willmclaren/ensembl-vep:release_88.6

USER root

RUN apt-get update
RUN apt-get -y install sudo

RUN apt-get -y install python3
RUN apt-get -y install python3-dev
RUN apt-get -y install python3-setuptools
RUN apt-get -y install python3-pip
RUN apt-get -y install nginx uwsgi-core

RUN sudo -H pip3 install -Iv Flask flask-cors requests uwsgi

ADD . /PyVEP
RUN chmod -R 777 /PyVEP/pyvep/uploads/
RUN chmod -R 777 /PyVEP/pyvep/results/

CMD /PyVEP/boot.sh
EXPOSE 80

WORKDIR $HOME/src/
RUN git clone https://github.com/Ensembl/ensembl-xs.git
WORKDIR $HOME/src/ensemlb-xs
RUN chmod -R 777 $HOME/src/ensemlb-xs
RUN sudo perl Makefile.PL
RUN sudo make
RUN sudo make test
RUN sudo make install

WORKDIR $HOME/src/ensembl-vep
RUN git pull