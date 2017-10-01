from pathlib import Path
from enum import Enum
from collections import OrderedDict
from src.base import * 
import os
from inspect import currentframe, getframeinfo

class NodeType(Enum):
    source = 1
    destination = 2
    __str__ = lambda self: NodeType._value_to_str.get(self)

# define after Types class
NodeType.__new__ = lambda cls, value: (cls._str_to_value.get(value)
                                    if isinstance(value, str) and value in cls._str_to_value else
                                    super(NodeType, cls).__new__(cls, value))

# define look-up table and its inverse
NodeType._str_to_value = OrderedDict((('source', NodeType.source),
                                    ('destination', NodeType.destination),))
NodeType._value_to_str = {val: key for key, val in NodeType._str_to_value.items()}
NodeType._str_to_value = dict(NodeType._str_to_value) # convert to regular dict (optional)


class PathType(Enum):
    relative = 1
    absolute = 2
    __str__ = lambda self: PathType._value_to_str.get(self)

# define after PathType class
PathType.__new__ = lambda cls, value: (cls._str_to_value.get(value) 
                                    if isinstance(value, str) and value in cls._str_to_value else
                                    super(PathType, cls).__new__(cls, value))

# define look-up table and its inverse
PathType._str_to_value = OrderedDict((('relative', PathType.relative),
                                    ('absolute', PathType.absolute),))
PathType._value_to_str = {val: key for key, val in PathType._str_to_value.items()}
PathType._str_to_value = dict(PathType._str_to_value) # convert to regular dict (optional)

#
#class PathType(Enum):
#    relative = 1
#    absolute = 2
#    def dude_make_class(cls,name):
#        print('constructor')
#        for pt in cls:
#            if pt.name == name:
#                return PathType(pt.value) 

#    def __new__(self,value):
#        print('constructor')
#        print('yes',self.value)
#        return type(self)(self,1)        
#
#    def __init__(self,value):
#        print('constructor')
#        print('yes',self.value)
#        return type(self)(self,1)        
#    def__new(
#    def make(cls,value):
#        return type(self)(cls.value)

class NodePath:
    def __init__(self, path, path_type, node_type):
        self.set_path(path)
        self.set_path_type(path_type)
        self.set_node_type(node_type)

    def __init__(self, path, path_type, node_type, create_if_not_exist):
        self.set_path(path)
        self.set_path_type(path_type)
        self.set_node_type(node_type)
        self.set_create_if_not_exist(create_if_not_exist)

    def set_create_if_not_exist(self, cne):
        self.create_if_not_exist=cne

    def get_create_if_not_exist():
        return self.create_if_not_existt

    def set_path_type(self, path_type):
        if isinstance(path_type, PathType):
            self.path_type=path_type
        else:
            exit('fail,',path_type,'type:',type(path_type),'not of type PathType')
    def get_path_type(self):
        return self.path_type

    def set_path(self, path):
        if isinstance(path, Path):
            self.path=path
        else:
            exit('fail,',path,'type:',type(path),'not of type Path')
    def get_path(self):
        return self.path

    def set_node_type(self, node_type):
        if isinstance(node_type, NodeType):
            self.node_type=node_type
        else:
            exit('fail,', node_type, 'type:',type(node_type),'not of type PathType')
    def get_node_type(self):
        return self.node_type


class NPWrap(object):
    def __init__(self, wrapped_NodePath, path_type, path, base_path, node_type, create_if_not_exist=False):
        invalid_mess="invalid, path is not relative nor absolute"
        if create_if_not_exist:
            dne_mess="(does not exist), will be created"
        else:
            dne_mess="WARNING: does not exist"

        path_type = PathType(path_type)
        path = Path(path)
        base_path=Path(base_path)
        node_type = NodeType(node_type)
        if path_type.name == 'relative':
            path = self.join_paths(base_path,path)
            self.does_it_exist(path,dne_mess=dne_mess)
        elif path_type.name == 'absolute':
            self.does_it_exist(path,dne_mess=dne_mess)
        else:    
            exit(invalid_mess)
        #fix order here:

        self.wrapped_NodePath = wrapped_NodePath(path, path_type, node_type, create_if_not_exist)
    def join_paths(self,first_path,second_path):
       first_path=os.path.abspath(first_path)
       return Path(os.path.join(first_path,second_path))
    def does_it_exist(self, path, e_mess='(exists)', dne_mess="(WARNING: doesn't exist)", exit_on_dne=False, file_mess="(is a file not a directory)"):
        if type(path) is not type(Path('')):
            exit('error object is not type Path, it is instead type:',path.__class__)
        if path.is_dir():
            print('Directory: ',path,e_mess)  
        elif path.is_file():
            print('File: ',path,file_mess)
        else:
            print('Path: ',path,dne_mess)
            if exit_on_dne:
               exit("path: '",path,"' is not dir or file, looks like it doesn't exist")
    def __getattr__(self,attr):
        orig_attr = self.wrapped_NodePath.__getattribute__(attr)
        if callable(orig_attr):
            def hooked(*args, **kwargs):
                result = orig_attr(*args, **kwargs)
                #prevent wrapped_class from becomming unwrapped
                if result == self.wrapped_NodePath:                
                    return self
                return result
            return hooked
        else:
            return orig_attr

           
#    def print_text_path_for_copy(path_type,path,base_path,invalid_mess):
#        #directory=Path(direct)
#        if path_type == 'relative':
#            directory = join_text_paths(base_path,path)
#            does_it_exist(directory) 
#        elif path == 'absolute':
#            path=Path(path)
#            does_it_exist(path)
#        else:
#            exit()


#    def __init__(self,path,path_type,node_type):
#        self.path=path
#        self.path_type=path_type
#        self.node_type=node_type


#np1 = NodePath(Path("/data"),1)
#np2 = NodePath(Path("/data"),2)
#print(np1.path_type)
#print(np2.path_type)
#if __name__ == '__main__':
#    print("PathType('absolute')  ->", PathType('absolute'))   # PathType('absolute')  -> nl
#    print("PathType('relative') ->", PathType('relative'))  # PathType('relative') -> nl
#
#    print()
#    print(list(PathType))  # iterate values
#
#    import pickle  # demostrate picklability
#    print(pickle.loads(pickle.dumps(PathType.absolute)) == PathType.absolute)  # -> True
#
#    np1 = NodePath(Path("/data"),PathType('relative'))
#    np2 = NodePath(Path("/data"),PathType('absolute'))
#    np3 = NodePath(Path("/data"),PathType('aoeuabsolute'))
#    print(np1.path_type)
#    print(np2.path_type)
#    print(np3.path_type)

