from src.base import 


class Copy:
    origins = []
    destinations = []
    def add_origin(NPWrap):
        if not origins:
            origins.append(NPWrap)
        else:
            exit("currently we do not allow adding more than one origin")
    def add_destination(NPWrap):
        destinations.append(NPWrap)
    def execute_copy():
           
