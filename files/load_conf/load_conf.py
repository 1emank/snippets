#tags:files,load
#modules:shlex
#state:finished
#modified:2024-07-10

import shlex

def get_conf(path,
             assignator = '=',
             comment_sign = '#',
             unpack_singles = True
             ) -> dict :
    
    """
    Function for reading typical configuration files, such as .conf or .ini,
    with lines structured as `key = value[s]`. It returns a dictionary with
    key-value pairs. Values are splitted like typical shell arguments, with
    shlex.split, and saved in a tuple. For example:

    The line: `conf_key = value "this isn't multiple values "`
    Will become: `{'conf_key' : ('value', "this isn't multiple values ") }`

    Since the output is a dictionary, if a key is repeated, only the last
    value is saved. If the value of a key is empty, it'll be saved as None.
    
    Arguments:
    - path: Path to the configuration file to read.
    - assignator: Symbol that relates the key with the value. Usually = or :
    - comment_sign: Symbol that indicates a comment, so it can be ignored.
    - unpack_singles: If True, `key = value`, becomes `{ 'key' : 'value' }`,
    instead of `{ 'key' : ( 'value' ,) }`
    """

    file = open(path, mode='r', encoding='utf-8')
    conf_dict = dict()

    for raw_line in file:
        line = raw_line.split(comment_sign)[0]
        if len(line) < 2: continue
        
        line = tuple(item.strip() for item in line.split(assignator, maxsplit=1))
        key = line[0]

        values = tuple( shlex.split(line[1]) )

        match ( len(values), unpack_singles ):
            case ( 1 , True ) : values = values[0]
            case ( 0, False ) : values = (None,)
            case ( 0 , True ) : values = None

        conf_dict.update( {key : values} )

    file.close()

    return conf_dict

conf_file_path = '/'.join(__file__.split('/')[:-3])+'/examples/files/example.conf'

conf = get_conf(conf_file_path, unpack_singles=True)
for i in conf: print(i , '=', conf[i])

help(get_conf)