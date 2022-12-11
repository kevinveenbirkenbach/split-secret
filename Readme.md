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
To decrypt the data type in:

```bash 
python scripts/main.py --mode decrypt
```

### decrypt defined user
To decrypt the data for a defined user type in:

```bash 
python scripts/main.py --mode decrypt --user "<<user_id>>"
```

## encrypt

### encrypt all data

```bash 
python scripts/main.py --amount 3 --quota 50 --mode encrypt --add-user-information --master-password "{{master_password}}"
```

### encrypt master-password file

## todo 
- add data-input attribut
- add data-output attribut