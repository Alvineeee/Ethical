Here’s a description you can use for your GitHub repository:
Shift Cipher Encoder-Decoder

This Python script implements a simple Shift Cipher (Caesar Cipher), a classic encryption technique where each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. It allows users to encode and decode messages, print substitution tables, and dynamically change the shift value.
Features

    Encoding Messages: Encrypts a message using the Caesar Cipher based on the current shift value.
    Decoding Messages: Decrypts a message back to plaintext using the inverse substitution table.
    Customizable Shift Value: Users can change the shift value (n) at any time.
    Substitution Tables: Displays encoding and decoding mappings in an easy-to-read format.
    Interactive Menu: User-friendly CLI interface for managing cipher operations.

How It Works

    Create Substitution Tables:
        Generates mappings for encoding and decoding based on a shift value (n).
    Encoding:
        Each letter in the message is shifted by n positions in the alphabet.
        Non-alphabetic characters remain unchanged.
    Decoding:
        Each letter in the encoded message is shifted backward by n positions to retrieve the original message.
    Custom Shift:
        Change the value of n to redefine the substitution mappings.

Menu Options

    Print Encoding/Decoding Tables:
        Displays the current substitution mappings.
    Encode Message:
        Encrypts a user-provided message using the current shift value.
    Decode Message:
        Decrypts a user-provided message using the current shift value.
    Change Shift:
        Allows the user to set a new shift value.
    Quit:
        Exits the program.

Example

For a shift value of n = 3:

    Plaintext: HELLO
    Encoded: KHOOR
    Decoded: HELLO

Prerequisites

    Python 3.x
    No external libraries are required.
