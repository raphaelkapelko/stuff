import os

tasks_file = open(os.path.join(os.path.dirname(__file__), 'tasks.txt'))
text = tasks_file.read()

ls = [t.split() for t in text.splitlines()]

ls_in = [l[1:l.index("OUT:")] for l in ls]
ls_out = [l[l.index("OUT:")+1:] for l in ls]

def find_unique(l):
    out = set()
    for el in l:
        out.update(el)
    return out

reverse_dict = lambda dict: {value:key for key, value in dict.items()}

encode_in = {val:idx for idx, val in enumerate(find_unique(ls_in))}
decode_in = reverse_dict(encode_in)

encode_out = {val:idx for idx, val in enumerate(find_unique(ls_out))}
decode_out = reverse_dict(encode_in)

encode = lambda data, encoder: [[encoder[item] for item in el] for el in data]

encoded_in = encode(ls_in, encode_in)
encoded_out = encode(ls_out, encode_out)