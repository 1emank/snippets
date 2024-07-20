#tags:combinatorics,map,files,save,load
#modules:itertools,product,os,ast,literal_eval
#state:unfinished
from __future__ import annotations
from itertools import product
from tunings_classes import Fretting
from typing import TextIO
import os
from ast import literal_eval

tunings_file = '/'.join(  __file__.split('/')[:-1]  )+'/files/tunings.txt'
class data:
    source_frets : tuple[str, ...] = tuple()
    ok_frets : list[str] = []
    i : int = 0
    done : bool = False

    len_source = 0

def get_frets():
    def load_line(file : TextIO): return literal_eval(file.readline())
    if os.path.exists(tunings_file):
        with open(tunings_file, mode='r', encoding='utf-8') as file:
            data.source_frets   = tuple(load_line(file))
            data.ok_frets       = list( load_line(file))
            data.i              = int(  load_line(file))
            data.done           = bool( load_line(file))
            data.len_source     = len(data.source_frets)

def save_frets():
    with open(tunings_file, mode='w', encoding='utf-8') as file:
        if not data.done:
            print( data.source_frets, data.ok_frets, data.i, False \
                  , sep='\n', file=file )
        else:
            print( (None,), data.ok_frets, 0, True \
                  , sep='\n', file=file )

def produce_frettings(*, max_fret : int, minimum_notes : int , strings : int = 6 ):
    return Fretting.filter_frets( *tuple(''.join(item) for item in \
            product(  Fretting.max_fret(max_fret), repeat=strings)  ), \
            minimum_notes=minimum_notes)

def select_frets():
    while data.i < data.len_source:
        print(data.len_source - data.i, 'frets remaining')
        try: command = input(f"Is this fretting possible (or useful)?\n\n{data.source_frets[data.i]}\n")
        except: break

        match command.lower():
            case 'yes' | 'y' | 'si' | 's':
                data.ok_frets.append( str(data.source_frets[data.i]) )
            case 'no' | 'n' : pass
            case 'stop' | 'cerrar' | 'detener' | 'exit' : break
            case _ : continue
        data.i = data.i + 1
        

### BEGIN ###
get_frets()

if data.source_frets == tuple() and not data.done:
    data.source_frets = produce_frettings( max_fret=3, minimum_notes=5 )
    data.len_source = len( data.source_frets )

if not data.done:
    select_frets()
    save_frets()