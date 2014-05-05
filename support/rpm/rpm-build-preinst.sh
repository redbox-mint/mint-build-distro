#!/usr/bin/env bash
## Create redbox user and group if they have not been created
if ! type "/etc/init.d/mint" > /dev/null; then
  service mint stop
fi

## Remove old library
if [ -d /opt/mint/server/lib ]; then
	rm -rfv /opt/mint/server/lib
fi
if [ -d /opt/mint/server/plugins ]; then
	rm -rfv /opt/mint/server/plugins
fi