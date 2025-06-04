import pytest
from encrypter import encrypt_file


def test_encrypt_file():
    input_path = 'sample.txt'
    output_path = 'sample_encrypted.txt'
    key = b'some16bytekey....'  # Depends on your actual implementation

    # Create a sample file
    with open(input_path, 'w') as f:
        f.write('Hello, World!')

    encrypt_file(input_path, output_path, key)

    # Check if encrypted file exists
    with open(output_path, 'rb') as f:
        content = f.read()
        assert content != b'Hello, World!'
