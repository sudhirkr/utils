import pandas as pd
from itertools import chain, starmap
import json
import os
import argparse

def process_json(inpf, outpf):
    try:
        fpw = open(outpf, 'w')
    except:
        print ("error in opening file to append")
        exit(1)
    
    try:
        with open (inpf) as fp:
            for cnt, line in enumerate(fp):
                
                processed_doc = {}
                print("{}".format(line))
                doc = json.loads(line)
                print ("dict1 = ", doc)

                for k, v in doc.items():
                    k = k.lower()
                    k = k.replace(" ", "_")
                    if k == "entity_type":
                        processed_doc.update({"type":v})

                    if isinstance(v, list):
                        v = " | ".join([str(elem) for elem in v])
                    processed_doc.update({k: v})

                print (json.dumps(processed_doc))
                json.dump(processed_doc, fpw)
                fpw.write(",")
                fpw.write("\n")
                #df = pd.Series(dict2).to_frame()
                #print (df.head(10))
    finally:
        fp.close()
        fpw.close()

def read_json(fname):
    inpf = fname
    outpf = "outfile.json"
    process_json(inpf, outpf)
    
if __name__ == '__main__':
    ap = argparse.ArgumentParser()                                              
                 
    ap.add_argument("-f", "--file", help="path to the json file")       
         
    args = vars(ap.parse_args())                                                
    working_dir = os.path.dirname(os.path.abspath(__file__))                    
                                                                                
    if args["file"]:                              
        read_json(args["file"])                 
    else:                                                                       
        print("python prog_name [-f <json file>")    
    
