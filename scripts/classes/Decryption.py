from .AbstractSplittedSecret import AbstractSplittedSecret
class Decryption(AbstractSplittedSecret):
    
    def __init__(self):
        self.user_id='0';
        self.user_password=''
        pass
    
    def setUserId(self,user_id):
        self.user_id=str(user_id)
    
    def setUserPassword(self,user_password):
        self.user_password = str(user_password)
    
    def decryptFile(self,password,input_file_path):
        self.executeCommand('gpg --batch --passphrase "'+ password + '" '+ file_path)
        print(self.getCommandString())
        print(self.getOutputString())
    
    def decryptUserFile(self):
        input_file_path = self.getUserFilePath(self.user_id)
        self.decryptFile(self.user_password, file_path)
        