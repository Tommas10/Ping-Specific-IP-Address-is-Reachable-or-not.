#!/usr/bin/env python

#This is small auto Python script file to check if a particular IP address is reachable or not. 
#Created by Tommas Huang 
#Created date: 2019-07-24

import shlex
#The shlex class makes it easy to write lexical analyzers for simple syntaxes resembling that of the Unix shell.
import subprocess
#The subprocess module allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes.

   
cmd=shlex.split("ping -c1 google.com")
# Tokenize the shell command
# cmd will contain  ["ping","-c1","google.com"]  
#The shlex.split() can be useful when determining the correct tokenization for args( for unix shell).
#Yes it can be done without shlex in that case you have to tokenize your command like cmd=["ping","-c1","google.com"] as list and pass to subprocess.check_ouptut this work is done by shlex.split() for you.
try:
   output = subprocess.check_output(cmd)
   #Use the subprocess.check_output() function to store output of a command.
except subprocess.CalledProcessError as e:
   print ("The IP {0} is NotReacahble".format(cmd[-1]))
else:
   print ("The IP {0} is Reachable".format(cmd[-1]))
   #Will print the command failed with its exit status
   