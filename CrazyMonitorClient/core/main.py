# -*- coding: utf-8 -*-



class command_handler(object):

    def __init__(self, sys_args):
        self.sys_args = sys_args
        self.command_allowcator()

    def command_allowcator(self):

       # print(self.sys_args)

        if hasattr(self,self.sys_args[1]):
            func = getattr(self,self.sys_args[1])
            return func()

        else:
            print ("Command does not exist")

    def help_msg(selfs):
        valid_commands = """
        start  start momitor client
        stop   stop  monitor client
        """
        exit(valid_commands)


    def start(self):
        print ("going to start the monitor client")


    def stop(self):
        print ("stopping the monitor client")