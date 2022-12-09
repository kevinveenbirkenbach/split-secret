import random
import string
import math
import numpy
import re
import json
from .AbstractSplittedSecret import AbstractSplittedSecret

class Generate(AbstractSplittedSecret):
    
    def __init__(self, amount_of_secret_holders, decryption_quota,master_password):
        super(Generate, self).__init__()
        self.amount_of_secret_holders = amount_of_secret_holders
        self.decryption_quota = decryption_quota
        self.master_password = master_password
        self.quota_factor=self.decryption_quota/100
        self.group_members_amount=math.ceil(self.amount_of_secret_holders * self.quota_factor)
        
    def getStartnumber(self):
        index = 0
        start_number = ''
        while index < self.group_members_amount:
            start_number += '1'
            index += 1
        return int(start_number)

    def getEndnumber(self):
        index = 0
        start_number = ''
        while index < self.group_members_amount:
            start_number += str(self.amount_of_secret_holders)
            index += 1
        return int(start_number)

    def savePassword(self,password,password_file_path):
        print("Saving password to: " + password_file_path)
        master_password_file = open(password_file_path, "a")
        master_password_file.seek(0)
        master_password_file.truncate()
        master_password_file.write(password)
        master_password_file.close()
    
    def createPassword(self):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for i in range(int(64*self.quota_factor))).upper()
    
    def isGroupValid(self,password_group_index_str):
        secret_stakeholders_range=range(1,(self.amount_of_secret_holders+1))
        valid_numbers = re.compile("([" + ','.join([str(x) for x in secret_stakeholders_range]) + "]{" + str(self.group_members_amount) + "})")
        unvalid_sequenz = re.compile("(.)\\1+")
        return re.search(valid_numbers, password_group_index_str) and not re.search(unvalid_sequenz, password_group_index_str)
    
    def createUserMappedDataFrame(self):
        self.user_mapped_data = {}
        user_count = 1
        while user_count <= self.amount_of_secret_holders:
            self.user_mapped_data[str(user_count)] = {}
            user_count += 1;
    
    def createGroupMappedDataFrame(self):
        self.group_mapped_data = {} 
        
    def generateMappedData(self):
        self.createUserMappedDataFrame()
        self.createGroupMappedDataFrame()
        index = self.getStartnumber()
        while index < self.getEndnumber():
            password_group_index_str = ''.join(sorted(str(index)))
            if self.isGroupValid(password_group_index_str):
                password_group_index_int = int(password_group_index_str)
                if not password_group_index_int in self.group_mapped_data:
                    self.group_mapped_data[password_group_index_int] = {}
                    self.group_mapped_data[password_group_index_int]['members'] = {}
                    self.group_mapped_data[password_group_index_int]['password'] = '' 
                    password = ''
                    for secret_holder_index in password_group_index_str:
                        self.group_mapped_data[password_group_index_int]['members'][secret_holder_index]={}
                        password_part = self.createPassword()
                        self.group_mapped_data[password_group_index_int]['members'][secret_holder_index] = password_part
                        password += password_part
                        self.user_mapped_data[secret_holder_index][password_group_index_str] = password_part
                    self.group_mapped_data[password_group_index_int]['password'] += password
            index += 1
            
    def generateEncryptedGroupFiles(self):
        for password_group_index_int in self.group_mapped_data:
            encrypted_splitted_password_file = AbstractSplittedSecret().encrypted_splitted_password_files_folder + str(password_group_index_int) + ".txt.gpg"
            self.executeCommand('echo "' + self.master_password + '" | gpg --symmetric --armor --batch --passphrase "' + self.group_mapped_data[password_group_index_int]['password'] + '" -o "' + encrypted_splitted_password_file + '"')
            print(self.getCommandString())
    
    def saveJsonFile(self,file_path,data):
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
            
    def saveUserMappedData(self):
        for user_id in self.user_mapped_data:
            file_path=self.decrypted_password_files_folder+user_id+'.json'
            self.saveJsonFile(file_path, self.user_mapped_data[user_id])
            
    def saveGroupMappedData(self):
        file_path=self.decrypted_password_files_folder+'group_mapped.json'
        self.saveJsonFile(file_path, self.group_mapped_data)
    
    def saveMappedData(self):
        self.saveUserMappedData()
        self.saveGroupMappedData();
        
    def generate(self):
        self.generateMappedData()
        self.saveMappedData()
        self.generateEncryptedGroupFiles()
    
    def getUserMappedData(self):
        return self.user_mapped_data
    
    def getGroupMappedData(self):
        return self.group_mapped_data