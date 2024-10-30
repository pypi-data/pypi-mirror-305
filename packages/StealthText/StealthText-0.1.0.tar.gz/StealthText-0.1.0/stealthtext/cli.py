import argparse
from .encryption import encrypt, decrypt

def main():
    parser = argparse.ArgumentParser(description='Encrypt or decrypt text messages.')
    parser.add_argument('action', choices=['encrypt', 'decrypt'], help='Action to perform: encrypt or decrypt')
    parser.add_argument('password', help='Password for encryption/decryption')
    parser.add_argument('message', help='Message to encrypt or decrypt')

    args = parser.parse_args()

    if args.action == 'encrypt':
        encrypted_message = encrypt(args.message, args.password)
        print(f'Encrypted Message: {encrypted_message}')

    elif args.action == 'decrypt':
        try:
            decrypted_message = decrypt(args.message, args.password)
            print(f'Decrypted Message: {decrypted_message}')
        except Exception as e:
            print("Decryption failed:", e)

if __name__ == "__main__":
    main()
