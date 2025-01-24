from pathlib import Path
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--dirpath', default='', required=False)
parser.add_argument('--files', nargs='*')
files = list(Path(parser.parse_args().dirpath).glob('*'))
if parser.parse_args().files is None:
    size, cnt = 0, 0
    for i in range(len(files)):
        if not files[i].is_dir():
            size += files[i].stat().st_size
            cnt += 1
    print(f'В папке {cnt} файлов с суммарным размером {size}kb')
else:
    in_files = parser.parse_args().files
    filenames = []
    for i in range(len(files)):
        filenames.append(files[i].name)
    print('Файлы в папке:')
    with open('file1.txt', 'w') as out:
        for i in range(len(in_files)):
            print(in_files[i])
            out.write(in_files[i] + '\n')
    print('Файлы не в папке:')
    with open('file2.txt' 'w') as out:
        for i in range(len(in_files)):
            if in_files[i] not in filenames:
                print(in_files[i])
                out.write(in_files[i] + '\n')