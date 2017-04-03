#!/usr/bin/env bash
adduser --disabled-password --gecos '' r
cd /PyVEP/
mod_wsgi-express setup-server wsgi.py --port=80 --user r --group r --server-root=/etc/PyVEP --socket-timeout=600
chmod a+x /etc/PyVEP/handler.wsgi
/etc/PyVEP/apachectl start
tail -f /etc/PyVEP/error_log
