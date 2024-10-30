<p align="center"><img alt="The age logo, an wireframe of St. Peters dome in Rome, with the text: age, file encryption" width="600" src="https://user-images.githubusercontent.com/1225294/132245842-fda4da6a-1cea-4738-a3da-2dc860861c98.png"></p>

This is a cross-platform GUI for the file encryption tool [age](https://age-encryption.org). This program wraps the `age` , and uses python's Subprocess library functions to securely call age commands. The UI is built on top of Flet.

The format specification is at age-encryption.org/v1. To discuss the spec or other age related topics, please email the mailing list at age-dev@googlegroups.com. age was designed by [@Benjojo12](https://twitter.com/Benjojo12) and [@FiloSottile](https://twitter.com/FiloSottile). .



# Installation & Compilation

## Option 1: Install from PyPI (Recommended)

```
pip install agecrypt
```

After installation, you can run the program by typing:
```
agecrypt
```

## Option 2: Run from source

1. Download and extract the archive or clone the repository
2. Install the required dependencies:

```
pip install -r requirements.txt
```

3. Run the program
```
python -m agecrypt
```

## Option 3: Compile from source

1. Download and extract the source archive
2. Install build requirements:

```
pip install build wheel
```

3. Build the package:

```
python -m build
```

4. Install the resulting wheel file:

```
pip install dist/agecrypt-1.0.0-py3-none-any.whl
```

After installation, run the program by typing:

```
agecrypt
```

# Use

To generate a new identity, click the `Generate X25519 key pair` radio option, and `Select Output File`

To encrypt a file, click the `Encrypt` radio option, choose to `armor` the output or not. Select the input + output files, recipient keys or recipient file(s) or identity file(s) and hit `Execute`

To decrypt an `.age` file after selection `Decrypt`, select input file using `Select Input` and specify the passphrase or identity file.

To encrypt to multiple recipients, specify a recipient text file with one recipient on each line. To encrypt to a single recipient, you can paste it directly in the `Recipient Keys` text field.

# Compilation instructions

1. Install [Rust](https://www.rust-lang.org/tools/install), open `winage`, and run `cargo build --release`.

2. Install and open Visual Studio 2019. Go to `Extensions` > `Manage Extensions` and install `Microsoft Visual Studio Installer Projects`. Open the `winage\winage\age.sln` Solution, select `Release`, `x64`, and build.

# Restrictions

- All features supported by age work (No restrictions)
