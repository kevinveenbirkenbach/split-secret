# Split Secret
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

### cleanup for user

To delete all data which isn't necessary for the user:

```bash 
python scripts/main.py --mode cleanup --user "<<user>>"
```

### delete all data

To delete all data execute:

```bash 
python scripts/main.py --mode cleanup
```

### delete decrypted data
To delete all decrypted data execute:

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

### decrypt accumulated file
To decrypt the accumulated datafile execute:

```bash 
python scripts/main.py --mode decrypt --meta
```


### decrypt defined user
To decrypt the data for a defined user execute:

```bash 
python scripts/main.py --mode decrypt --user "<<user_id>>"
```

### addtional instructions
In the [INSTRUCTIONS.md](./INSTRUCTIONS.md) file the master encrypter can leave additional instructions.

## encrypt

### encrypt main data
```bash 
python scripts/main.py --secret-holders-amount "<<amount>>" --quota "<<quota>>" --mode encrypt --master-password "<<master_password>>" --input-directory "<<input_directory>>"
```

### generate encryption data
To encrypt the master-password file and to create the neccessary encrypted meta data execute: 

```bash 
python scripts/main.py --secret-holders-amount "<<amount>>" --quota "<<quota>>" --mode encrypt --add-user-information --master-password "<<master_password>>" --meta
```

### generate encryption data with user info
To encrypt the master-password file and to create the neccessary encrypted meta data with additional user infos data execute: 

```bash 
python scripts/main.py --secret-holders-amount "3" --quota "50" --mode encrypt --add-user-information --master-password "<<master_password>>" --meta --add-user-information << EOL 
Alan Turing
+ 12358
turing@turing-bomb.world
Bletchley Park
¯\_(ツ)_/¯
Ada Lovelace 
+ 132134
best@algorythm.ai
Somewhere in London 
:)
John von Neumann
+ 5488142
test@test3.de
Washington D.C.
<3 <3 <3
EOL
```
