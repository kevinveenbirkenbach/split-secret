from .Cli import Cli

class AbstractSplittedSecret(Cli):
    
    def __init__(self):
        super(Cli, self).__init__()
        self.data_folder = "data/"
    
    def getFolderPath(self,folder_type):
        return self.data_folder + folder_type + "/"
    
    def getGroupFilesFolderPath(self,folder_type):
        return self.getFolderPath(folder_type) + "group_files/"
    
    def getUserFilesFolderPath(self,folder_type):
        return self.getFolderPath(folder_type) + "user_files/"
    
    def getFileExtension(self,file_type):
        if file_type == "encrypted":
            return '.gpg'
        return ''
    
    def getUserFilePath(self,user_id,file_type):
        return self.getUserFilesFolderPath(file_type)+user_id+'.json' + self.getFileExtension(file_type);
    
    def getGroupFilePath(self,group_id,file_type):
        return self.getGroupFilesFolderPath(file_type) + str(group_id) + '.txt' + self.getFileExtension(file_type);
    
    def getAccumulatedFilePath(self,file_type):
        return self.getFolderPath(file_type) + 'accumulated.json' + self.getFileExtension(file_type);