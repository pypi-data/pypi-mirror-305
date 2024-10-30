# StealthText

StealthText is a simple and secure library for encrypting and decrypting text messages using AES encryption. This package also provides a command-line interface for easy use.

## Features

- **Encryption**: Securely encrypt text messages.
- **Decryption**: Decrypt previously encrypted messages.
- **Command-Line Interface**: Easily encrypt or decrypt messages directly from the terminal.

## Installation

You can install `StealthText` using pip:

```bash
pip install StealthText
```

## Usage

### Importing the Library

You can use `StealthText` in your Python code by importing the `encrypt` and `decrypt` functions:

```python
from stealthtext import encrypt, decrypt
```

### Encrypting a Message

To encrypt a message, use the `encrypt` function:

```python
password = 'your_password'  # Use a strong password
message = 'Hello, world!'    # Message to encrypt

encrypted_message = encrypt(message, password)
print(f'Encrypted Message: {encrypted_message}')
```

### Decrypting a Message

To decrypt an encrypted message, use the `decrypt` function:

```python
encrypted_message = 'your_encrypted_message_here'  # Replace with your encrypted message

try:
    decrypted_message = decrypt(encrypted_message, password)
    print(f'Decrypted Message: {decrypted_message}')
except Exception as e:
    print("Decryption failed:", e)
```

## Command-Line Interface

### Encrypt a Message

You can also use the command-line interface to encrypt messages:

```bash
stealthtext encrypt your_password "Hello, world!"
```

### Decrypt a Message

To decrypt a message from the command line, use:

```bash
stealthtext decrypt your_password "your_encrypted_message_here"
```

### Command-Line Arguments

- **action**: The action to perform, either `encrypt` or `decrypt`.
- **password**: The password used for encryption or decryption.
- **message**: The message to encrypt or the encrypted message to decrypt.

### Example

Here’s a full example of using the CLI:

1. Encrypt a message :

```bash
stealthtext encrypt my_secret_password "This is a secret message."
```

Output :

Encrypted Message: [Base64 encoded string] 


2. Decrypt the message:

```bash
stealthtext decrypt my_secret_password "[Base64 encoded string]"
```

Output :

Decrypted Message: This is a secret message.


## Security Recommendations

- Always use a strong password for encryption.
- Keep your passwords and encrypted messages secure.
- Consider using a password manager to store your passwords.

## Contribution

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

