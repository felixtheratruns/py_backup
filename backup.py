#!/usr/bin/python
from src.formatter import Formatter 
import json
import pprint as pp


def value_list(x):
    if isinstance(x, dict):
        return True
    elif isinstance(x, str):
        return False
    else:
        return False

def r_dict(i,data):
    if value_list(data) is False:
        return    
    pretty=pp.PrettyPrinter(indent=i, width=1)
    pretty.pprint("")
    pretty.pprint(". . . level")
    for key in data.keys():
        pretty.pprint("")
        pretty.pprint("item")
        key_p="key: "+key+"end"
        pretty.pprint(key_p)
        val_p="val: "+str(data[key])+"endval"
        pretty.pprint(val_p)
        r_dict(i+12,data[key])    

with open('user_variables.json') as data_file:    
    data = json.load(data_file)

    pretty = Formatter()
    print(pretty(data));

#    r_dict(9,data)
#    for val in data.values():
#        print(val)
        
#    pprint(data.items()) 
#    print(data.items()) 
#    print(type(data))
#    print(dir(data))
    


#    for thing in data.items():
#        print(type(thing))
#        print('keys')
#        for key in thing:
#            print(thing[key]) 
  
    
 
#    other_copying = data.   
#    for i in other_copying
    

#    data.dumps()


#pprint(data)



#bashCommand = "cwm --rdf test.rdf --ntriples > test.nt"
#import subprocess
#process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
#output, error = process.communicate()
    
