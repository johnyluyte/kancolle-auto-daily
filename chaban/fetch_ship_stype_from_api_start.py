# -*- coding: utf-8 -*-


def main():
    with open('api_start2_long.json','r') as in_file, open('kcShipStype.json','w') as out_file:
        for line in in_file:
            check_write_to_file(out_file, line)

def check_write_to_file(out_file, line):
    test = line.strip()
    if test.startswith('{') or test.startswith('}') or test.startswith('"api_name"') or test.startswith('"api_sortno"') or test.startswith('"api_mst_ship": ['):
        out_file.write(line)
        return True
    elif test.startswith('"api_stype"'):
        out_file.write(line.rstrip()[:-1])
        return True
    return False


if __name__ == '__main__':
    main()
