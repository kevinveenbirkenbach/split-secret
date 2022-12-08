import argparse
import random
import string
import math
import numpy
import re

def getPassword():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(int(64*quota_factor))).upper()

def getStartnumber():
    index = 0
    start_number = ''
    while index < group_members_amount:
        start_number += '1'
        index += 1
    return int(start_number)

def getEndnumber():
    index = 0
    start_number = ''
    while index < group_members_amount:
        start_number += str(amount_of_secret_holders)
        index += 1
    return int(start_number)



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--amount',type=int, dest='amount_of_secret_holders',required=True)
    parser.add_argument('-q', '--quota', type=int, dest='decryption_quota', choices=range(1,101),required=True)
    args = parser.parse_args()
    amount_of_secret_holders = args.amount_of_secret_holders
    decryption_quota = args.decryption_quota
    quota_factor=decryption_quota/100
    group_members_amount=math.ceil(amount_of_secret_holders * quota_factor)
    amount_of_partner_secrets=(amount_of_secret_holders * group_members_amount)
    maximum_posible_combinations=amount_of_secret_holders*amount_of_secret_holders
    width= range(1,(amount_of_secret_holders+1))
    regex="([" + ','.join([str(x) for x in width]) + "]{" + str(group_members_amount) + "})"
    print(regex)
    valid_numbers = re.compile(regex)
    unvalid_sequenz = re.compile("(.)\\1+")
    index = getStartnumber()
    while index < getEndnumber():
        index_str= ''.join(sorted(str(index)))
        if re.search(valid_numbers, index_str) and not re.search(unvalid_sequenz, index_str):
            print(index_str)
        index += 1

    
  #  # Create Passwords
  #  password_groups = {}
  #  password_group_index = 0
  #  secret_holder_index = 0 
  #  while password_group_index < amount_of_secret_holders : 
  #      password_groups[password_group_index] = {};
  #      password_groups[password_group_index]['members'] = {}
  #      password_groups[password_group_index]['password'] = '' 
  #      group_members_count = 0
  #      while group_members_count < amount_of_secret_holders :
  #          if secret_holder_index == amount_of_secret_holders: 
  #              secret_holder_index = 0
  #          password_groups[password_group_index]['members'][secret_holder_index]={}
  #          password_groups[password_group_index]['members'][secret_holder_index]['password_part'] = getPassword()
  #          password_groups[password_group_index]['members'][secret_holder_index]['password_index'] = group_members_count
  #          password_groups[password_group_index]['password'] += ''.join(password_groups[password_group_index]['members'][secret_holder_index]['password_part'])
  #          secret_holder_index += 1
  #          group_members_count += 1
  #      #mathematical_formular_verification.append(sorted(password_groups[password_group_index]['members']))
  #      mathematical_formular_verification.append(sorted(password_groups[password_group_index]['members']))
  #      password_group_index += 1
  #  print(password_groups)
#
  #  # Create User Mapping
  #  user_splitted_passwords = {}
  #  for password_group_index in password_groups:
  #      for member_id in password_groups[password_group_index]['members']:
  #          if not member_id in user_splitted_passwords:
  #              user_splitted_passwords[member_id] = []
  #          user_splitted_passwords[member_id].append({"password_information" : password_groups[password_group_index]['members'][member_id], "members": list(password_groups[password_group_index]['members'].keys())});
  #  #print(user_splitted_passwords)
  #  print(sorted(mathematical_formular_verification));
