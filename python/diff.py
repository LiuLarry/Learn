#!/usr/bin/env python
# coding=utf-8

'''
比较git中最近两次提交间的差异
'''
import os
import sys

if len(sys.argv) == 2:
    git_dir = sys.argv[1]
else:
    raise Exception("Should input git repo path.")

os.chdir(git_dir)

proc = os.popen(r"git log | grep -m 2 '^commit' | awk '{ print $2 }' ")

commits = []

for line in proc:
    commits.insert(0, line)

cmd = " ".join(commits)
cmd = "git diff " + cmd

proc = os.popen(cmd)

out = ''
for line in proc:
    out += str(line)

print out

proc.close()
