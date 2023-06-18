# Python Obfuscator

This is a Python script that can obfuscate strings and remove comments from a given Python source code file. It uses regular expressions to identify and manipulate strings and comments in the source code.

## Functionality

The script provides two main functions:

1. `remove_comments(source_code)`: This function removes all comments from the given `source_code` string. It uses regular expressions to match and remove both single-line comments (lines starting with `#`) and multi-line comments enclosed in triple quotes (`"""..."""` or `'''...'''`). The resulting modified source code string without comments is returned.

2. `obfuscate_strings(source_code)`: This function obfuscates the strings in the given `source_code` string. It identifies strings using regular expressions and replaces them with variable names. The obfuscated code is returned as a string. Additionally, it creates string variable assignments for the obfuscated strings at the beginning of the code.

The script also contains a `main()` function that interacts with the user. It prompts the user to enter the name of the input Python file. It then reads the contents of the file, removes comments using the `remove_comments()` function, obfuscates the strings using the `obfuscate_strings()` function, and finally writes the obfuscated code to a new file with a filename prefixed with "obfuscated_" in the same directory.

If an error occurs during the execution of the script, appropriate error messages are displayed to the user.

## Usage

To use the code obfuscator script, follow these steps:

1. Make sure you have Python installed on your system.

2. Save the script to a Python file, for example, `code_obfuscator.py`.

3. Open a command prompt or terminal and navigate to the directory where the script is located.

4. Run the script by executing the following command:

   ```
   python code_obfuscator.py
   ```

5. The script will prompt you to enter the name of the input Python file.

6. Provide the name of the file (including the file extension) and press Enter.

7. The script will process the file, obfuscate the strings, remove comments, and create a new file with the obfuscated code.

8. The obfuscated code will be saved in a file named `obfuscated_input_file.py`, where `input_file.py` is the name of the input file.

9. The script will display a message indicating the success of the obfuscation process and the name of the output file.

## Note

- The script uses regular expressions to match strings and comments, so it may not handle all possible cases. It is designed to work with common Python code patterns, but there may be some cases where the obfuscation may not be perfect or some comments may not be removed.

- The script assumes that the input file exists in the same directory as the script file. If the file is located in a different directory, provide the path along with the file name when prompted.

- The script overwrites the output file if it already exists. Make sure to provide a unique input file name to avoid unintentional data loss.
