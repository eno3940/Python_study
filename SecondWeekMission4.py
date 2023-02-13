file_path = "/Users/inho/Python_study/data-01-test-score.csv"

class ReadCSV():
    def __init__(self,file_path):
        self.file_path = file_path

    def read_file(self):
        file_list = []
        file = open(file_path, 'r')
        while True:
            file_line= file.readline().rstrip('\n')
            if file_line:
                file_line = list(map(int,file_line.split(',')))
                file_list.append(file_line)
            else:
                break
        return file_list
    def merge_list(self):
        file_list = self.read_file()
        merge_list = [sum(file_line) for file_line in file_list]
        return merge_list
read_csv = ReadCSV(file_path)
print(read_csv.read_file())
print(read_csv.merge_list())