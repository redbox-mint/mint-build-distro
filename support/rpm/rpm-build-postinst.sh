#!/usr/bin/env bash

cp /opt/mint/server/mint /etc/init.d/mint
chown root:root /etc/init.d/mint
chmod 755 /etc/init.d/mint

chkconfig --level 445 mint on
# means we have existing data, otherwise copy 'seed' data
DIRECTORY=`/opt/mint/solr/indexes/fascinator/index/`
if [ ! -d "$DIRECTORY" ]; then
  yum -y install unzip
  unzip /opt/mint/home/data/seed/storage.zip -d /opt/mint/
  unzip /opt/mint/home/data/seed/fascinator-index.zip -d /opt/mint/solr/indexes/fascinator
  chown -R redbox:redbox /opt/mint/
fi
# install mint-solr-geonames
yum -y install mint-solr-geonames
service mint restart