from .AbstractSplittedSecret import AbstractSplittedSecret
class Decryption(AbstractSplittedSecret):
    
    def __init__(self):
        self.user_id='0';
        self.user_password=''
        super(Decryption, self).__init__()
    
    def setUserId(self,user_id):
        self.user_id=str(user_id)
    
    def setUserPassword(self,user_password):
        self.user_password = str(user_password)
    
    def decryptFile(self,password,input_file_path,output_file_path):
        self.executeCommand('gpg --batch --passphrase "'+ password + '" -o "' + output_file_path +'" "'+ input_file_path+'"')
    
    def decryptUserFile(self):
        input_file_path = self.getUserFilePath(self.user_id,"encrypted")
        output_file_path = self.getUserFilePath(self.user_id,"decrypted")
        self.decryptFile(self.user_password, input_file_path, output_file_path)
        
    def decryptAccumulatedFile(self):
        input_file_path = self.getAccumulatedFilePath("encrypted")
        output_file_path = self.getAccumulatedFilePath("decrypted")
        self.decryptFile(self.user_password, input_file_path, output_file_path)