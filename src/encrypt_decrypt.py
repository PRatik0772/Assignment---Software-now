# Importing required libraries
import string

# Function to encrypt the text
def encrypt_text(input_file, output_file, n, m):
    with open(input_file, 'r') as file:
        text = file.read()
    
    encrypted_text = ""
    for char in text:
        if char.islower():
            if char in string.ascii_lowercase[:13]:  # a-m
                shift = n * m
                new_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            else:  # n-z
                shift = n + m
                new_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
        elif char.isupper():
            if char in string.ascii_uppercase[:13]:  # A-M
                shift = -n
                new_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            else:  # N-Z
                shift = m ** 2
                new_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        else:
            new_char = char  # Special characters and numbers remain unchanged
        encrypted_text += new_char
    
    with open(output_file, 'w') as file:
        file.write(encrypted_text)

# Function to decrypt the text
def decrypt_text(input_file, output_file, n, m):
    with open(input_file, 'r') as file:
        text = file.read()

    decrypted_text = ""
    for char in text:
        if char.islower():
            if char in string.ascii_lowercase[:13]:  # a-m
                shift = n * m
                new_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            else:  # n-z
                shift = n + m
                new_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
        elif char.isupper():
            if char in string.ascii_uppercase[:13]:  # A-M
                shift = -n
                new_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            else:  # N-Z
                shift = m ** 2
                new_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
        else:
            new_char = char
        decrypted_text += new_char
    
    with open(output_file, 'w') as file:
        file.write(decrypted_text)

# Function to check correctness of decrypted text
def check_correctness(original_file, decrypted_file):
    with open(original_file, 'r') as file1, open(decrypted_file, 'r') as file2:
        original_text = file1.read()
        decrypted_text = file2.read()
        return original_text == decrypted_text

# Example usage
encrypt_text("raw_text.txt", "encrypted_text.txt", 2, 3)
decrypt_text("encrypted_text.txt", "decrypted_text.txt", 2, 3)
if check_correctness("raw_text.txt", "decrypted_text.txt"):
    print("Decryption is correct!")
else:
    print("Decryption is incorrect!")
