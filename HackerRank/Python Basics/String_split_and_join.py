# trying something new
def split_and_join(line):
    line_parts = line.split()
    return "-".join(line_parts)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
