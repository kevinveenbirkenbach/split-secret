# Splitted Secret
The purpose of this software is to splitt a secret over multiple people. Just if a defined amount of this people meet together they can encrypt the secret and have access to it. 

## requirements 

### system
This software is developed for and on an [Arch Linux](https://archlinux.org/) system.

### setup

Before executing the script it may be necessary to install the following software packages:

```bash
pacman -S gpg tar python pip python-pip
pip install numpy
```
## commands

## cleanup data

### delete all data

To delete all data execute:

```bash 
python scripts/main.py --mode cleanup
```

### delete decrypted data
To delete all encrypted data execute:

```bash 
python scripts/main.py --mode cleanup --file-types decrypted
```

### delete all encrypted data
To delete all encrypted data execute:

```bash 
python scripts/main.py --mode cleanup --file-types encrypted
```

## decrypt

### decrypt automatic
To decrypt the data execute:

```bash 
python scripts/main.py --mode decrypt
```

### decrypt defined user
To decrypt the data for a defined user execute:

```bash 
python scripts/main.py --mode decrypt --user "<<user_id>>"
```

## encrypt

### encrypt main data

```bash 
python scripts/main.py --secret-holders-amount "<<amount>>" --quota "<<quota>>" --mode encrypt --master-password "<<master_password>>" --input-directory "<<input_directory>>"
```

### encrypt master password

To encrypt the master-password file and to create the neccessary encrypted meta data execute: 

```bash 
python scripts/main.py --secret-holders-amount "<<amount>>" --quota "<<quota>>" --mode encrypt --add-user-information --master-password "<<master_password>>" --create-meta-data
```