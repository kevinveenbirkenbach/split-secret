import os 

class Paths():
    
    TYPE_ENCRYPTED="encrypted"
    TYPE_DECRYPTED="decrypted" 
    
    ROOT_PATH= os.path.join(os.path.dirname(os.path.abspath(__file__)),"../","../")
    
    def __init__(self):
        self.data_folder = os.path.join(self.ROOT_PATH,"data") + '/'
    
    def getDataFolderPath(self,folder_type):
        return self.data_folder + folder_type + "/"
    
    def getGroupFilesFolderPath(self,folder_type):
        return self.getDataFolderPath(folder_type) + "group_files/"
    
    def getUserFilesFolderPath(self,folder_type):
        return self.getDataFolderPath(folder_type) + "user_files/"
    
    def getEncryptedMainDataFile(self):
        return self.getDataFolderPath(Paths.TYPE_ENCRYPTED) + "main_data.tar.gz.gpg"
    
    def getDecryptedMainDataStandartFolder(self):
        return self.getDataFolderPath(Paths.TYPE_DECRYPTED) + "main_data/"
    
    def getFileExtension(self,file_type):
        if file_type == Paths.TYPE_ENCRYPTED:
            return '.gpg'
        return ''
    
    def getUserFilePath(self,user_id,file_type):
        return self.getUserFilesFolderPath(file_type)+user_id+'.json' + self.getFileExtension(file_type);
    
    def getGroupFilePath(self,group_id,file_type):
        return self.getGroupFilesFolderPath(file_type) + str(group_id) + '.txt' + self.getFileExtension(file_type);
    
    def getAccumulatedFilePath(self,file_type):
        return self.getDataFolderPath(file_type) + 'accumulated.json' + self.getFileExtension(file_type);