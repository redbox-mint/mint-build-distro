#!/usr/bin/env bash

cp /opt/mint/server/mint /etc/init.d/mint
chown root:root /etc/init.d/mint
chmod 755 /etc/init.d/mint

chkconfig --level 445 mint on

service mint restart