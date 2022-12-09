import argparse
from classes.Generate import Generate
from classes.Cleanup import Cleanup
from getpass import getpass

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode',type=str, dest='mode',required=True,choices=['cleanup','generate'])
    parser.add_argument('--amount',type=int, dest='amount_of_secret_holders',required=False,choices=range(1,9))
    parser.add_argument('--quota', type=int, dest='decryption_quota', choices=range(1,101),required=False)
    parser.add_argument('--master-password',type=str, dest='master_password',required=False)
    parser.add_argument('--user',type=int, dest='user',choices=range(1,9),required=False)
    args = parser.parse_args()
    
    if args.mode == 'cleanup':
        cleanup = Cleanup()
        if args.user is None: 
            cleanup.deleteAll()
            exit()
        cleanup.cleanupForUser(args.user)
        
    if args.mode == 'generate':
        if args.master_password is None:
            print("Please enter the master password:")
            master_password = getpass()
        else:
            master_password = args.master_password
        generate = Generate(args.amount_of_secret_holders, args.decryption_quota,master_password)
        generate.generate()
        exit()