# Secure File Storage System Using Hybrid Cryptography

A robust file storage system that implements multiple encryption algorithms to ensure maximum security for stored files. The system uses a combination of AES, ChaCha20Poly1305, AES-GCM, and AES-CCM encryption methods to provide layered security.

## Features

- **Hybrid Encryption**: Implements multiple encryption algorithms:
  - AES in CBC mode with 128-bit keys
  - ChaCha20Poly1305 for high-speed encryption
  - AES-GCM for authenticated encryption
  - AES-CCM for combined encryption and authentication

- **Secure File Management**:
  - File upload and download through a web interface
  - Secure key management
  - File integrity verification
  - Automatic file restoration

- **Web Interface**:
  - User-friendly file upload/download
  - Secure key distribution
  - File status tracking
  - Responsive design

## Prerequisites

- Python 3.6 or higher
- Required Python packages (install using `pip install -r requirements.txt`):
  - Flask==2.2.2
  - cryptography==2.9.2
  - werkzeug
  - gunicorn==20.0.4

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ashi3643/Secure-File-Storage.git
   cd Secure-File-Storage
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create required directories:
   ```bash
   mkdir files encrypted key raw_data uploads restored_file
   ```

## Usage

### Command Line Usage

1. **Encrypting Files**:
   - Place the file to be encrypted in the `files` directory
   - Run the encryption script:
     ```bash
     python encrypter.py
     ```
   - The encrypted file will be stored in the `encrypted` directory
   - A key file (Main_Key.pem) will be generated in the `key` directory

2. **Decrypting Files**:
   - Ensure the Main_Key.pem file is in the `key` directory
   - Run the decryption script:
     ```bash
     python decrypter.py
     ```
   - The decrypted file will be restored in the `files` directory

### Web Interface Usage

1. Start the web server:
   ```bash
   python app.py
   ```

2. Access the web interface at `http://localhost:8000`

3. **Uploading Files**:
   - Click "Upload" in the web interface
   - Select the file to encrypt
   - Download and securely store the generated key file

4. **Downloading Files**:
   - Click "Download" in the web interface
   - Upload the key file (Main_Key.pem)
   - Download the decrypted file

## Security Features

1. **Multiple Encryption Layers**:
   - Files are encrypted using different algorithms in rotation
   - Each file uses a unique combination of encryption methods
   - Keys are themselves encrypted for additional security

2. **Key Management**:
   - Secure key generation
   - Encrypted key storage
   - Key rotation support
   - Secure key distribution

3. **File Protection**:
   - Secure file transfer
   - File integrity verification
   - Automatic file restoration
   - Secure file deletion

## Project Structure

