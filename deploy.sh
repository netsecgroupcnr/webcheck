#!/bin/bash

if [ "$#" != "1" ]; then
	echo "Usage: $0 <comment>"
	exit 0
fi

git add .
git commit -m "$1"
git push -f origin master
