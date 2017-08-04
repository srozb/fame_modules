#!/bin/bash

MODULE_DIR="fame/modules/srozb/processing"

pip3 install acefile

pwd
gcc $MODULE_DIR/decoder.c -o $MODULE_DIR/decoder
