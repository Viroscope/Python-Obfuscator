import re

def remove_comments(source_code):
    source_code = re.sub(r'#[^\n]*', '', source_code)
    
    source_code = re.sub(r'""".*?"""', '', source_code, flags=re.DOTALL)
    source_code = re.sub(r"'''.*?'''", '', source_code, flags=re.DOTALL)
    
    return source_code

def obfuscate_strings(source_code):
    obfuscated_code = ""
    string_variables = {}
    variable_counter = 0
    
    strings = re.findall(r'("[^"]*")|(\'[^\']*\')', source_code)
    
    for string in strings:
        variable_name = f"_var{variable_counter}"
        string_variables[variable_name] = string[0] if string[0] else string[1]
        obfuscated_code = source_code.replace(string[0] if string[0] else string[1], variable_name)
        source_code = obfuscated_code
        variable_counter += 1
    
    string_vars_code = ""
    for variable_name, string_value in string_variables.items():
        string_vars_code += f"{variable_name} = {string_value}\n"
    
    obfuscated_code = string_vars_code + obfuscated_code
    
    return obfuscated_code

def main():
    input_file = input("Enter the name of the input Python file: ")
    
    try:
        with open(input_file, "r") as file:
            source_code = file.read()
        
        source_code = remove_comments(source_code)
        
        obfuscated_code = obfuscate_strings(source_code)
        
        output_file = f"obfuscated_{input_file}"
        with open(output_file, "w") as file:
            file.write(obfuscated_code)
        
        print(f"Obfuscated code has been written to {output_file}")
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
