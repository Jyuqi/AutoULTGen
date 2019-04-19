# generate unified cmd config file from .h, no use now
from ult_generator import header_parser
import re
import os


def main(input_file='input.txt', media_path='C:\\Users\\jiny\\gfx\\gfx-driver\\Source\\media\\\media_driver\\agnostic'):
       with open(input_file, 'r') as fin:
        for line in fin:
            line = line.strip()
            if not line:
                continue
            idx = line.rfind('/')
            file_name = line[idx+1:]
            file_path = line[:idx+1]
            parser_list = [header_parser.HeaderParser(file_name, file_path)]
            # print(os.getcwd())
            parser_list[0].read_file()
            xml_tree_str = parser_list[0].parse_file_info()
            with open( file_name + '.xml', "w") as f:
                f.write(xml_tree_str)


if __name__ == '__main__':
    main()