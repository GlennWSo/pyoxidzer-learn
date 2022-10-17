#!/usr/bin/env bash

source venv/bin/activate

pyoxidizer build

rsync -a --remove-source-files build/x86_64-unknown-linux-gnu/debug/install/lib/python3.9/site-packages/lib/ build/x86_64-unknown-linux-gnu/debug/install/lib/
