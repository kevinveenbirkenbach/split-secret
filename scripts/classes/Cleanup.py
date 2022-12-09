from .AbstractSplittedSecret import AbstractSplittedSecret
class Cleanup(AbstractSplittedSecret):
    def __init__(self):
        super(Cleanup, self).__init__()
        self.encrypted_files_folders = [self.decrypted_password_files_folder,self.decrypted_password_files_folder]
        self.decrypted_files_folders = [self.encrypted_splitted_password_files_folder,self.encrypted_password_files_folder]
    
    def deleteAllFilesInFolder(self,folder_path):
        try:
            self.executeCommand('rm -v ' + folder_path + '*')
            print(self.getCommandString())
            print(self.getOutputString())
        except:
            pass    
    
    def deleteAllDecryptedFiles(self):
        for folder_path in self.decrypted_files_folders:
            self.deleteAllFilesInFolder(folder_path)
        
    def deleteAllEncryptedFiles(self):
        for folder_path in self.encrypted_files_folders:
            self.deleteAllFilesInFolder(folder_path)

    def deleteAll(self):
        self.deleteAllEncryptedFiles()
        self.deleteAllDecryptedFiles()