from src.base import *
import subprocess
        
 
class Copy:
    origins = []
    destinations = []
    rsync_cmd = ""
    rsync_vars = [] 
    use_batch = False
    def __init__(self, rsync_cmd, use_batch):
        self.rsync_cmd = rsync_cmd
        self.use_batch = use_batch 
    def add_origin(NPWrap):
        if not origins:
            origins.append(NPWrap)
        else:
            exit("currently we do not allow adding more than one origin")
    def add_destination(NPWrap):
        destinations.append(NPWrap)
    def execute_copy():
        for org in self.origins:
            for dest in self.destinations:
                o_path = org.get_path()
                d_path = dest.get_path()
                bashcommand = self.rsync_cmd + 
                for


    def rproc(bashcommand):
        process = subprocess.Popen(bashcommand.split(), stdout=subprocess.PIPE)
        output = process.communicate()[0]
        return output 



