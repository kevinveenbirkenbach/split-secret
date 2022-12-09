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
    parser.add_argument('--user-password',type=str, dest='user_password',required=False)
    parser.add_argument('--user',type=int, dest='user',choices=range(1,9),required=False)
    parser.add_argument('--add-user-information',type=bool, dest='add_user_information', default=False, required=False, action=argparse.BooleanOptionalAction)
    args = parser.parse_args()
    mode = args.mode
    
    print("Splitted Secret Interface started.")
    print("Selected Mode: " + mode)
    
    if mode == 'cleanup':
        cleanup = Cleanup()
        if args.user is None: 
            print("Delete all files.")
            cleanup.deleteAll()
            exit()
        print("Delete files for user <<" + str(args.user) + ">>");
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
            if args.user_password is None:
                while True:
                    print("Please enter the user password:")
                    decrypt.setUserPassword(getpass())
                    print("Decrypting User File...")
                    try:
                        decrypt.initializeData();
                        break;
                    except:
                        print("Wrong password :(")
            else:
                decrypt.setUserPassword(args.user_password)
                print("Decrypting User File...")
                try:
                    decrypt.initializeData();
                except:
                    print("Wrong password :(")
                    exit()
            print("File decrypted :) \n")
            print("Please contact the following persons and tell them that you need help to encrypt the data: \n")
            for contact_id in decrypt.user_data['contacts']:
                print("user_id: " + contact_id)
                for label in decrypt.user_data['contacts'][contact_id]:
                    print(label + ": " + decrypt.user_data['contacts'][contact_id][label])
            print("You need at least <<" + str(decrypt.needed_encrypters_amount) +">> other person to decrypt the secret.")
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
        if args.add_user_information is not None:
            for user_id in encrypt.user_mapped_data:
                for label in ['name','phone','email','address']:
                    print("Please enter attribut <<" + label + ">> for user <<" + user_id+ ">>:" )
                    encrypt.addInformationToUser(user_id, label, str(input()))
        encrypt.compileData()
        encrypt.encrypt()
        exit()