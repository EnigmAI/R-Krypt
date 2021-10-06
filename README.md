# R-Krypt
A comprehensive cipher tool for text, audio and images.

## Installation and Setup
* Fork the repo and clone it.
```
git clone https://github.com/EnigmAI/R-Krypt.git
```
* You can view the list of commands by running the following command
```
python cli.py --help
```
* Some sample commands
```
python cli.py --cipher caesar --encrypt --key 10
python cli.py --cipher rot13 --decrypt
python cli.py --cipher caesar --input_file sample.txt --output_file out.txt --encrypt --key 10
```

## How To Contribute?
- Add to the list of ciphers inside ciphers/ directory by coding the cipher in Python language and the script should have separate functions for "encrypt", "decrypt" and "main" as shown in ciphers/baconian.py file.
- You can also add the cipher functionality in the CLI by editing the cli.py file. Checkout how Caesar cipher is added inside cli.py to see how to add a cipher.
