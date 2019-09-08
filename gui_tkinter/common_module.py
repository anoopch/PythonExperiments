file_name = 'user_data.txt'


def validate_field(entry_list):
    for e in entry_list:
        if e is not None and e.get() is not None and "" is not e.get():
            continue
        else:
            return False
    return True


def delete_line(username):
    f = None
    lines = None
    try:
        f = open(file_name, 'r')
        lines = f.readlines()
    except IOError:
        print('Error')
    finally:
        if f is not None:
            f.close()
    try:
        f = open(file_name, 'w')
        username += ','
        for line in lines:
            if not line.startswith(username):
                f.write(line)
    except IOError:
        print('Error')
    finally:
        if f is not None:
            f.close()


def is_data_in_file(username):
    try:
        f = open(file_name, "r")
        try:
            data_lines = f.readlines()
            for line in data_lines:
                if line.startswith(username):
                    f.close()
                    return True
        except IOError:
            print('Exception occurred')
        finally:
            f.close()
    except FileNotFoundError:
        print('File is not yet created')
    return False


def insert_into_file(line):
    username = line.split(',', 1)
    if len(username) > 0 and is_data_in_file(username[0]):
        delete_line(username[0])
    line += '\n'
    f = open(file_name, "a+")
    try:
        f.write(line)
    except IOError:
        print('unable to write to file')
    finally:
        f.close()


def is_authentication_valid(username, password):
    f = None
    lines = None
    username += ','
    try:
        f = open(file_name, 'r')
        lines = f.readlines()
    except IOError:
        print('Error')
    finally:
        if f is not None:
            f.close()

    for line in lines:
        if line.startswith(username):
            data = line.split(',')
            if data[2] == password:
                return True
    return False


def get_name(username):
    f = None
    lines = None
    username += ','
    try:
        f = open(file_name, 'r')
        lines = f.readlines()
    except IOError:
        print('Error')
    finally:
        if f is not None:
            f.close()

    for line in lines:
        if line.startswith(username):
            data = line.split(',')
            return data[1]
    return None
