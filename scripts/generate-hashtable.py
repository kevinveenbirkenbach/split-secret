import argparse
import random
import string


def getPassword():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(int(64*quota_factor))).upper()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--amount',type=int, dest='amount_of_secret_holders',required=True)
    parser.add_argument('-q', '--quota', type=int, dest='decryption_quota', choices=range(1,101),required=True)
    args = parser.parse_args()
    amount_of_secret_holders = args.amount_of_secret_holders
    decryption_quota = args.decryption_quota
    quota_factor=decryption_quota/100
    password_group_members_amount=amount_of_secret_holders * quota_factor
    amount_of_partner_secrets=(amount_of_secret_holders * password_group_members_amount)
    #required_passwords=amount_of_partner_secrets * ( amount_of_secret_holders -1) ;
    required_passwords=amount_of_partner_secrets * amount_of_secret_holders
    print(quota_factor);
    print(amount_of_secret_holders);
    print(decryption_quota);
    print(required_passwords);

    mathematical_formular_verification=[]

    # Create Passwords
    password_groups = {}
    password_group_index = 0
    secret_holder_index = 0 
    while password_group_index < required_passwords : 
        password_groups[password_group_index] = {};
        password_groups[password_group_index]['members'] = {}
        password_groups[password_group_index]['password'] = '' 
        group_members_count = 0
        while group_members_count < password_group_members_amount :
            if secret_holder_index == amount_of_secret_holders: 
                secret_holder_index = 0
            password_groups[password_group_index]['members'][secret_holder_index]={}
            password_groups[password_group_index]['members'][secret_holder_index]['password_part'] = getPassword()
            password_groups[password_group_index]['members'][secret_holder_index]['password_index'] = group_members_count
            password_groups[password_group_index]['password'] += ''.join(password_groups[password_group_index]['members'][secret_holder_index]['password_part'])
            secret_holder_index += 1
            group_members_count += 1
        mathematical_formular_verification.append(sorted(password_groups[password_group_index]['members']))
        password_group_index += 1
    print(password_groups)

    # Create User Mapping
    user_splitted_passwords = {}
    for password_group_index in password_groups:
        for member_id in password_groups[password_group_index]['members']:
            if not member_id in user_splitted_passwords:
                user_splitted_passwords[member_id] = []
            user_splitted_passwords[member_id].append({"password_information" : password_groups[password_group_index]['members'][member_id], "members": list(password_groups[password_group_index]['members'].keys())});
    #print(user_splitted_passwords)
    print(sorted(mathematical_formular_verification));
