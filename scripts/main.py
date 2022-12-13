import argparse
from classes.Encryption import Encryption
from classes.Cleanup import Cleanup
from classes.Decryption import Decryption, AutomaticIdentificationImpossibleException
from getpass import getpass
import traceback
from classes.Cli import Cli
from classes.Paths import Paths

cli = Cli()
paths = Paths()
cleanup = Cleanup(cli,paths)

def clean_exit():
    print("Cleaning up.")
    try:
        cleanup.cleanupFiles(Paths.TYPE_DECRYPTED)
    except:
        pass
    standard_exit()

def dirty_exit():
    print("ATTENTION: SECURITY RISK !!!\nPROGRAM DIDN'T CLEAN UP DECRYPTED DATA. \nDECRYPTED DATA EXISTS AND CAN BE READ BY EVERYBODY!")
    print("TO REMOVE DECRYPTED DATA EXECUTE:\nmain.py --mode cleanup --file-types " + Paths.TYPE_DECRYPTED)
    standard_exit()

def standard_exit():
    print("Leaving program.")
    exit()
    
try:
    if __name__ == '__main__':
        parser = argparse.ArgumentParser()
        parser.add_argument('--mode',type=str, dest='mode',required=True,choices=['cleanup','encrypt','decrypt'])
        parser.add_argument('--file-types',type=str, dest='file_types',required=False,choices=[Paths.TYPE_DECRYPTED, Paths.TYPE_ENCRYPTED])
        parser.add_argument('--secret-holders-amount',type=int, dest='amount_of_secret_holders',required=False,choices=Encryption.getCoSecretHoldersRange(),help="Needed for creating of encryption meta data.")
        parser.add_argument('--quota', type=int, dest='decryption_quota', choices=range(1,101),required=False)
        parser.add_argument('--master-password',type=str, dest='master_password',required=False)
        parser.add_argument('--user-password',type=str, dest='user_password',required=False)
        parser.add_argument('--user',type=int, dest='user',choices=Encryption.getSecretHoldersRange(),required=False)
        parser.add_argument('--add-user-information',type=bool, dest='add_user_information', default=False, required=False, action=argparse.BooleanOptionalAction, help="Add additional information to users.")
        parser.add_argument('--input-directory',type=str,dest='input_directory',required=False, help="The directory from which the data should be encrypted.")
        parser.add_argument('--meta-data',type=bool, dest='meta_data', default=False, required=False, action=argparse.BooleanOptionalAction, help="When mode is encrypt and this flag is set, the encrypted meta data is created. When mode is decrypt and this flag is set the accumulated file will be decrypted.")
        args = parser.parse_args()

        print("Application started.")
        print("To leave the appplication use the key kombination: <<Ctr>> + <<Alt>> + <<C>>")
        print("Cleaning up all decrypted files.")
        cleanup.cleanupFiles(Paths.TYPE_DECRYPTED)
        print("Selected Mode: " + args.mode)
        
        if args.mode == 'cleanup':   
            print("Cleaning up.")
            if args.file_types is None:
                if args.user is None: 
                    print("Deleting all encrypted and decrypted files.")
                    cleanup.deleteAll()
                    standard_exit()
                print("Deleting all files which aren't related to user: " + str(args.user));
                cleanup.cleanupForUser(args.user)
                standard_exit()
            print("Deleting all " + args.file_types + " files.")
            cleanup.cleanupFiles(args.file_types)
            standard_exit()
            
        if args.mode == 'decrypt':
            decrypt = Decryption(cli,paths)
            if args.meta_data is True:
                if args.master_password is None:
                    print("Enter the master password:")
                    master_password = getpass()
                else:
                    master_password = args.master_password
                decrypt = Decryption(cli,paths)
                print("Decrypting accumulated data.")
                decrypt.setUserPassword(master_password)
                decrypt.decryptAccumulatedFile()
                dirty_exit()
            if args.user is None:
                try:
                    print("Attempt to identify user.") 
                    user_id = decrypt.identifyUser()
                    print("The user id is: " + user_id)
                except:
                    print("A automatic user id identification wasn't possible.")
                    print("Type in the user id:")
                    user_id = input()
                decrypt.initializeUser(user_id)
            else:
                decrypt.initializeUser(args.user)
            if args.user_password is None:
                while True:
                    print("Enter the user password:")
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
            print("\nContact the following persons and request their password share: \n")
            for contact_id in decrypt.user_data['contacts']:
                print("user_id: " + contact_id)
                for label in decrypt.user_data['contacts'][contact_id]:
                    print(label + ": " + decrypt.user_data['contacts'][contact_id][label])
            while True:
                print("\nReset password shares.\n")
                decrypt.resetDecrypterIds()
                try:
                    password_shares_count = 1
                    while password_shares_count < decrypt.getNeededDecryptersAmount():
                        print(str(password_shares_count) + " password shares had been added.")
                        print("Password shares for the the users " + str(decrypt.getDecrypterIds()) + " been added. ")
                        print("You need to add " + str((decrypt.getNeededDecryptersAmount()-password_shares_count)) +" more password shares.")
                        print("\nType in the user id of another decrypter:")
                        decrypt.addDecrypterId(int(input()))
                        password_shares_count += 1
                    break
                except Exception as error:
                    print("The following error occured <<" + str(error) + ">> :( \n Try again :)")
            print("\nYour data is:\n")
            print("FOR PASSWORD GROUP: " + decrypt.getDecryptersGroupName()) 
            print("FOR USER ID: "  + decrypt.getUserId())
            print("PASSWORD SHARE IS: " + decrypt.getPasswordShare() + "\n")
            while True:
                try:
                    decrypt.resetPasswordShare()
                    co_decrypter_ids = decrypt.getCoDecrypterIds()
                    for co_decrypter_id in decrypt.getCoDecrypterIds():
                        print("Type in the password share for: \n")
                        print("FOR PASSWORD GROUP: " + decrypt.getDecryptersGroupName()) 
                        print("FOR USER: " + str(co_decrypter_id)) 
                        print("PASSWORD SHARE IS: ")
                        decrypt.addPasswordShare(co_decrypter_id, input())
                    print("\nTHE GROUP PASSWORD IS: " + decrypt.getGroupPassword())
                    print("\nDecrypting group password file.\n")
                    decrypt.initializeGroupDataEncryption()
                    print("THE MASTER PASSWORD IS: " + decrypt.getMasterPassword())
                    break;
                except:
                    print("An unexpected error occured: \n" + traceback.format_exc())
            print("Decrypting main data.")
            decrypt.decryptMainData()
            print("The data was decrypted to: " + paths.getDecryptedMainDataStandartFolder())
            dirty_exit()
        
        if args.mode == 'encrypt':
            if args.master_password is None:
                print("Enter the master password:")
                master_password = getpass()
            else:
                master_password = args.master_password
            encrypt = Encryption(cli,paths,args.amount_of_secret_holders, args.decryption_quota, master_password)
            if args.add_user_information is True:
                for user_id in encrypt.user_mapped_data:
                    for label in ['name','phone','email','address','notes']:
                        print("Enter attribut <<" + label + ">> for user <<" + user_id+ ">>:" )
                        encrypt.addInformationToUser(user_id, label, str(input()))
            encrypt.compileData()
            if args.meta_data is True:
                print('Cleaning up encrypted meta data.')
                cleanup.cleanupMetaData(Paths.TYPE_ENCRYPTED)
                print("Create and encrypt meta data.")
                encrypt.encryptMetaData()
            if args.input_directory is not None:
                print("Encrypt main data.")
                encrypt.encryptMainData(args.input_directory)
            dirty_exit()
except KeyboardInterrupt:
    print("Program interrupted by user.")
clean_exit()