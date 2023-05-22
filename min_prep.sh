#!/usr/bin/bash

awk -f ../code/min_prep.awk $1 | uniq > out.txt
