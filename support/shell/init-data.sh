#!/usr/bin/env bash
curl -o mint-solr-geonames-1.0.noarch.rpm http://dev.redboxresearchdata.com.au/yum/releases/mint-solr-geonames-1.0.noarch.rpm
rpm --noscripts -i mint-solr-geonames-1.0.noarch.rpm
rm -Rf mint-solr-geonames-1.0.noarch.rpm
curl -o mint-build-distro-initial-data-1.2-1.noarch.rpm http://dev.redboxresearchdata.com.au/yum/releases/mint-build-distro-initial-data-1.2-1.noarch.rpm
rpm --noscripts -i mint-build-distro-initial-data-1.2-1.noarch.rpm
rm -Rf mint-build-distro-initial-data-1.2-1.noarch.rpm
cd /opt/mint
tar -xvzf mint-build-distro-initial-data.tar.gz -C /
cp -Rf /opt/mint/storage /opt/mint/data/ && rm -Rf /opt/mint/storage
cp -Rf /opt/mint/solr /opt/mint/data/ && rm -Rf /opt/mint/solr
rm -Rf /opt/mint/mint-build-distro-initial-data.tar.gz
