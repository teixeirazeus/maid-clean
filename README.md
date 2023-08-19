# Maid Clean
Maid Clean is a command-line tool designed to help developers clean up common "junk" directories and files that can accumulate in their projects. It supports cleaning Python projects (__pycache__ directories and .pyc files), JavaScript/Node projects (node_modules directories), and Flutter projects (by running the flutter clean command).

## Installation

```bash
git clone https://github.com/your_username/maid_clean.git
cd maid_clean
pip install -r requirements.txt
```

## Usage
From the project directory, run the script with the desired command.

Clean __pycache__ and .pyc files:
```bash
python maid_clean.py remove_pycache /path/to/your/directory
```

If you don't provide a directory path, it defaults to the current directory.

Remove node_modules directories:
```bash
python maid_clean.py remove_node_modules /path/to/your/directory
```

Run flutter clean on detected Flutter projects:
```bash
python maid_clean.py clean_flutter /path/to/your/directory
```

Execute all cleaning operations:
```bash
python maid_clean.py all /path/to/your/directory
```
## Contribution
Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## License
This project is MIT licensed.