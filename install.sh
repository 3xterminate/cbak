#!/bin/bash
dir=$(dirname "$0")
cd $dir

sudo cp cbak.py /usr/bin/cbak
sudo chmod +x /usr/bin/cbak
