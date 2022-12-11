# Splitted Secret
The purpose of this software is to splitt a secret over multiple people. Just if a defined amount of this people meet together they can encrypt the secret and have access to it. 

# testing
```bash 
python scripts/main.py --mode cleanup && 
echo "werewrw" > data/decrypted/main_data/test123.txt
echo "werewrw" > data/decrypted/main_data/test124.txt
mkdir data/decrypted/main_data/folder
echo "werewrw" > data/decrypted/main_data/folder/test124.txt

python scripts/main.py --amount 3 --quota 50 --mode encrypt --add-user-information --master-password "ewrwerwerew"  << END_OF_INPUTS
alpha bravo
123123812908
asfdasd@asdskjd.de
street in straat
charlie delta
1888888
sadasfdasd@asdskjd.de
street in strutt
echo2 foxtrott
99999999
asfdasd@sdskjd.de
street in strasdlasöd
END_OF_INPUTS
python scripts/main.py --mode decrypt --master-password "ewrwerwerew" 


python scripts/main.py --mode cleanup --file-types decrypted && 
python scripts/main.py --mode decrypt --user "1" --user-password "Y4GYTEW80SCQQDTIKOJ6YNCIP6MBBEM68SCKBAA1VWAQFRSPNGHEBKHSFZQENDRB" << END_OF_INPUTS
2
VGCQPW2LIKJ7SDFFLUZXBXGFPZ6L8RGPTS7TLCNN9GLR82RPHRSN34YZUXF0L27V
END_OF_INPUTS
```
# Requirements to know
- Amount of People
- How much people need to reunite for decrypting

# Requirements to implement
- Plattform independend
- easy to use

# required software
```bash 
    pip install numpy
    gpg
    ecryptfs-utils 
    ecryptfs-simple
    python
    pip
```

## todo 
- implement tails setup script
- add data-input attribut
- add data-output attribut
- write scenario test

## Further Information
- https://www.tutorialspoint.com/python/python_command_line_arguments.htm
- https://docs.python.org/3/library/argparse.html#module-argparse
- https://wiki.ubuntuusers.de/GoCryptFS/
- https://pynative.com/python-generate-random-string/
- https://www.studimup.de/abitur/stochastik/anzahl-der-m%C3%B6glichketen-berechnen-kombinatorik/
- https://numpy.org/doc/stable/reference/generated/numpy.base_repr.html?highlight=base_repr#numpy.base_repr
- https://linuxconfig.org/how-to-create-compressed-encrypted-archives-with-tar-and-gpg