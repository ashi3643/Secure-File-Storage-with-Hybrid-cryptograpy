# Secure Cloud Storage & Encryption Hybid Cryptography System

## 📜 Overview
The Secure File Storage System is a hybrid cryptographic application designed to enhance the confidentiality, integrity, and availability of sensitive data. By leveraging advanced encryption algorithms and robust file handling mechanisms, this project ensures a secure and efficient file storage solution.

---

## 📂 Features
- **Hybrid Cryptography**: Combines AES, RSA, ChaCha20-Poly1305, AES-GCM, and AES-CCM for robust encryption.
- **File Splitting**: Splits large files into smaller chunks for efficient processing.
- **Key Management**: Secure generation and storage of encryption keys.
- **Flexible Architecture**: Supports multiple encryption modes and algorithms.
- **Scalability**: Designed to handle large datasets with minimal computational overhead.

---

## 🛠️ Technologies Used
- **Programming Language**: Python 3.x
- **Libraries**: Cryptography (Fernet, AES-GCM, AES-CCM, ChaCha20-Poly1305)
- **Development Tools**: Visual Studio Code, Git

---

## 📜 How It Works
1. **Encryption Process**:
   - Splits files into chunks.
   - Encrypts each chunk using different algorithms in a rotating sequence.
   - Generates and securely stores encryption keys and nonces.

2. **Decryption Process**:
   - Retrieves encryption keys and nonces.
   - Decrypts each file chunk.
   - Merges chunks to reconstruct the original file.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed
- Required libraries: Install using `pip install -r requirements.txt`

### Installation
 Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage
1. **Encrypt Files**:
   Place files in the `files` directory and run:
   ```bash
   python encrypter.py
   ```

2. **Decrypt Files**:
   Place encrypted files in the `encrypted` directory and run:
   ```bash
   python decrypter.py
   ```

---

## 📁 Project Structure
```plaintext
secure-file-storage-system/
│
├── files/               # Directory for original files
├── encrypted/           # Directory for encrypted files
├── key/                 # Directory for storing keys
├── raw_data/            # Metadata for file handling
├── restored_file/       # Directory for decrypted files
├── encrypter.py         # Encryption logic
├── decrypter.py         # Decryption logic
├── tools.py             # Helper functions
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
```

---

## 📊 Performance Metrics
- **Encryption Speed**: 500 MB file encrypted in ~3 seconds.
- **Decryption Speed**: 500 MB file decrypted in ~2.8 seconds.
- **Key Generation**: All keys generated within milliseconds.


## 💡 Future Enhancements
- Implement post-quantum cryptography.
- Add a user-friendly GUI for non-technical users.
- Integrate with cloud storage platforms.
