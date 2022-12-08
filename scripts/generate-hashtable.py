import argparse
import random
import string

def getPassword():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(int(128*quota_factor))).upper();

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--amount',type=int, dest='amount_of_secret_holders',required=True)
    parser.add_argument('-q', '--quota', type=int, dest='decryption_quota', choices=range(1,101),required=True)
    args = parser.parse_args()
    amount_of_secret_holders = args.amount_of_secret_holders;
    decryption_quota = args.decryption_quota;
    quota_factor=decryption_quota/100;
    password_divisor=int(amount_of_secret_holders*quota_factor)
    amount_of_partner_secrets=(amount_of_secret_holders * password_divisor)
    required_passwords=amount_of_partner_secrets * ( amount_of_secret_holders -1) ;
    print(quota_factor);
    print(amount_of_secret_holders);
    print(decryption_quota);
    print(required_passwords);

    # generate splitted password matrix       
    secret_holders = {}
    secret_holder_index = 0;

    while secret_holder_index < amount_of_secret_holders:
        secret_holders[secret_holder_index] = {};
        partner_secret_holder_index  = 0;
        while partner_secret_holder_index < amount_of_secret_holders:
            if partner_secret_holder_index != secret_holder_index :
                secret_holders[secret_holder_index][partner_secret_holder_index] = {};
                secret_holders[secret_holder_index][partner_secret_holder_index][secret_holder_index] = {};
                index=0
                while index < password_divisor:
                    secret_holders[secret_holder_index][partner_secret_holder_index][secret_holder_index][index] = getPassword();
                    index += 1;
            partner_secret_holder_index += 1;
        secret_holder_index += 1;
    print(secret_holders);

    # generate passwords
    passwords = []
    while secret_holder_index < amount_of_secret_holders:
        
        secret_holder_index += 1;