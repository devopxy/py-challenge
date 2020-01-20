import sys  
import os
import json

def calculate(path):
    files = []  # Initialising the list of files in the given path
    sum = "error"
# Scanning file in the path and populating the lisr=root, d=directories, f = files
    try:
        for r, d, f in os.walk(path):
          for file in f:
            if '.data.json' in file:
               files.append(os.path.join(r, file))

        seqlen_tot = 0 # Initialising the seqlen values total 

        if len(files) == 0:
            raise Exception ("No Files or wrong directory")
        for f in files:
          with  open(f,"r") as json_file:
            print("............Parsing File............" +f)
            for line in json_file:
              json_line = json.loads(line)
              seqlen_tot=seqlen_tot + json_line["seqlen"]  # Incrementing seqlen value total

        sum = seqlen_tot
    except:
        print("Exception occured")
    finally:
        return sum
    
if __name__ == '__main__':
    
    sum = calculate(sys.argv[2]) # third commandline argument is our required path
   # 0 sum implies either an exception or file absence
    print("===== seqlen total is :",sum)
