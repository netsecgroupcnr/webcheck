#!/bin/bash

# This program is created by NetSec group of CNR-IEIIT: http://www.netsec.ieiit.cnr.it
# Original GitHub page for the is https://github.com/netsecgroupcnr/webcheck

if [ `whoami` != root ]; then
	echo "Run the program as root"
	exit 0
fi

D="/root/webcheck/"
cd "$D"
while [ 1 ]; do
	N=`netstat -napt | grep ":80\ " | grep apache2 | grep ESTA | wc -l`
	rm tmpstatus.txt 2> /dev/null
	cp status.txt tmpstatus.txt
	tail tmpstatus.txt -n 59 > status.txt
	echo $N >> status.txt
	sleep 1
done
