def read_the_file(file_name):
    with open(file_name) as file_log:
        for row in file_log:
            yield row


def main():
    for row in read_the_file("file.txt"):
        if row.lower().startswith("error"):
            print(row)
