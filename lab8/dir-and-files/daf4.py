def count_lines(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            line_count = sum(1 for line in file)
            print(f"The number of lines in the file '{file_path}' is: {line_count}")
    except FileNotFoundError:
        print(f"The specified file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")


path = "row.txt"
count_lines(path)
