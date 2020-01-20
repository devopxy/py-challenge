#!/bin/bash

DATAPATH="./data"

python3 app.py -p $DATAPATH

python3 test.py -p $DATAPATH
