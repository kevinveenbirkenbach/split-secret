import argparse
import random
import string
import math
import numpy
import re
import subprocess

def bash(command):
    print(command)
    process = subprocess.Popen([command], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    out, err = process.communicate()
    stdout = out.splitlines()
    output = []
    for line in stdout:
        output.append(line.decode("utf-8"))
    if process.wait() > bool(0):
        print(command, out, err)
        raise Exception("Exitcode is greater then 0")
    return output

def list_to_string(list):
    return str(' '.join(list))

def print_bash(command):
    output = bash(command)
    print(list_to_string(output))
    return output

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

def savePassword(password,password_file_path):
    print("Saving password to: " + password_file_path)
    master_password_file = open(password_file_path, "a")
    master_password_file.seek(0)
    master_password_file.truncate()
    master_password_file.write(password)
    master_password_file.close()

if __name__ == '__main__':
    master_password_file_path="data/master-password.txt"

    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--amount',type=int, dest='amount_of_secret_holders',required=True,choices=range(1,9))
    parser.add_argument('-q', '--quota', type=int, dest='decryption_quota', choices=range(1,101),required=True)
    parser.add_argument('-p', '--master-password', type=str, dest='master_password', required=False)
    args = parser.parse_args()
    amount_of_secret_holders = args.amount_of_secret_holders
    master_password = args.master_password
    decryption_quota = args.decryption_quota
    
    savePassword(master_password,master_password_file_path)
    
    quota_factor=decryption_quota/100
    group_members_amount=math.ceil(amount_of_secret_holders * quota_factor)
    amount_of_partner_secrets=(amount_of_secret_holders * group_members_amount)
    maximum_posible_combinations=amount_of_secret_holders*amount_of_secret_holders
    width= range(1,(amount_of_secret_holders+1))
    regex="([" + ','.join([str(x) for x in width]) + "]{" + str(group_members_amount) + "})"
    valid_numbers = re.compile(regex)
    unvalid_sequenz = re.compile("(.)\\1+")
    index = getStartnumber()
    password_groups = {}
    while index < getEndnumber():
        password_group_index_str = ''.join(sorted(str(index)))
        if re.search(valid_numbers, password_group_index_str) and not re.search(unvalid_sequenz, password_group_index_str):
            password_group_index_int = int(password_group_index_str)
            if not password_group_index_int in password_groups:
                password_index = 1
                password_groups[password_group_index_int] = {}
                password_groups[password_group_index_int]['members'] = {}
                password_groups[password_group_index_int]['password'] = '' 
                password = ''
                for secret_holder_index in password_group_index_str:
                    password_groups[password_group_index_int]['members'][secret_holder_index]={}
                    password_part = getPassword()
                    password_groups[password_group_index_int]['members'][secret_holder_index]['password_part'] = password_part
                    password_groups[password_group_index_int]['members'][secret_holder_index]['password_index'] = password_index
                    password += password_part
                    password_index += 1
                password_groups[password_group_index_int]['password'] += password
                splitted_password_file = "data/" + password_group_index_str + ".splitted_password_file.txt"
                print_bash('cp -v "' + master_password_file_path + '" "' + splitted_password_file + '" && gpg --batch --passphrase "' + password + '" -c "' + splitted_password_file +'"')
        index += 1
    print(password_groups)


