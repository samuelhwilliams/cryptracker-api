#!/usr/bin/env python3

import json

APACHE_CONFIG = """WSGIPythonPath "/home/cryptracker/cryptracker-api/venv3/bin/python3"
WSGIPythonHome "/home/cryptracker/cryptracker-api/venv3/lib/python3.5/site-packages"

<VirtualHost *:80>
        # The ServerName directive sets the request scheme, hostname and port that
        # the server uses to identify itself. This is used when creating
        # redirection URLs. In the context of virtual hosts, the ServerName
        # specifies what hostname must appear in the request's Host: header to
        # match this virtual host. For the default virtual host (this file) this
        # value is not decisive as it is used as a last resort host regardless.
        # However, you must set it for any further virtual host explicitly.
        ServerName {}
        ServerAdmin webmaster@localhost

        DocumentRoot /home/cryptracker/cryptracker-api

        # Available loglevels: trace8, ..., trace1, debug, info, notice, warn,
        # error, crit, alert, emerg.
        # It is also possible to configure the loglevel for particular
        # modules, e.g.
        #LogLevel info ssl:warn

        ErrorLog ${{APACHE_LOG_DIR}}/error.log
        CustomLog ${{APACHE_LOG_DIR}}/access.log combined

        # Comment out WSGIDaemonProcess to deploy certificates via certbot-auto
        # Uncomment after... obviously
        WSGIDaemonProcess cryptracker user=cryptracker group=cryptracker threads=1
        WSGIScriptAlias / /home/cryptracker/cryptracker-api/cryptracker.wsgi

        <Directory /home/cryptracker/cryptracker-api>
                WSGIProcessGroup cryptracker
                WSGIApplicationGroup %{{GLOBAL}}
                Require all granted
        </Directory>

        # For most configuration files from conf-available/, which are
        # enabled or disabled at a global level, it is possible to
        # include a line for only one particular virtual host. For example the
        # following line enables the CGI configuration for this host only
        # after it has been globally disabled with "a2disconf".
        #Include conf-available/serve-cgi-bin.conf
</VirtualHost>

# vim: syntax=apache ts=4 sw=4 sts=4 sr noet"""

if __name__ == '__main__':
    with open('../secrets/config.json') as config_file:
        config = json.loads(config_file.read())

    with open('{}.conf'.format(config['domain']), 'w') as apache_config_file:
        apache_config_file.write(APACHE_CONFIG.format(config['domain']))

