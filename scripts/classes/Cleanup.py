from .AbstractSplittedSecret import AbstractSplittedSecret
class Cleanup(AbstractSplittedSecret):
    def __init__(self):
        super(Cleanup, self).__init__()
        
    def getAllFilePaths(self,file_type):
        all_file_paths = [
            self.getGroupFilesFolderPath(file_type),
            self.getUserFilesFolderPath(file_type),
            self.getAccumulatedFilePath(file_type)
            ]
        if file_type == AbstractSplittedSecret.TYPE_DECRYPTED:
            all_file_paths.append(self.getDecryptedMainDataStandartFolder())
        return all_file_paths
    
    def deleteAllFilesInFolder(self,folder_path):
        try:
            self.executeCommand('rm -r ' + folder_path + '*')
        except Exception as error:
            print(error)
    
    def cleanupFiles(self,file_type):
        for folder_path in self.getAllFilePaths(file_type):
            self.deleteAllFilesInFolder(folder_path)
            
    def cleanupForUser(self,user):
        try:
            self.executeCommand('find "' + self.getDataFolderPath(AbstractSplittedSecret.TYPE_ENCRYPTED) + '" -not -name "*' + str(user) +'*" -type f -print | xargs rm -v')   
        except Exception as error:
            print(error)
        self.cleanupFiles(AbstractSplittedSecret.TYPE_DECRYPTED)

    def deleteAll(self):
        self.cleanupFiles(AbstractSplittedSecret.TYPE_ENCRYPTED)
        self.cleanupFiles(AbstractSplittedSecret.TYPE_DECRYPTED)