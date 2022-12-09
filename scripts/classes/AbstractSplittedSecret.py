from .Cli import Cli

class AbstractSplittedSecret(Cli):
    def __init__(self):
        super(Cli, self).__init__()
        self.encrypted_folder="data/encrypted/"
        self.decrypted_folder="data/encrypted/"
        self.encrypted_group_files_folder = self.encrypted_folder + "group_files/"
        self.decrypted_group_files_folder = self.decrypted_folder + "group_files/"
        self.encrypted_user_files_folder = self.encrypted_folder + "user_files/"
        self.decrypted_user_files_folder = self.encrypted_folder + "user_files/"