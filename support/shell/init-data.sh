#!/usr/bin/env bash
curl -o mint-solr-geonames-1.0.noarch.rpm http://dev.redboxresearchdata.com.au/yum/releases/mint-solr-geonames-1.0.noarch.rpm
rpm --noscripts -i mint-solr-geonames-1.0.noarch.rpm
rm -Rf mint-solr-geonames-1.0.noarch.rpm
curl -o mint-build-distro-initial-data-1.2-1.noarch.rpm http://dev.redboxresearchdata.com.au/yum/releases/mint-build-distro-initial-data-1.2-1.noarch.rpm
rpm --noscripts -i mint-build-distro-initial-data-1.2-1.noarch.rpm
rm -Rf mint-build-distro-initial-data-1.2-1.noarch.rpm
cd /opt/mint
tar -xvzf mint-build-distro-initial-data.tar.gz -C /
mv /opt/mint/storage /opt/mint/data/storage
rm -Rf /opt/mint/mint-build-distro-initial-data.tar.gz