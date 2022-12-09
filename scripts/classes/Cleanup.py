from .AbstractSplittedSecret import AbstractSplittedSecret
class Cleanup(AbstractSplittedSecret):
    
    def __init__(self):
        super(Cleanup, self).__init__()
        
    def getAllFilePaths(self,file_type):
        return [
            self.getGroupFilesFolderPath(file_type),
            self.getUserFilesFolderPath(file_type),
            self.getAccumulatedFilePath(file_type)
            ]
    
    def deleteAllFilesInFolder(self,folder_path):
        try:
            self.executeCommand('rm -v ' + folder_path + '*')
        except:
            pass    
    
    def deleteAllFiles(self,file_type):
        for folder_path in self.getAllFilePaths(file_type):
            self.deleteAllFilesInFolder(folder_path)
        
    def deleteAllEncryptedFiles(self):
        for folder_path in self.encrypted_files_folders:
            self.deleteAllFilesInFolder(folder_path)
            
    def cleanupForUser(self,user):
        self.executeCommand('find "' + self.getFolderPath("encrypted") + '" -not -name "*' + str(user) +'*" -type f -print | xargs rm -v')    

    def deleteAll(self):
        self.deleteAllFiles("encrypted")
        self.deleteAllFiles("decrypted")