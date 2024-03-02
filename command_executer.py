import subprocess

def execute_bash_commands(file_path):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Remove leading and trailing whitespaces
                command = line.strip()
                
                # Execute the bash command
                subprocess.run(command, shell=True, check=True)
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'your_file.txt' with the path to your text file
file_path = 'list_command.txt'
execute_bash_commands(file_path)
