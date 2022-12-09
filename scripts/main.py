import argparse
from classes.Generate import Generate

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--amount',type=int, dest='amount_of_secret_holders',required=True,choices=range(1,9))
    parser.add_argument('-q', '--quota', type=int, dest='decryption_quota', choices=range(1,101),required=True)
    #parser.add_argument('-p', '--master-password', type=str, dest='master_password', required=False)
    args = parser.parse_args()
    #master_password = args.master_password
    generate = Generate(args.amount_of_secret_holders, args.decryption_quota)
    generate.execute()
    #savePassword(master_password,decrypted_master_password_file_path)
    
    
    #print(password_groups)


