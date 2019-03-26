import os

def add_file_header(lines):
    with open('cmake_header.txt', 'r') as f_header:    #file header need to be specified, not only sample_header
        for line in f_header:
            lines.append(line)
    lines.append('\n\n')

def search_str(str, dir): 
    result=[] 
    for root, dirs, files in os.walk(dir):
        #root:cwd
        #dirs:all subdir in cwd
        #files:all files(not include subdir) in cwd
        for file in files:
            if str in file:
                result.append(file)
    return result

def set_headers(cmake_file, dir):
    cmake_file.append('set(TMP_HEADERS_' + '\n')
    indent='    '
    fixed_words='${CMAKE_CURRENT_LIST_DIR}/'
    headers_list=search_str('.h', dir)
    for headers in headers_list:
        cmake_file.append(indent+fixed_words+headers+'\n')
    cmake_file.append(')\n\n')


def set_sources(cmake_file, dir):
    cmake_file.append('set(TMP_SOURCES_' + '\n')
    indent='    '
    fixed_words='${CMAKE_CURRENT_LIST_DIR}/'
    headers_list=search_str('.cpp', dir)
    for headers in headers_list:
        cmake_file.append(indent+fixed_words+headers+'\n')
    cmake_file.append(')\n\n')

def generate_cmake_file(work_dir):
    cmake_file = []
    add_file_header(cmake_file)
    set_headers(cmake_file, work_dir);
    set_sources(cmake_file, work_dir);
    cmake_file.append('set(CODEC_ULT_HEADERS_ ${CODEC_ULT_HEADERS_} ${TMP_HEADERS_})' + '\n')
    cmake_file.append('set(CODEC_ULT_SOURCES_ ${CODEC_ULT_SOURCES_} ${TMP_SOURCES_})' + '\n')
    path = work_dir.split('ult')[1]
    cmake_file.append('source_group("' + path + '"' + ' FILES ${TMP_HEADERS_} ${TMP_SOURCES_})' + '\n\n')
    cmake_file.append('ult_add_curr_to_include_path()' + '\n')
    return cmake_file


def main():
    #work dir need to be modified according real env
    work_dir = [r'C:\\Users\\jiny\\gfx\\gfx-driver\\Source\\media\\media_embargo\\media_driver_next\\ult\\agnostic\\test\\common\\shared\\scalability', 
                r'C:\\Users\\jiny\\gfx\\gfx-driver\\Source\\media\\media_embargo\\media_driver_next\\ult\\agnostic\\test\\common\\codec\\hal\\enc\\shared\\scalability']
    for dir in work_dir:
        cmake_file = generate_cmake_file(dir)
        completeName = os.path.join(dir, 'ult_srcs.cmake') 
        with open(completeName, 'w') as fout:
            fout.writelines(cmake_file)
    
if __name__ == '__main__':
    main()

