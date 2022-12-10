from .Cli import Cli

class AbstractSplittedSecret(Cli):
    USER_PASSWORD_LENGTHS = 64
    OVERALL_PASSWORD_LENGTHS = 128
    
    # At the moment the programm can only deal with one digit numbers. 
    MAXIMUM_SECRET_HOLDERS = 9
    MINIMUM_SECRET_HOLDERS = 2
    
    TYPE_ENCRYPTED="encrypted"
    TYPE_DECRYPTED="decrypted"
    
    def __init__(self):
        super(Cli, self).__init__()
        self.data_folder = "data/"
    
    def getCoSecretHoldersRange():
        return range(AbstractSplittedSecret.MINIMUM_SECRET_HOLDERS,AbstractSplittedSecret.MAXIMUM_SECRET_HOLDERS)
    
    def getSecretHoldersRange():
        return range(1,AbstractSplittedSecret.MAXIMUM_SECRET_HOLDERS)
    
    def getDataFolderPath(self,folder_type):
        return self.data_folder + folder_type + "/"
    
    def getGroupFilesFolderPath(self,folder_type):
        return self.getDataFolderPath(folder_type) + "group_files/"
    
    def getUserFilesFolderPath(self,folder_type):
        return self.getDataFolderPath(folder_type) + "user_files/"
    
    def getEncryptedMainDataFile(self):
        return self.getDataFolderPath(AbstractSplittedSecret.TYPE_ENCRYPTED) + "main_data.tar.gz.gpg"
    
    def getDecryptedMainDataStandartFolder(self):
        return self.getDataFolderPath(AbstractSplittedSecret.TYPE_DECRYPTED) + "main_data/"
    
    def getFileExtension(self,file_type):
        if file_type == AbstractSplittedSecret.TYPE_ENCRYPTED:
            return '.gpg'
        return ''
    
    def getUserFilePath(self,user_id,file_type):
        return self.getUserFilesFolderPath(file_type)+user_id+'.json' + self.getFileExtension(file_type);
    
    def getGroupFilePath(self,group_id,file_type):
        return self.getGroupFilesFolderPath(file_type) + str(group_id) + '.txt' + self.getFileExtension(file_type);
    
    def getAccumulatedFilePath(self,file_type):
        return self.getDataFolderPath(file_type) + 'accumulated.json' + self.getFileExtension(file_type);