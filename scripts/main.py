import argparse
from classes.Encryption import Encryption
from classes.Cleanup import Cleanup
from classes.Decryption import Decryption
from getpass import getpass
from classes.AbstractSplittedSecret import AbstractSplittedSecret
import traceback

cleanup = Cleanup()

def clean_exit():
    print("Cleaning up.")
    cleanup.cleanupFiles(AbstractSplittedSecret.TYPE_DECRYPTED)
    print("Leaving program. Goodby :)")
    exit();
    pass
try:
    if __name__ == '__main__':
        parser = argparse.ArgumentParser()
        parser.add_argument('--mode',type=str, dest='mode',required=True,choices=['cleanup','encrypt','decrypt'])
        parser.add_argument('--amount',type=int, dest='amount_of_secret_holders',required=False,choices=AbstractSplittedSecret.getCoSecretHoldersRange())
        parser.add_argument('--quota', type=int, dest='decryption_quota', choices=range(1,101),required=False)
        parser.add_argument('--master-password',type=str, dest='master_password',required=False)
        parser.add_argument('--user-password',type=str, dest='user_password',required=False)
        parser.add_argument('--user',type=int, dest='user',choices=AbstractSplittedSecret.getSecretHoldersRange(),required=False)
        parser.add_argument('--add-user-information',type=bool, dest='add_user_information', default=False, required=False, action=argparse.BooleanOptionalAction)
        args = parser.parse_args()

        print("Splitted Secret Interface started.")
        print("Selected Mode: " + args.mode)
        
        if args.mode == 'cleanup':   
            if args.user is None: 
                print("Delete all files.")
                cleanup.deleteAll()
                clean_exit()
            print("Delete files for user <<" + str(args.user) + ">>");
            cleanup.cleanupForUser(args.user)
            clean_exit()
            
        if args.mode == 'decrypt':
            decrypt = Decryption()
            if args.master_password is None:
                if args.user is None: 
                    print("Please type in the user number:")
                    decrypt.initializeUser(input())
                else:
                    decrypt.initializeUser(args.user)
                if args.user_password is None:
                    while True:
                        print("Please enter the user password:")
                        decrypt.setUserPassword(getpass())
                        print("Decrypting User File...")
                        try:
                            decrypt.initializeUserDataDecryption();
                            break;
                        except Exception as error:
                            print("An error occured. Propably you typed in a wrong password :( The error is: " + str(error))
                else:
                    decrypt.setUserPassword(args.user_password)
                    print("Decrypting User File...")
                    try:
                        decrypt.initializeUserDataDecryption();
                    except Exception as error:
                        print("An error occured. Propably you passed a wrong password :( The error is: " + str(error))
                        clean_exit()
                print("File decrypted :) \n")
                print("Please contact the following persons and tell them that you need help to encrypt the data: \n")
                for contact_id in decrypt.user_data['contacts']:
                    print("user_id: " + contact_id)
                    for label in decrypt.user_data['contacts'][contact_id]:
                        print(label + ": " + decrypt.user_data['contacts'][contact_id][label])
                    print("--------------------------------\n")
                while True:
                    decrypt.resetDecrypterIds()
                    try:
                        person_counter = 1
                        while person_counter <= decrypt.getNeededCoDecryptersAmount():
                            print("The following user id's are in the decryption list: " + str(decrypt.getDecrypterIds()))
                            print("You need at least <<" + str(decrypt.getNeededCoDecryptersAmount()) +">> other person to decrypt the secret.")
                            print("Type in the user id of another encrypter:")
                            decrypt.addDecrypterId(int(input()))
                            person_counter += 1
                        break
                    except Exception as error:
                        print("The following error occured <<" + str(error) + ">> :( \n Please try again :)")
                print("\nFOR PASSWORD GROUP: " + decrypt.getDecryptersGroupName()) 
                print("FOR USER ID: "  + decrypt.getUserId())
                print("PASSWORD SHARE IS: " + decrypt.getPasswordShare() + "\n")
                while True:
                    decrypt.resetPasswordShare()
                    co_decrypter_ids = decrypt.getCoDecrypterIds()
                    print("Please execute this script at the users " + str(co_decrypter_ids) + ".")
                    for co_decrypter_id in decrypt.getCoDecrypterIds():
                        print("\nFOR PASSWORD GROUP: " + decrypt.getDecryptersGroupName()) 
                        print("FOR USER: " + str(co_decrypter_id)) 
                        print("PASSWORD SHARE IS: ")
                        decrypt.addPasswordShare(co_decrypter_id, input())
                    print("\nTHE SHARED PASSWORD IS: " + decrypt.getSharedPassword())
                    break;
                        
                clean_exit()  
            print("Decrypting accumulated file...")
            decrypt.setUserPassword(args.master_password)
            decrypt.decryptAccumulatedFile()
            clean_exit()
        
        if args.mode == 'encrypt':
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
            clean_exit()
except Exception:
    print(traceback.format_exc())
clean_exit()