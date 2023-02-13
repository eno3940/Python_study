file_path = "/Users/inho/Python_study/data-01-test-score.csv"
def read_file(file_path):
    file_list= []
    file = open(file_path, 'r')
    while True:
        file_line= file.readline().rstrip('\n')
        if file_line:
            file_line = file_line.split(',')
            file_list.append(file_line)
        else:
            break
    return file_list

print(read_file(file_path),)