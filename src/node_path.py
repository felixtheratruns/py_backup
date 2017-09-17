from pathlib import Path
from enum import Enum

class NodeType(Enum):
    source = 1
    destination = 2

class PathType(Enum):
    relative = 1
    absolute = 2
    def make_class(cls,name):
        for pt in cls:
            if pt.name == name:
                return PathType(pt.value) 

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
    def __init__(self, path):
        self.path=path
    def __init__(self, path, path_type):
        self.path=path
        self.set_path_type(path_type)
    def set_path_type(self, path_type):
        self.path_type=PathType.make_class(PathType, path_type)
    def get_path_type(self):
        return self.path_type
    def set_path(self,path):
        if type(path) == type(Path()):
            self.path=path
        else:
            print('fail,',path,'not of type Path')
    def get_path(self):
        return self.path
#    def __init__(self,path,path_type,node_type):
#        self.path=path
#        self.path_type=path_type
#        self.node_type=node_type


#np1 = NodePath(Path("/data"),1)
#np2 = NodePath(Path("/data"),2)
#print(np1.path_type)
#print(np2.path_type)
np1 = NodePath(Path("/data"),'relative')
print(np1.path_type)

