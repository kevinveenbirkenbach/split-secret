# This class offers easy logik to execute cli commands
# @author Kevin Veen-Birkenbach [kevin@veen.world]

import subprocess

class Cli():
    
    def __init__(self):
        self.command = ''
        self.output  = []
        pass
    
    def executeCommand(self,command):
        self.command = command
        process = subprocess.Popen([command], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        out, err = process.communicate()
        stdout = out.splitlines()
        self.output = []
        for line in stdout:
            self.output.append(line.decode("utf-8"))
        if process.wait() > bool(0):
            print(command, out, err)
            raise Exception("Exitcode is greater then 0")
        return self.output
    
    def getOutputString(self):
        return str(' '.join(self.output))

    def getCommandString(self):
        return self.command