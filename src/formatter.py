class Formatter(object):
    def __init__(self):
        self.types = {}
        self.htchar = '\t'
        self.lfchar = '\n'
        self.indent = 0
        self.set_formater(object, self.__class__.format_object)
        self.set_formater(dict, self.__class__.format_dict)
        self.set_formater(list, self.__class__.format_list)
        self.set_formater(tuple, self.__class__.format_tuple)

    def set_formater(self, obj, callback):
        self.types[obj] = callback

    def __call__(self, value, **args):
        for key in args:
            setattr(self, key, args[key])
        formater = self.types[type(value) if type(value) in self.types else object]
        return formater(self, value, self.indent)

    def format_object(self, value, indent):
        return repr(value)

    def format_dict(self, value, indent):
        items = [
            self.lfchar + self.htchar * (indent + 1) + repr(key) + ': ' +
            (self.types[type(value[key]) if type(value[key]) in self.types else object])(self, value[key], indent + 1)
            for key in value
        ]
        return '{%s}' % (','.join(items) + self.lfchar + self.htchar * indent)

    def format_list(self, value, indent):
        items = [
            self.lfchar + self.htchar * (indent + 1) + (self.types[type(item) if type(item) in self.types else object])(self, item, indent + 1)
            for item in value
        ]
        return '[%s]' % (','.join(items) + self.lfchar + self.htchar * indent)

    def format_tuple(self, value, indent):
        items = [
            self.lfchar + self.htchar * (indent + 1) + (self.types[type(item) if type(item) in self.types else object])(self, item, indent + 1)
            for item in value
        ]
        return '(%s)' % (','.join(items) + self.lfchar + self.htchar * indent)


#To initialize it :
#
#pretty = Formatter()
#It can support the addition of formatters for defined types, you simply need to make a function for that like this one and bind it to the type you want with set_formater :
#
#from collections import OrderedDict
#
#def format_ordereddict(self, value, indent):
#    items = [
#        self.lfchar + self.htchar * (indent + 1) +
#        "(" + repr(key) + ', ' + (self.types[
#            type(value[key]) if type(value[key]) in self.types else object
#        ])(self, value[key], indent + 1) + ")"
#        for key in value
#    ]
#    return 'OrderedDict([%s])' % (','.join(items) +
#           self.lfchar + self.htchar * indent)
#pretty.set_formater(OrderedDict, format_ordereddict)
#For historical reasons, I keep the previous pretty printer which was a function instead of a class, but they both can be used the same way, the class version simply permit much more :
#
#def pretty(value, htchar='\t', lfchar='\n', indent=0):
#    nlch = lfchar + htchar * (indent + 1)
#    if type(value) is dict:
#        items = [
#            nlch + repr(key) + ': ' + pretty(value[key], htchar, lfchar, indent + 1)
#            for key in value
#        ]
#        return '{%s}' % (','.join(items) + lfchar + htchar * indent)
#    elif type(value) is list:
#        items = [
#            nlch + pretty(item, htchar, lfchar, indent + 1)
#            for item in value
#        ]
#        return '[%s]' % (','.join(items) + lfchar + htchar * indent)
#    elif type(value) is tuple:
#        items = [
#            nlch + pretty(item, htchar, lfchar, indent + 1)
#            for item in value
#        ]
#        return '(%s)' % (','.join(items) + lfchar + htchar * indent)
#    else:
#        return repr(value)
#To use it :
#
#>>> a = {'list':['a','b',1,2],'dict':{'a':1,2:'b'},'tuple':('a','b',1,2),'function':pretty,'unicode':u'\xa7',("tuple","key"):"valid"}
#>>> a
#{'function': <function pretty at 0x7fdf555809b0>, 'tuple': ('a', 'b', 1, 2), 'list': ['a', 'b', 1, 2], 'dict': {'a': 1, 2: 'b'}, 'unicode': u'\xa7', ('tuple', 'key'): 'valid'}
#>>> print(pretty(a))
#{
#    'function': <function pretty at 0x7fdf555809b0>,
#    'tuple': (
#        'a',
#        'b',
#        1,
#        2
#    ),
#    'list': [
#        'a',
#        'b',
#        1,
#        2
#    ],
#    'dict': {
#        'a': 1,
#        2: 'b'
#    },
#    'unicode': u'\xa7',
#    ('tuple', 'key'): 'valid'
#}

#Compared to other versions :
#
#This solution looks directly for object type, so you can pretty print almost everything, not only list or dict.
#Doesn't have any dependancy.
#Everything is put inside a string, so you can do whatever you want with it.
#The class and the function has been tested and works with Python 2.7 and 3.4.
#You can have all type of objects inside, this is their representations and not theirs contents that being put in the result (so string have quotes, Unicode string are fully represented ...).
#With the class version, you can add formatting for every object type you want or change them for already defined ones.
#key can be of any valid type.
#Indent and Newline character can be changed for everything we'd like.
#Dict, List and Tuples are pretty printed.
