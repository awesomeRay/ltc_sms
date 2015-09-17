#!/bin/bash
# -u参数，使得python不启用缓冲, 否则不能马上看到print的内容
nohup python -u src/main.py > nohup.log 2>&1 &