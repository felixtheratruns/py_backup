#!/usr/bin/python
from src.formatter import Formatter 
import json
import pprint as pp
import subprocess
from pathlib import Path
import os
import sys
from src.node_path import NodePath
import src.base 

#maybe make the origin path, and destination path, and ancillary paths a class type that contains the information that will be passed to the des_it_exist function automatically



def rproc(bashcommand):
    process = subprocess.Popen(bashcommand.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    return output 


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

def join_text_paths(first_path,second_path):
    first_path=os.path.abspath(first_path)
    return Path(os.path.join(first_path,second_path))
   
def does_it_exist(path,e_mess='(exists)',dne_mess="(WARNING: doesn't exist)",exit_on_dne=False,file_mess="(is a file not a directory)"):
    if type(path) is not type(Path('')):
        print('error object is not type Path, it is instead type:',path.__class__)
        exit()
    if path.is_dir():
        print('Directory: ',path,e_mess)  
    elif path.is_file():
        print('File: ',path,file_mess)
    else:
        print('Path: ',path,dne_mess)
        if exit_on_dne:
            exit()
 
with open('user_variables.json') as data_file:    
    data = json.load(data_file)

    #print(pretty(data));
    #print(data['backup_folders']['sub_copying'])

def print_text_path_for_copy(path_type,path,base_path,invalid_mess):
    #directory=Path(direct)
    if path_type == 'relative':
        directory = join_text_paths(base_path,path)
        does_it_exist(directory) 
    elif path == 'absolute':
        path=Path(path)
        does_it_exist(path)
    else:
        exit()

print('Ancillary copying happens first.')
for value in data['ancillary_copying']:
    print(">Will copy")
    path_type=value['src_path_type']
    path=value['src_path']
    base_path=data['base_paths']['ancillary_copying_base']
    print_text_path_for_copy(path_type,path,base_path,'src_path_type invalid')
    print(">to")
    path_type=value['dest_path_type']
    path=value['dest_path']
    base_path=data['base_paths']['ancillary_copying_base']
    print_text_path_for_copy(path_type,path,base_path,'dest_path_type invalid')
    print('')

#I am replacing this with two "print_text_path_for_copy" functions
#    print('Will copy:')
#    if value['src_path_type'] == 'relative':
#        b_p=data['base_paths']['ancillary_copying_base']
#        directory = join_text_paths(b_p,value['src_path'])
#        does_it_exist(directory) 
#    elif value['src_path_type'] == 'absolute':
#        path=Path(value['src_path'])
#        does_it_exist(path)
#    else:
#        print('src_path_type invalid')
#        sys.exit()
#    print('to')
#    if value['dest_path_type'] == 'relative':
#        b_p=data['base_paths']['ancillary_copying_base']
#        directory = join_text_paths(b_p,value['dest_path'])
#        does_it_exist(directory,dne_mess="(doesn't exist, will be created)") 
#    elif value['dest_path_type'] == 'absolute':
#        path=Path(value['dest_path'])
#        does_it_exist(path,dne_mess="(doesn't exist, will be created)")
#    else:
#        print('dest_path_type invalid')
#        sys.exit()

print("")
print("Then script will copy origin to destinations.")
print('>Will copy')
origin_path_type=data['origin']['path_type']
origin_path=data['origin']['path']
origin_base_path=data['base_paths']['origin_base']
print_text_path_for_copy(origin_path_type,origin_path,origin_base_path,'destination_path_type invalid')
print('>to')
destination_base_path=data['base_paths']['origin_base']
for value in data['origin']['destinations']:
    destination_path_type=value['path_type']
    destination_path=value['path']
    print_text_path_for_copy(destination_path_type,destination_path,destination_base_path,'destination_path_type invalid')


    

#for value in data['origin']['destinations']:
#    #direct=os.path.join(base_path,value['src_path'])
#    #directory=Path(direct)
#    print('Will copy:')
#    if value == 'relative':
#        b_p=data['base_paths']['ancillary_copying_base']
#        directory = join_text_paths(b_p,value['src_path'])
#        does_it_exist(directory) 
#    elif value['src_path_type'] == 'absolute':
#        path=Path(value['src_path'])
#        does_it_exist(path)
#    else:
#        print('src_path_type invalid')
#        sys.exit()
#    print('to')
#    if value['dest_path_type'] == 'relative':
#        b_p=data['base_paths']['ancillary_copying_base']
#        directory = join_text_paths(b_p,value['dest_path'])
#        does_it_exist(directory,dne_mess="(doesn't exist, will be created)") 
#    elif value['dest_path_type'] == 'absolute':
#        path=Path(value['dest_path'])
#        does_it_exist(path,dne_mess="(doesn't exist, will be created)")
#    else:
#        print('dest_path_type invalid')
#        sys.exit()




# for value in data['']['']:
    
    

    
#pretty = Formatter()
#print(pretty(data))



#moo=rproc("echo 'testing with people is great'")
#print("output",moo)

#r_dict(9,data)
#for val in data.values():
#    print(val)
    
#pprint(data.items()) 
#print(data.items()) 
#print(type(data))
#print(dir(data))
 


#for thing in data.items():
#    print(type(thing))
#    print('keys')
#    for key in thing:
#        print(thing[key]) 
 
 
 
#sub_copying = data.   
#for i in sub_copying
 

#data.dumps()


#pprint(data)



#bashCommand = "cwm --rdf test.rdf --ntriples > test.nt"
#import subprocess
#process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
#output, error = process.communicate()
    
