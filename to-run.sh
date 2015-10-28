#!/bin/sh

find ~/work/main/mozilla -name 'mochitest.ini' | xargs ./manifest-parser.py
