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
    
    def cleanupFiles(self,file_type):
        for folder_path in self.getAllFilePaths(file_type):
            self.deleteAllFilesInFolder(folder_path)
            
    def cleanupForUser(self,user):
        try:
            self.executeCommand('find "' + self.getFolderPath(AbstractSplittedSecret.TYPE_ENCRYPTED) + '" -not -name "*' + str(user) +'*" -type f -print | xargs rm -v')   
        except:
            pass
        self.cleanupFiles(AbstractSplittedSecret.TYPE_DECRYPTED)

    def deleteAll(self):
        self.cleanupFiles(AbstractSplittedSecret.TYPE_ENCRYPTED)
        self.cleanupFiles(AbstractSplittedSecret.TYPE_DECRYPTED)