# Program to read an entire text file
import chardet


def read_file(file_path):
    file_pointer = None
    file_data = ''
    try:
        file_pointer = open(file_path, 'rb', 2)
        encoding = chardet.detect(file_pointer.read())
        print(encoding)
        while True:
            data = file_pointer.read()
            if data is not None and len(data) > 0:
                file_data += data
            else:
                break
    except IOError as e:
        print('unable to access file', e)
    except Exception as e:
        print('unable to read file\n', e)
    finally:
        if file_pointer is not None:
            file_pointer.close()
    return file_data


file_name = input('Enter a file name - ')
print(read_file(file_name))
