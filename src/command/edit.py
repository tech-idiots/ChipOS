import libs.term as term
def run(file_path):
    term.clear_terminal()
    print(f"Opening file: {file_path}")
    try:
        with open(file_path, 'r') as file:
            for line in file:
                print(line, end='')  
        print("\n--- End of file ---\n")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
   
    
    


