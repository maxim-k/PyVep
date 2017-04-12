FROM willmclaren/ensembl-vep:release_88.5

USER root

RUN apt-get update
RUN apt-get -y install sudo

RUN apt-get -y install python3
RUN apt-get -y install python3-dev
RUN apt-get -y install python3-setuptools
RUN apt-get -y install python3-pip
#RUN apt-get -y install apache2
#RUN apt-get -y install apache2-dev
RUN apt-get -y install nginx uwsgi-core

#RUN sudo -H pip3 install mod_wsgi
RUN pip3 install -Iv Flask uwsgi
RUN sudo -H pip3 install -Iv flask flask-cors requests werkzeug uwsgi

ADD . /PyVEP
CMD /PyVEP/boot.sh
EXPOSE 80

WORKDIR $HOME/src/ensembl-vep
RUN git pull
#RUN sudo echo 'r     ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
#RUN perl INSTALL.pl -a c -s homo_sapiens -y GRCh38 -l --NO_TEST