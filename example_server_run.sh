#!/bin/sh
# Serves OneMax in dimension 10 on the named pipes query and reply; then run: python3 example_client.py query reply
mkfifo query reply
./build/ioh-server --type integer --problem OneMax --instance 1 --dimension 10 query reply
