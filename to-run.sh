#!/bin/sh

find /home/mrbkap/work/main/mozilla -name 'mochitest.ini' | xargs ./manifest-parser.py
