#!/usr/bin/env bash
adduser --disabled-password --gecos '' r
cd /pyvep/
mod_wsgi-express setup-server wsgi.py --port=80 --user r --group r --server-root=/etc/pyvep --socket-timeout=600
chmod a+x /etc/pyvep/handler.wsgi
/etc/pyvep/apachectl start
tail -f /etc/pyvep/error_log
