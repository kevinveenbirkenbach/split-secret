from .AbstractSplittedSecret import AbstractSplittedSecret
class Cleanup(AbstractSplittedSecret):
    def __init__(self):
        super(Cleanup, self).__init__()
    def deleteAllEncryptedFiles(self):
        self.executeCommand('rm -v ' + self.decrypted_password_files_folder + '*')
        print(self.getCommandString())
        print(self.getOutputString())
        self.executeCommand('rm -v ' + self.encrypted_splitted_password_files_folder + '*')
        print(self.getCommandString())
        print(self.getOutputString())
    def deleteAll(self):
        self.deleteAllEncryptedFiles()