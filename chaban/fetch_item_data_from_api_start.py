# -*- coding: utf-8 -*-


def main():
    with open('old_item.json','r') as in_file, open('new_item','w') as out_file:
        for line in in_file:
            check_write_to_file(out_file, line)

def check_write_to_file(out_file, line):
    test = line.strip()
    if test.startswith('{') or test.startswith('}') or test.startswith('"api_id"') or test.startswith('"api_sortno"'):
        out_file.write(line)
        return True
    elif test.startswith('"api_name"'):
        out_file.write(line.rstrip()[:-1])
        return True
    return False


if __name__ == '__main__':
    main()
