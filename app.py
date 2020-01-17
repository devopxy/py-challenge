
import sys  
import os
import json

print("Please Enter The Path of Data Directory")
path= input() # Feature : Check the path if exist exception handling 

files = []  # Initialising the list of files in the given path

# Scanning file in the path and populating the lisr=root, d=directories, f = files
for r, d, f in os.walk(path):
  for file in f:
    if '.data.json' in file:
       files.append(os.path.join(r, file))

seqlen_tot = 0 # Initialising the seqlen values total 

for f in files:
  json_file = open(f,"r")
  print("............Parsing File............" +f)
  for line in json_file:
    json_line = json.loads(line)
    seqlen_tot=seqlen_tot + json_line["seqlen"]  # Incrementing seqlen value total

print("..............Total of seqlen values = " + str(seqlen_tot))



