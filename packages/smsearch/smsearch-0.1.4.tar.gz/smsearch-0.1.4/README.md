# Recursive File Searcher with Boolean Expressions

This Python script allows you to recursively search for files within a directory based on a boolean expression of keywords. It supports AND (`&`), OR (`|`), and parentheses for grouping, providing a flexible way to define search criteria. Matching file content can optionally be copied to the clipboard.

## Features

* **Recursive Search:** Traverses subdirectories within the specified directory.
* **Boolean Expressions:** Uses `&` (AND), `|` (OR), and parentheses for complex search logic.
* **File Pattern Inclusion/Exclusion:** Filter files based on include and exclude patterns (e.g., `*.txt`, `*.log`).
* **Clipboard Copying:** Copy the content of all matching files to the clipboard for easy access.
* **Error Handling:** Gracefully handles file read errors and invalid directory specifications.
* **Colored Output:** Uses color-coded output for improved readability (requires `colorama`).
* **File Grouping by Extension:** Groups found files by their extensions for clearer presentation.
* **UTF-8 Support:** Handles files encoded in UTF-8.

## Installation

You can install this package using pip:

```bash
pip install smsearch
```

## Usage

After installation, you can use the `smsearch` command:

```
smsearch <directory> <expression> [--include <pattern>] [--exclude <pattern>] [-c]
```

**Arguments:**

* `<directory>`: The directory to search in.
* `<expression>`: The boolean expression to search for. Use `&` for AND, `|` for OR, and parentheses for grouping.
* `--include <pattern>` (optional): Include only files matching this pattern. Uses `fnmatch` syntax.
* `--exclude <pattern>` (optional): Exclude files matching this pattern. Uses `fnmatch` syntax.
* `-c`, `--copy` (optional): Copy the content of matching files to the clipboard.

**Examples:**

* Search for files containing both "word1" and "word2":

  ```bash
  smsearch /path/to/search "word1 & word2"
  ```

* Search for files containing either "python" or "java", and also containing "code":

  ```bash
  smsearch /path/to/search "(python | java) & code"
  ```

* Search for files containing "important" and either "urgent" or "critical":

  ```bash
  smsearch /path/to/search "important & (urgent | critical)"
  ```

* Search for files containing either "error" or "exception" in `.log` files, excluding `.gz` files:

  ```bash
  smsearch /path/to/search "error | exception" --include "*.log" --exclude "*.gz"
  ```

* Search for files containing "confidential" and either "password" or "secret", and copy the content to the clipboard:

  ```bash
  smsearch /path/to/search "confidential & (password | secret)" -c
  ```

## How it Works

The script uses the `pyparsing` library to parse the boolean expression and `os.walk` to recursively search the directory. It opens each file, reads its content, and evaluates the boolean expression against the content. Matching files are printed to the console, grouped by extension. If the `-c` or `--copy` flag is set, the content of matching files is concatenated and copied to the clipboard.

## Contributing

Contributions are welcome! Please feel free to submit pull requests for bug fixes, new features, or improvements to the documentation.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file for details.