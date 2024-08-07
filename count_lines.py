import os

def count_lines_of_code(directory):
    total_lines = 0
    
    for root, _, files in os.walk(directory):
        for file in files:
            # Filter out non-code files based on file extension
            if file.endswith(('.py', '.java', '.cpp', '.c', '.js', '.html', '.css', '.php', '.ipynb', '.sql')):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', errors='ignore') as f:
                    try:
                        lines = f.readlines()
                        total_lines += len(lines)
                    except Exception as e:
                        print(f"Could not read file {file_path}: {e}")
    
    return total_lines

# Replace 'your_directory_path' with the actual directory path you want to analyze
directory_path = input("target directory?\n")
#directory_path = 'Repo'
total_lines = count_lines_of_code(directory_path)
print(f"Total lines of code in {directory_path}: {total_lines}")
