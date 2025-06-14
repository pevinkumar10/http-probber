def read_from_file(file):

    try:
        with open (file,"r") as opened_file:
            contents = opened_file.readlines()
            return contents
        
    except FileNotFoundError as Fe:
        print(f"[ ! ] The file '{file}' doesn't exist")
        exit(1)

    except PermissionError as Pe:
        print(f"[ ! ] Permission denied for '{file}' ")
        exit(1)