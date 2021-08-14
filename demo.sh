#!/usr/bin/env bash

PASSWORD=.2/lor.SedutperspiciDndeomnis
INPUT=env/2020.04.05-04.46.mp4

python encrypt.py $PASSWORD $INPUT $INPUT.aes
python decrypt.py $PASSWORD $INPUT.aes $INPUT.dec

md5sum $INPUT
md5sum $INPUT.dec
