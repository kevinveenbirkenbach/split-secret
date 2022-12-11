import json
from pathlib import Path

class Decryption():
    
    def __init__(self,cli,paths):
        self.user_id='0';
        self.user_password=''
        self.cli = cli
        self.paths = paths
    
    def initializeUser(self,user_id):
        self.user_id=str(user_id)
        self.user_file_decrypted_path = self.paths.getUserFilePath(self.user_id,self.paths.TYPE_DECRYPTED)

    def initializeUserDataDecryption(self):
        self.decryptUserFile()
        self.user_data = self.loadJsonFile(self.user_file_decrypted_path)
        self.initializeNeededDecryptersAmount()
        self.initializeValidDecrypterIds()
    
    def initializeGroupDataEncryption(self):
        self.group_name = self.getDecryptersGroupName()
        self.encrypted_group_file_path = self.paths.getGroupFilePath(self.group_name, self.paths.TYPE_DECRYPTED)
        self.decryptGroupFile()
        self.master_password = self.loadTxtFile(self.encrypted_group_file_path).strip()

    def initializeNeededDecryptersAmount(self):
        self.needed_decrypters_amount = len(str(list(self.user_data['groups'].keys())[0]))
    
    def initializeValidDecrypterIds(self):
        self.valid_decrypter_ids = []
        self.valid_decrypter_ids.append(int(self.user_id))
        for contact_id in self.user_data['contacts']:
            self.valid_decrypter_ids.append(int(contact_id)) 
    
    def setUserPassword(self,user_password):
        self.user_password = str(user_password)
        
    def resetDecrypterIds(self):
        self.decrypter_ids = []
        self.addDecrypterId(self.user_id)
        
    def resetPasswordShare(self):
        self.password_parts = {}
        self.addPasswordShare(self.user_id,self.getPasswordShare())

    def addPasswordShare(self,user_id,password_share):
        self.password_parts[str(user_id)] = password_share
        
    def getGroupPassword(self):
        shared_password = ''
        for password_share_index in sorted(self.password_parts):
            shared_password += str(self.password_parts[password_share_index])
        return shared_password
    
    def getMasterPassword(self):
        return self.master_password
    
    def addDecrypterId(self,decrypter_id):
        decrypter_id = int(decrypter_id)
        if decrypter_id not in self.valid_decrypter_ids:
            raise Exception("The encrypter id is not valid. Valid encrypter ids are: " + str(self.valid_decrypter_ids))
        if len(self.decrypter_ids) >= self.needed_decrypters_amount:
            raise Exception("There are already sufficients decrypters (" + str(len(self.decrypter_ids)) + ") defined!")
        if decrypter_id in self.decrypter_ids:
            raise Exception("The decrypter is already in the list.")
        self.decrypter_ids.append(decrypter_id)
    
    def getUserId(self):
        return self.user_id
    
    def getCoDecrypterIds(self):
        co_decrypter_ids = self.decrypter_ids[:]
        co_decrypter_ids.remove(int(self.user_id))
        return co_decrypter_ids
    
    def getDecrypterIds(self):
        return self.decrypter_ids
    
    def getDecryptersGroupName(self):
        self.decrypter_ids.sort()
        return ''.join(str(x) for x in self.decrypter_ids)
    
    def getPasswordShare(self):
        return self.user_data['groups'][str(self.getDecryptersGroupName())]
        
    def getNeededDecryptersAmount(self):
        return self.needed_decrypters_amount
    
    def loadTxtFile(self,file_path):
        return Path(file_path).read_text()
    
    def loadJsonFile(self,file_path):
        file = open(file_path)
        data = json.load(file)
        file.close()
        return data
    
    def decryptFile(self,password,input_file_path,output_file_path):
        self.cli.executeCommand('gpg --batch --passphrase "'+ password + '" -o "' + output_file_path +'" "'+ input_file_path+'"')
    
    def decryptUserFile(self):
        input_file_path = self.paths.getUserFilePath(self.user_id,self.paths.TYPE_ENCRYPTED)
        self.decryptFile(self.user_password, input_file_path, self.user_file_decrypted_path)
        
    def decryptGroupFile(self):
        input_file_path = self.paths.getGroupFilePath(self.group_name, self.paths.TYPE_ENCRYPTED)
        self.decryptFile(self.getGroupPassword(), input_file_path, self.encrypted_group_file_path)
        
    def decryptAccumulatedFile(self):
        input_file_path = self.paths.getAccumulatedFilePath(self.paths.TYPE_ENCRYPTED)
        output_file_path = self.paths.getAccumulatedFilePath(self.paths.TYPE_DECRYPTED)
        self.decryptFile(self.user_password, input_file_path, output_file_path)
    
    def decryptMainData(self):
        self.cli.executeCommand('gpg --batch --passphrase "' + self.getMasterPassword() + '" -d "' + self.paths.getEncryptedMainDataFile() + '" | tar --one-top-level="' + self.paths.getDecryptedMainDataStandartFolder() + '" -xvzf -')