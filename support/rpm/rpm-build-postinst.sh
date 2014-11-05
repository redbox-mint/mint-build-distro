#!/usr/bin/env bash

cp /opt/mint/server/mint /etc/init.d/mint
chown root:root /etc/init.d/mint
chmod 755 /etc/init.d/mint

chkconfig --level 445 mint on
# existence of storage directory means we have existing data, otherwise copy 'seed' data
if [ ! -d /opt/mint/storage ]; then
  unzip /opt/mint/home/data/seed/storage.zip -d /opt/mint/
  unzip /opt/mint/home/data/seed/fascinator-index.zip -d /opt/mint/solr/indexes/fascinator
  chown -R redbox:redbox /opt/mint/
fi
service mint restart