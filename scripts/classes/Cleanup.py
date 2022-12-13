from .Paths import Paths

class Cleanup():
    def __init__(self,cli,paths):
        self.cli = cli
        self.paths = paths
    
    def getMetaFilePaths(self,file_type):    
        return [
            self.paths.getGroupFilesFolderPath(file_type),
            self.paths.getUserFilesPath(file_type),
            self.paths.getAccumulatedFilePath(file_type)
        ]
    
    def getAllFilePaths(self,file_type):
        all_file_paths = self.getMetaFilePaths(file_type)
        if file_type == Paths.TYPE_DECRYPTED:
            all_file_paths.append(self.paths.getDecryptedMainDataStandartFolder())
        return all_file_paths
    
    def deleteAllFilesInFolder(self,folder_path):
        try:
            self.cli.executeCommand('rm -r ' + folder_path + '*')
        except Exception as error:
            pass
    
    def cleanupFiles(self,file_type):
        for folder_path in self.getAllFilePaths(file_type):
            self.deleteAllFilesInFolder(folder_path)
            
    def cleanupForUser(self,user):
        try:
            self.cli.executeCommand('find "' + self.paths.getDataFolderPath(Paths.TYPE_ENCRYPTED) + '" -not -name "*' + str(user) +'*" -type f -print | xargs rm -v')   
        except Exception as error:
            pass
        self.cleanupFiles(Paths.TYPE_DECRYPTED)

    def cleanupMetaData(self,file_type):
        for folder_path in self.getMetaFilePaths(file_type):
            self.deleteAllFilesInFolder(folder_path)

    def deleteAll(self):
        self.cleanupFiles(Paths.TYPE_ENCRYPTED)
        self.cleanupFiles(Paths.TYPE_DECRYPTED)