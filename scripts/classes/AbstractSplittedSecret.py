from .Cli import Cli

class AbstractSplittedSecret(Cli):
    def __init__(self):
        super(Cli, self).__init__()
        self.encrypted_splitted_password_files_folder = "data/encrypted/splitted_password_files/"
        self.decrypted_password_files_folder="data/decrypted/password_files/"