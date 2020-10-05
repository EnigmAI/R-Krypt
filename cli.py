import click

import ciphers.caesar as caesar_cipher
import ciphers.rot13 as rot13_cipher


@click.command()
@click.option(
    '--cipher',
    '-cipher',
    help='Select which cipher to use.',
    required=True,
)
@click.option(
    '--input_file',
    type=click.File('r'),
    help='File in which there is the text you want to encrypt/decrypt. If not provided, a prompt will allow you to type the input text.',
)
@click.option(
    '--output_file',
    type=click.File('w'),
    help='File in which the encrypted / decrypted text will be written. If not provided, the output text will just be printed.',
)
@click.option(
    '--encrypt/--decrypt',
    '-e/-d',
    help='Whether you want to encrypt the input text or decrypt it.'
)
@click.option(
    '--key',
    '-k',
    default=1,
    help='The numeric key to use for the caesar encryption / decryption.'
)
def main(cipher, input_file, output_file, encrypt, key):
    if cipher == 'caesar':
        caesar(input_file, output_file, encrypt, key)
    if cipher == 'rot13':
        rot13(input_file, output_file, encrypt)


def caesar(input_file, output_file, encrypt, key):
    if input_file:
        text = input_file.read()
    else:
        text = click.prompt('Enter text', hide_input=encrypt)

    if encrypt:
        cyphertext = caesar_cipher.encrypt(text, key)
    else:
        cyphertext = caesar_cipher.decrypt(text, key)

    if output_file:
        output_file.write(cyphertext)
    else:
        click.echo(cyphertext)


def rot13(input_file, output_file, encrypt):
    if input_file:
        text = input_file.read()
    else:
        text = click.prompt('Enter text', hide_input=encrypt)

    if encrypt:
        cyphertext = rot13_cipher.encrypt(text)
    else:
        cyphertext = rot13_cipher.decrypt(text)

    if output_file:
        output_file.write(cyphertext)
    else:
        click.echo(cyphertext)


if __name__ == '__main__':
    main()
