File and Folder Encryption Script with Password Protection

This Python script provides secure encryption and decryption for files and folders using a password-based key generation mechanism. The script uses the cryptography library to implement encryption and decryption with the Fernet symmetric encryption algorithm. It allows users to encrypt sensitive data and decrypt it later using the same password.
Features

    Password-Based Key Derivation: Securely generates an encryption key from a password and salt using the Scrypt key derivation function (KDF).
    Salt Management:
        Automatically generates and saves a unique salt for secure key derivation.
        Can load an existing salt for consistent key generation.
    File Encryption and Decryption:
        Encrypts individual files with Fernet encryption.
        Decrypts encrypted files back to their original state.
    Folder Encryption and Decryption:
        Recursively encrypts all files in a folder, including subfolders.
        Decrypts entire folders and their contents.
    Command-Line Interface: Interactive CLI for encrypting and decrypting files or folders.

How It Works

    Salt Generation:
        A random salt is generated using the secrets module and stored in a salt.salt file.
    Key Derivation:
        The script derives a cryptographic key from a password and salt using the Scrypt KDF.
        This ensures strong encryption and protection against brute-force attacks.
    Encryption:
        Files are read as binary data, encrypted with the Fernet algorithm, and saved back.
        Entire folders can be encrypted recursively.
    Decryption:
        Encrypted files are decrypted using the correct password and key.
        If an invalid password or token is used, the script alerts the user.

Command-Line Usage

The script provides a user-friendly CLI for encrypting or decrypting files and folders.
Arguments

    path: Path to the file or folder to encrypt/decrypt.
    -e, --encrypt: Specifies encryption mode.
    -d, --decrypt: Specifies decryption mode.
    -s, --salt-size: (Optional) Size of the salt to generate for a new key.

Example Usage

    Encrypt a File:

python encryptor.py myfile.txt -e

Decrypt a File:

python encryptor.py myfile.txt -d

Encrypt a Folder:

python encryptor.py myfolder -e

Decrypt a Folder:

python encryptor.py myfolder -d

Generate a Custom Salt:

    python encryptor.py myfile.txt -e -s 32

Important Notes

    Ensure the salt.salt file is stored securely, as it is required for decryption.
    Use a strong and memorable password for enhanced security.
    The same password and salt must be used to decrypt encrypted files or folders.

Prerequisites

    Python 3.x
    cryptography library (pip install cryptography)

How to Run

    Clone the repository:

git clone https://github.com/Alvineeee/Ethical.git
cd Ethical/ProjectA


Run the script:

    python encryptor.py

License

This project is licensed under the MIT License.
