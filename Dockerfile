FROM willmclaren/ensembl-vep:release_88.1

#Install denepdencies for Flask
USER root

RUN apt-get update
RUN apt-get -y install sudo

RUN apt-get -y install python3
RUN apt-get -y install python3-dev
RUN apt-get -y install python3-setuptools
RUN apt-get -y install apache2
RUN apt-get -y install apache2-dev


RUN easy_install3 pip
RUN sudo -H pip3 install mod_wsgi
RUN sudo -H pip3 install flask flask-cors requests
EXPOSE 80

ADD . /PyVEP
CMD /PyVEP/boot.sh

#Switch back to VEP-user
USER root
WORKDIR $HOME
RUN git pull