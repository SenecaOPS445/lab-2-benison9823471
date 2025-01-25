#!/usr/bin/env python3

#Author:Benison Paul Jogi
#Author ID:151649225
#Date Created:2025/01/24

import sys

timer = 3
if len(sys.argv) == 2:
    timer = int(sys.argv[1])

while timer != 0:
    print(timer)
    timer = timer - 1
print('blast off!')