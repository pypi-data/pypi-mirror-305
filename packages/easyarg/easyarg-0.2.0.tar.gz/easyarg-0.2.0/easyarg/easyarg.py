import sys
class AGR:
    def __init__(self):
        self.list_arg={}
    def add_agr(self,flag,action='agr',default=None):
        if action=='agr':
            if default:
                self.list_arg[flag]=default
            else:
                self.list_arg[flag]=None
        elif action=='store_true':
            self.list_arg[flag] = False
        else:
            print('Action not found,action="agr" or action="store_true"')
    def parse_agrs(self):
        for arg in sys.argv:
            if arg in self.list_arg:
                if self.list_arg[arg] == False:
                    self.list_arg[arg] =True
                elif self.list_arg[arg] == None:
                    try:
                        if not sys.argv[sys.argv.index(arg)+1].startswith('-'):
                            self.list_arg[arg]=sys.argv[sys.argv.index(arg)+1]
                        else:
                            print(f'Parameter {arg} has arguments that do not start with -')
                    except:
                        print(f'Parameter {arg} is missing an argument')
                else:
                    try:
                        if not sys.argv[sys.argv.index(arg)+1].startswith('-'):
                            self.list_arg[arg]=sys.argv[sys.argv.index(arg)+1]
                        else:
                            print(f'Parameter {arg} has arguments that do not start with -')
                    except:
                        pass

    def get_value(self,flag):
        return self.list_arg[flag]


