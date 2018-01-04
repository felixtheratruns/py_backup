#!/usr/bin/python
from src.formatter import Formatter 
import json
import pprint as pp
import subprocess
from pathlib import Path
import os
from src.node_path import NPWrap, NodePath
from src.base import * 

#maybe make the origin path, and destination path, and ancillary paths a class type that contains the information that will be passed to the des_it_exist function automatically

def value_list(x):
    if isinstance(x, dict):
        return True
    elif isinstance(x, str):
        return False
    else:
        return False

#def r_dict(i,data):
#    if value_list(data) is False:
#        return    
#    pretty=pp.PrettyPrinter(indent=i, width=1)
#    pretty.pprint("")
#    pretty.pprint(". . . level")
#    for key in data.keys():
#        pretty.pprint("")
#        pretty.pprint("item")
#        key_p="key: "+key+"end"
#        pretty.pprint(key_p)
#        val_p="val: "+str(data[key])+"endval"
#        pretty.pprint(val_p)
#        r_dict(i+12,data[key])    

def ixi_th(data,key):
    #stands for "if exist then" set value
    if key in data:
        return data[key]
    else:
        return None



if __name__ == '__main__':

    full_path = os.path.realpath(__file__)
    with open( os.path.dirname(full_path) + '/user_variables_test.json') as data_file:    
        data = json.load(data_file)
    #print(pretty(data));
    #print(data['backup_folders']['sub_copying'])

    nodes = data["copy"]["nodes"]    

 


    for node in nodes:
        sources=node["sources"]
        destinations=node["destinations"]
        command_order=node["command_order"]
        command_modify=ixi_th(node,"command_modify")
        command=ixi_th(command_modify,"command")
        command_switch_to=ixi_th(command_modify,"command_switch_to")
        at_destination_iteration=ixi_th(command_modify,"at_destination_on_iteration")
            
    exit()


    use_batch = data["origin"]["destinations"]["use_batch"]
    rsync_vars = data["rsync_args"]["rsync_vars"]
    rsync_delete = data["rsync_args"]["rsync_delete"]
    write_batch = data["rsync_args"]["write_batch"]
    command = data["rsync_args"]["command"]


    print('Ancillary copying happens first.')
    anci_copy = Copy 
    for value in data['ancillary_copying']:
        print(">Will copy")
        path_type=value['src_path_type']
        path=value['src_path']
        base_path=data['base_paths']['ancillary_copying_base']
        node_type = 'source'
        create_if_not_exist = False
        node_pathA = NPWrap(NodePath, path_type, path, base_path, node_type, create_if_not_exist)
        print(">to")
        path_type=value['dest_path_type']
        path=value['dest_path']
        base_path=data['base_paths']['ancillary_copying_base']
        node_type = 'destination'
        create_if_not_exist = True
        node_pathB = NPWrap(NodePath,path_type,path,base_path, node_type, create_if_not_exist)
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
    node_type = 'source'
    create_if_not_exist = False
    node_path1 = NPWrap(NodePath, origin_path_type, origin_path, origin_base_path, node_type, create_if_not_exist)
    print('>to')
    destination_base_path=data['base_paths']['origin_base']
    for value in data['origin']['destinations']:
        destination_path_type=value['path_type']
        destination_path=value['path']
        node_type = 'destination'
        create_if_not_exist = False
        node_path2 = NPWrap(NodePath, destination_path_type, destination_path, destination_base_path, node_type, create_if_not_exist)
            


    

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
    