```
Secure-File-Storage/
├── files/              # Directory for files to be encrypted
├── encrypted/          # Directory for encrypted files
├── key/               # Directory for encryption keys
├── raw_data/          # Directory for raw encrypted data
├── uploads/           # Directory for uploaded files
├── restored_file/     # Directory for decrypted files
├── templates/         # HTML templates
├── static/           # Static files (CSS, JS)
├── app.py            # Flask web application
├── encrypter.py      # File encryption module
├── decrypter.py      # File decryption module
├── divider.py        # File division module
├── restore.py        # File restoration module
└── tools.py          # Utility functions
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Cryptography library for encryption algorithms
- Flask framework for web interface
- Contributors and maintainers of the project

## Contact

For questions and support, please open an issue in the GitHub repository.

## Technical Details

### Encryption Algorithms

1. **AES in CBC Mode (128-bit)**
   - Block size: 128 bits
   - Key size: 128 bits
   - Uses PKCS7 padding
   - IV (Initialization Vector) is randomly generated for each encryption
   - Provides confidentiality through block cipher chaining

2. **ChaCha20Poly1305**
   - Stream cipher with 256-bit key
   - 96-bit nonce
   - 128-bit authentication tag
   - Provides both confidentiality and authenticity
   - High performance on modern CPUs

3. **AES-GCM (Galois/Counter Mode)**
   - Block size: 128 bits
   - Key size: 128 bits
   - 96-bit nonce
   - 128-bit authentication tag
   - Provides authenticated encryption
   - Hardware-accelerated on modern processors

4. **AES-CCM (Counter with CBC-MAC)**
   - Block size: 128 bits
   - Key size: 128 bits
   - Variable nonce length (7-13 bytes)
   - Provides authenticated encryption
   - Suitable for constrained environments

### Encryption Process Flow

1. **File Preparation**:
   - File is read in binary mode
   - Split into chunks of 1MB
   - Each chunk is processed independently

2. **Key Generation**:
   - Master key is generated using `os.urandom(32)`
   - Key is encrypted using RSA-2048
   - Encrypted key is stored in PEM format

3. **Encryption Steps**:
   - Each chunk is encrypted using a rotating algorithm sequence
   - Nonce/IV is generated for each encryption operation
   - Authentication tags are generated and stored
   - Metadata is encrypted separately

## API Documentation

### REST API Endpoints

1. **File Upload**
   ```
   POST /upload
   Content-Type: multipart/form-data
   
   Parameters:
   - file: The file to encrypt (required)
   
   Response:
   {
     "status": "success",
     "message": "File encrypted successfully",
     "key_file": "path/to/key.pem"
   }
   ```

2. **File Download**
   ```
   POST /download
   Content-Type: multipart/form-data
   
   Parameters:
   - key_file: The encryption key file (required)
   
   Response:
   - File download stream
   ```

3. **File Status**
   ```
   GET /status/<filename>
   
   Response:
   {
     "status": "encrypted|decrypted",
     "algorithm": "AES-CBC|ChaCha20|AES-GCM|AES-CCM",
     "timestamp": "2024-03-14T12:00:00Z"
   }
   ```

### Python API

1. **Encryption**
   ```python
   from encrypter import encrypt_file
   
   # Encrypt a file
   key_path = encrypt_file("path/to/file.txt")
   ```

2. **Decryption**
   ```python
   from decrypter import decrypt_file
   
   # Decrypt a file
   decrypt_file("path/to/encrypted/file", "path/to/key.pem")
   ```

## Troubleshooting Guide

### Common Issues and Solutions

1. **Key File Not Found**
   - Error: "Key file not found in the specified directory"
   - Solution: Ensure Main_Key.pem is in the `key` directory
   - Check file permissions

2. **Encryption Failed**
   - Error: "Failed to encrypt file"
   - Solution: Check file size and permissions
   - Verify sufficient disk space
   - Ensure file is not corrupted

3. **Decryption Failed**
   - Error: "Failed to decrypt file"
   - Solution: Verify key file integrity
   - Check if key file matches the encrypted file
   - Ensure no file corruption

4. **Web Interface Issues**
   - Error: "Connection refused"
   - Solution: Check if Flask server is running
   - Verify port 8000 is not in use
   - Check firewall settings

5. **Performance Issues**
   - Slow encryption/decryption
   - Solution: Check system resources
   - Verify file size is within limits
   - Consider increasing chunk size

## Component Documentation

### 1. Encrypter Module (`encrypter.py`)
- Handles file encryption using multiple algorithms
- Manages key generation and storage
- Implements chunk-based processing
- Provides progress tracking

### 2. Decrypter Module (`decrypter.py`)
- Manages file decryption process
- Handles key verification
- Implements file reconstruction
- Provides integrity checking

### 3. Web Interface (`app.py`)
- Flask-based web application
- Handles file uploads and downloads
- Manages user sessions
- Provides status monitoring

### 4. File Division (`divider.py`)
- Splits files into manageable chunks
- Manages chunk metadata
- Handles file reconstruction
- Implements progress tracking

### 5. Restoration Module (`restore.py`)
- Manages file restoration process
- Handles chunk reassembly
- Verifies file integrity
- Provides error recovery

### 6. Utility Functions (`tools.py`)
- Provides helper functions
- Manages file operations
- Handles error logging
- Implements security checks

## Security Best Practices

1. **Key Management**
   - Store keys securely
   - Implement key rotation
   - Use secure key distribution
   - Backup keys safely

2. **File Handling**
   - Verify file integrity
   - Implement secure deletion
   - Use secure file transfer
   - Monitor file access

3. **System Security**
   - Regular security updates
   - Access control implementation
   - Audit logging
   - Security monitoring
