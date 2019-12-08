import requests
import json

ENDPOINT = 'https://enigmatic-plains-7414.herokuapp.com/'

def evaluate_chunk(chunk: 'List') -> 'Tuple(Int, Char)':
    password_char_idx = int(chunk[0])
    char_coords = json.loads(chunk[1])
    grid = chunk[2:]

    print('char idx: %s' % password_char_idx)
    print('char coords: %s' % char_coords)
    print(grid)
    password_char =  chr(grid[len(grid) - 1 - int(char_coords[1])][int(char_coords[0])])
    print('got password char %s' % password_char)
    return password_char_idx, password_char

# def retrieve_stream():
#     stream = requests.get(ENDPOINT, stream=True)
#     chunk_lines = []

#     for line in stream.iter_lines():
#         if not line:
#             password_idx, password_char = evaluate_chunk(chunk_lines)
#             password, complete = assemble_password(password_idx, password_char)

#             if complete:
#                 print('password: %s ' % password)

#             chunk_lines = []
#         chunk_lines.append(line)


def assemble_password():
    password = {}
    password_string = ''
    chunk_lines = []

    stream = requests.get(ENDPOINT, stream=True)

    for line in stream.iter_lines():
        if not line:
            password_idx, password_char = evaluate_chunk(chunk_lines)

            if password_idx in password:
                print('DONE')
                print(password)
                for i in range(len(password)):
                    password_string += password[i]

                return password_string
            else:
                password[password_idx] = password_char

            chunk_lines = []
        else:
            chunk_lines.append(line)

    return None, None

print(assemble_password())
