def load_dictionary(file_path):
    with open(file_path, 'r') as lines:
        return [line.strip() for line in lines]
    

