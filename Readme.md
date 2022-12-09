# Splitted Secret
The purpose of this software is to splitt a secret over multiple people. Just if a defined amount of this people meet together they can encrypt the secret and have access to it. 

# testing
```bash 
python scripts/main.py --mode cleanup && 
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
python scripts/main.py --mode decrypt --master-password "ewrwerwerew"  &&
python scripts/main.py --mode decrypt --user "1" 


python scripts/main.py --mode cleanup --user "1"  && python scripts/main.py --mode decrypt --user "1" --user-password "O3ITMWXZED9FKYQ0PB2WNVRWSCSCYVXCD00PJ6GQ4MFPIUWBVDCYSSSX9ZDBW5QU"

```
# Requirements to know
- Amount of People
- How much people need to reunite for decrypting

# Requirements to implement
- Plattform independend
- easy to use

# setup
```bash 
    pip install numpy
    gpg
    python
    pip
```

## Further Information
- https://www.tutorialspoint.com/python/python_command_line_arguments.htm
- https://docs.python.org/3/library/argparse.html#module-argparse
- https://wiki.ubuntuusers.de/GoCryptFS/
- https://pynative.com/python-generate-random-string/
- https://www.studimup.de/abitur/stochastik/anzahl-der-m%C3%B6glichketen-berechnen-kombinatorik/
- https://numpy.org/doc/stable/reference/generated/numpy.base_repr.html?highlight=base_repr#numpy.base_repr