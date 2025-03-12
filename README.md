# Split Secret (sisec) 🔐
[![GitHub Sponsors](https://img.shields.io/badge/Sponsor-GitHub%20Sponsors-blue?logo=github)](https://github.com/sponsors/kevinveenbirkenbach) [![Patreon](https://img.shields.io/badge/Support-Patreon-orange?logo=patreon)](https://www.patreon.com/c/kevinveenbirkenbach) [![Buy Me a Coffee](https://img.shields.io/badge/Buy%20me%20a%20Coffee-Funding-yellow?logo=buymeacoffee)](https://buymeacoffee.com/kevinveenbirkenbach) [![PayPal](https://img.shields.io/badge/Donate-PayPal-blue?logo=paypal)](https://s.veen.world/paypaldonate)


[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) [![GitHub stars](https://img.shields.io/github/stars/kevinveenbirkenbach/split-secret.svg?style=social)](https://github.com/kevinveenbirkenbach/split-secret/stargazers)

Split Secret is a versatile command-line tool for securely splitting a master secret among multiple users. Only when a defined quorum of users combines their secret shares can the original secret be decrypted. The tool also supports robust encryption, decryption, and cleanup operations to ensure sensitive data is managed securely throughout the process.

---

## 🛠 Features

- **Secret Splitting:** Divide a master secret into shares distributed among users.
- **Encryption & Decryption:** Securely encrypt and decrypt data files using strong cryptographic methods.
- **User Management:** Add and manage user information along with their secret shares.
- **Cleanup Operations:** Remove decrypted files after processing to maintain security.
- **Interactive Modes:** Operate in active, preview, or interactive modes to match your workflow.
- **Parallel Processing:** Efficiently handles file operations using process pooling.

---

## 📥 Installation

Install Split Secret via [Kevin's Package Manager](https://github.com/kevinveenbirkenbach/package-manager) under the alias `sisec`:

```bash
package-manager install sisec
```

This command installs Split Secret globally, making it available as `sisec` in your terminal. 🚀

---

## 🚀 Usage

Split Secret offers several modes for managing your secrets. Here are a few example commands:

### Cleanup Data
To delete all unnecessary decrypted and encrypted files:
```bash
sisec --mode cleanup
```

### Encrypt Data & Generate Meta Data
Encrypt the master secret file and generate encrypted metadata with additional user information:
```bash
sisec --secret-holders-amount 3 --quota 50 --mode encrypt --add-user-information --master-password "your_master_password" --meta --add-user-information << EOL
Alan Turing
+12358
turing@turing-bomb.world
Bletchley Park
¯\_(ツ)_/¯
Ada Lovelace
+132134
best@algorythm.ai
Somewhere in London
:)
John von Neumann
+5488142
test@test3.de
Washington D.C.
<3 <3 <3
EOL
```

### Decrypt Meta Data File
To decrypt the accumulated metadata file:
```bash
sisec --mode decrypt --meta
```

For additional commands and options (such as user-specific decryption, file type filtering, or recursive processing), use:
```bash
sisec --help
```

---

## 🧑‍💻 Author

Developed by **Kevin Veen-Birkenbach**  
- 📧 [kevin@veen.world](mailto:kevin@veen.world)  
- 🌐 [https://www.veen.world](https://www.veen.world)

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 🤝 Contributions

Contributions are welcome! Please feel free to fork the repository, submit pull requests, or open issues if you have suggestions or encounter any problems. Let's work together to make secure secret management accessible and efficient! 😊
