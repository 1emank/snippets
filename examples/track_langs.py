#tags:files,folders,save,load
#modules:None
#state:unfinished

def get_meta(path):
    file = open(path, mode='r', encoding='utf-8')
    conf_dict = dict()

    try:
        while True:
            line = file.readline()
            if line.startswith('#'):
                key, values_str = line[1:-1].split(':')
                values = values_str.split(',')
                conf_dict.update({key : values})
            else: break
    except: pass

    file.close()

    return conf_dict

languages = (
    ('C', '.c'),
    ('C++', '.cpp'),
    ('Java', '.java'),
    ('Jupyter Notebook', '.ipynb'),
    ('Python', '.py'),
    ('Rust', '.rs')
    )

"""
- explore tree
- track folders
- check if there's a file for every intended language

"""