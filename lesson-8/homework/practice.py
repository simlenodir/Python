def create_alphabet_file(filename, letters_per_line):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # English alphabet
    lines = []
    
    # Split the alphabet into chunks of the specified number of letters per line
    for i in range(0, len(alphabet), letters_per_line):
        lines.append(alphabet[i:i + letters_per_line])
    
    try:
        with open(filename, 'w') as file:
            for line in lines:
                file.write(line + '\n')  # Write each line followed by a newline
        
        print(f"File '{filename}' created successfully!")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
filename = 'alphabet.txt'  # File where the alphabet will be saved
letters_per_line = 5  # Specify the number of letters per line
create_alphabet_file(filename, letters_per_line)
