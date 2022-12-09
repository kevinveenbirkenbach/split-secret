import random
import string
import math
import numpy
import re
import json
from .AbstractSplittedSecret import AbstractSplittedSecret

class Encryption(AbstractSplittedSecret):
    
    def __init__(self, amount_of_secret_holders, decryption_quota,master_password):
        super(Encryption, self).__init__()
        self.amount_of_secret_holders = amount_of_secret_holders
        self.decryption_quota = decryption_quota
        self.master_password = master_password
        self.quota_factor=self.decryption_quota/100
        self.group_members_amount=math.ceil(self.amount_of_secret_holders * self.quota_factor)
        self.initializeUserData()
        self.initializeGroupData()
        
    def initializeUserData(self):
        self.user_mapped_data = {}
        user_count = 1
        while user_count <= self.amount_of_secret_holders:
            self.user_mapped_data[str(user_count)] = {"groups":{},"user_password":self.createPassword(64),"about":{}}
            user_count += 1;
    
    def initializeGroupData(self):
        self.group_mapped_data = {} 

    def addInformationToUser(self,user_id,label,content):
        self.user_mapped_data[user_id]['about'][label] = content;
        
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
    
    def createPassword(self,length):
        characters = string.ascii_letters + string.digits
        return (''.join(random.choice(characters) for i in range(length)).upper())
    
    def isGroupValid(self,password_group_index_str):
        secret_stakeholders_range=range(1,(self.amount_of_secret_holders+1))
        valid_numbers = re.compile("([" + ','.join([str(x) for x in secret_stakeholders_range]) + "]{" + str(self.group_members_amount) + "})")
        unvalid_sequenz = re.compile("(.)\\1+")
        return re.search(valid_numbers, password_group_index_str) and not re.search(unvalid_sequenz, password_group_index_str)
    
    def compileContacts(self):
        contacts = {}
        for user_id in self.user_mapped_data:
            contacts[user_id] = self.user_mapped_data[user_id]['about']
        for user_id in self.user_mapped_data:
            self.user_mapped_data[user_id]['contacts'] = {}
            for contact_id in contacts:
                if contact_id != user_id:
                    self.user_mapped_data[user_id]['contacts'][contact_id] = contacts[contact_id]
        
    def compileData(self):
        self.compileContacts()
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
                        particial_password_length= int(128*self.quota_factor); 
                        password_part = self.createPassword(particial_password_length)
                        self.group_mapped_data[password_group_index_int]['members'][secret_holder_index] = password_part
                        password += password_part
                        self.user_mapped_data[secret_holder_index]['groups'][password_group_index_str] = password_part
                    self.group_mapped_data[password_group_index_int]['password'] += password
            index += 1
            
    def encryptStringToFile(self,text,output_file,password):
        self.executeCommand('echo \'' + text + '\' | gpg --symmetric --armor --batch --passphrase "' + password + '" -o "' + output_file + '"')
    
    def encryptGroupFiles(self):
        for password_group_index_int in self.group_mapped_data:
            encrypted_group_password_file_path = self.getGroupFilePath(password_group_index_int,"encrypted")
            self.encryptStringToFile(self.master_password,encrypted_group_password_file_path,self.group_mapped_data[password_group_index_int]['password'])
    
    def encryptToJsonFile(self,data,file_path,password):
        self.encryptStringToFile(json.dumps(data,ensure_ascii=False), file_path, password)
        
    def encryptUserData(self):
        for user_id in self.user_mapped_data:
            file_path=self.getUserFilePath(user_id,"encrypted")
            data=self.user_mapped_data[user_id]
            password=self.user_mapped_data[user_id]['user_password']
            self.encryptToJsonFile(data,file_path,password)
            
    def encryptAccumulatedData(self):
        file_path=self.getAccumulatedFilePath("encrypted")
        data={"user_mapped": self.user_mapped_data, "group_mapped": self.group_mapped_data}
        self.encryptToJsonFile(data,file_path,self.master_password)
    
    def encrypt(self):
        self.encryptUserData()
        self.encryptAccumulatedData()
        self.encryptGroupFiles()