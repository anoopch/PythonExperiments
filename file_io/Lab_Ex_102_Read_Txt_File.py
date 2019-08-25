# Program to read an entire text file
# Test File - /Users/anoop/Downloads/2173 Software engineers and designers.docx
import chardet


def read_file(file_path):
    file_pointer = None
    file_data = ''
    try:
        file_pointer = open(file_path, 'rb', 2)
        encoding = chardet.detect(file_pointer.read())
        print(encoding)
        if encoding.get('encoding') is not None:
            while True:
                data = file_pointer.read()
                if data is not None and len(data) > 0:
                    file_data += data
                else:
                    break
        else:
            print('Sorry!! Unknown File Encoding. Please try another file')
    except FileNotFoundError as e:
        print(f'No file found at {file_path}. Are you sure the file is available and the path has "Read" access?')
    except IOError as e:
        print('Unable to open file', e)
    except Exception as e:
        print('unable to read file\n', e)
    finally:
        if file_pointer is not None:
            file_pointer.close()
    return file_data


file_name = input('Enter a file name - ')
print(str(read_file(file_name)))
