#!/bin/bash

docker run \
-d \
-p 0.0.0.0:1883:1883 \
fluent/fluent-bit:1.4.5 \
/fluent-bit/bin/fluent-bit -i mqtt -o stdout -p format=json_lines
