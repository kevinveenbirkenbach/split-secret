import argparse
from classes.Encryption import Encryption
from classes.Cleanup import Cleanup
from classes.Decryption import Decryption
from getpass import getpass

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode',type=str, dest='mode',required=True,choices=['cleanup','encrypt','decrypt'])
    parser.add_argument('--amount',type=int, dest='amount_of_secret_holders',required=False,choices=range(1,9))
    parser.add_argument('--quota', type=int, dest='decryption_quota', choices=range(1,101),required=False)
    parser.add_argument('--master-password',type=str, dest='master_password',required=False)
    parser.add_argument('--user',type=int, dest='user',choices=range(1,9),required=False)
    args = parser.parse_args()
    mode = args.mode
    
    print("Splitted Secret Interface started.")
    print("Selected Mode: " + mode)
    
    if mode == 'cleanup':
        cleanup = Cleanup()
        if args.user is None: 
            cleanup.deleteAll()
            exit()
        cleanup.cleanupForUser(args.user)
        exit()
        
    if mode == 'decrypt':
        decrypt = Decryption()
        if args.master_password is None:
            if args.user is None: 
                print("Please type in the user number:")
                decrypt.setUserId(input())
            else:
                decrypt.setUserId(args.user)
            while True:
                print("Please enter the user password:")
                decrypt.setUserPassword(getpass())
                print("Decrypting User File...")
                try:
                    decrypt.decryptUserFile();
                    break;
                except:
                    print("Wrong password :(")
            print("File encrypted :) ")
            exit()
        print("Decrypting accumulated file...")
        decrypt.setUserPassword(args.master_password)
        decrypt.decryptAccumulatedFile()
        exit()
    
    if mode == 'encrypt':
        if args.master_password is None:
            print("Please enter the master password:")
            master_password = getpass()
        else:
            master_password = args.master_password
        encrypt = Encryption(args.amount_of_secret_holders, args.decryption_quota, master_password)
        encrypt.generateData()
        encrypt.encrypt()
        exit()