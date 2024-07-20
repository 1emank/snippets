#tags:classes
#modules:typing,Literal,Iterable,__future__,annotations
#state:chaos
from __future__ import annotations
from typing import Literal, Iterable

__all__ = ['Fretting', 'Note', 'Tuning']

# nota : natural, #, b, ##, bb
noteToValue = { #dict
    ('C', 'B#', None, None, 'Dbb') : 0,
    (None, 'C#', 'Db', None, None) : 1,
    ('D', None, None, 'C##', 'Ebb'): 2,
    (None, 'D#', 'Eb', None, None) : 3,
    ('E', None, 'Fb', 'D##', None) : 4,
    ('F', 'E#', None, None, 'Gbb') : 5,
    (None, 'F#', 'Gb', None, None) : 6,
    ('G', None, None, 'F##', 'Abb'): 7,
    (None, 'G#', 'Ab', None, None) : 8,
    ('A', None, None, 'G##', 'Bbb'): 9,
    (None, 'A#', 'Bb', None, None) :10,
    ('B', None, 'Cb', 'A##', None) :11
    }
valueToNote = ( #tuple
    ('C', 'B#', None, None, 'Dbb') ,
    (None, 'C#', 'Db', None, None) ,
    ('D', None, None, 'C##', 'Ebb'),
    (None, 'D#', 'Eb', None, None) ,
    ('E', None, 'Fb', 'D##', None) ,
    ('F', 'E#', None, None, 'Gbb') ,
    (None, 'F#', 'Gb', None, None) ,
    ('G', None, None, 'F##', 'Abb'),
    (None, 'G#', 'Ab', None, None) ,
    ('A', None, None, 'G##', 'Bbb'),
    (None, 'A#', 'Bb', None, None) ,
    ('B', None, 'Cb', 'A##', None)
    )

def count_alterations(notes : Iterable[int]) -> str:
    natural : int = 0
    sharp   : int = 0
    flat    : int = 0
    d_sharp : int = 0
    d_flat  : int = 0

    for item in notes:
        if valueToNote[item][0] != None:
            natural = natural + 1
            continue
        if valueToNote[item][1] != None: sharp   = sharp + 1 
        if valueToNote[item][2] != None: flat    = flat + 1
        if valueToNote[item][3] != None: d_sharp = d_sharp + 1
        if valueToNote[item][4] != None: d_flat  = d_flat + 1

    sorted_list = sorted((
        (natural, 'natural'),
        (sharp, 'sharp'),
        (flat, 'flat'),
        (d_sharp, 'd_sharp'),
        (d_flat, 'd_flat')
    ), key=lambda x:x[0], reverse=True)

    return 'unfinished'

class Note:
    def __init__(self, note : str | int = 'eb4', muted : bool = False) -> None:
        self.note : int = -1
        if isinstance(note, int):
            self.name : str = dict()[note % 12]
            self.note : int = note
        if isinstance(note, str):
            self.name : str = note[0].upper()
        self.muted = muted
        
        for item in notes.keys():
            if note[:-1].strip().lower() in item:
                self.note = int(notes[item])
                break

        if self.note < 0 :
            raise Exception(
                "Invalid note: Valid notes are A,B,C,D,E,F,G (uppercase or lowercase)," +\
                "and valid alterations are #, ##, b and bb.")

        self.alteration : str = ''
        self.octave : int = -99
        if note[-2] in '1234567890':
            self.alteration : str = note[1:-2].lower()
            self.octave = int(note[-2:])
        else:
            self.alteration : str = note[1:-1].lower()
            self.octave = int(note[-1])
        
        self.abs = self.note + (self.octave * 12)

        if self.octave == -99: raise Exception("An unknown error ocurred.")
    
    def __str__(self) -> str: return self.name+self.alteration+str(self.octave)
    def __add__(self, value : Note | int ) -> Note:         # self + other
        return Note( self.note + value)
    def __radd__(self, value : Note | int ) -> Note: pass   # other + self
    def __sub__(self, value : Note | int ) -> Note: pass    # self - other
    def __rsub__(self, value : Note | int ) -> Note: pass   # other - self
    def __int__(self) -> int: return self.note

    def interval(self, other_note : Note): return other_note.abs - self.abs

class Tuning:
    def __init__(self, *tuning : Note | str ) -> None:
        self.string_dict = dict()
        for string_n, index in zip( range(len(tuning), 0, -1), range(len(tuning)), strict=True ):
                self.string_dict.update( {string_n : index} )

        if isinstance(tuning[0], Note):
            self.tuning : tuple[Note, ...] = tuning
        if isinstance(tuning[0], str) :
            self.tuning : tuple[Note, ...] = tuple(Note(item) for item in tuning)
        relative = [0]

        root : Note = tuning[0]
        i = 1
        while i < len(tuning):
            relative.append(root.interval(tuning[i]))
            i = i + 1

        self.relative = tuple(relative)
            
    def notes_from_frets(self, frets : Fretting):
        out = []
        root = -1
        for item in frets.absolute:
            if item == 'X':
                out.append('X')
                continue
            if root == -1:
                root = int(item)
                out.append(0)
                continue
            out.append( int(item) - root )

        return out
    
    def __str__(self) -> str: return '<Tuning: '+' '.join( str(note) for note in self.tuning )+'>'

class Fretting:
    def __init__(self, frets : str) -> None:
        def relative_fret(frets : tuple[int | str, ...]):
            rel_frets : list[int|str] = []
            start_fret : int = -1
            for item in frets:
                if item == 'X': rel_frets.append('X')   # Añadir 'X' y seguir
                elif 0 not in rel_frets:        # Si no hay primer traste y el traste es válido
                    rel_frets.append(0)         # Añadir 0
                    start_fret = int(item)      # Guardar valor
                else: rel_frets.append( int(item) - start_fret )
                # Al nuevo traste le restamos el original
            return tuple(rel_frets)
        
        self.raw = frets.upper().strip()
        self.absolute = tuple( int(item) if item.upper() != 'X' else 'X' for item in frets)
        self.relative = relative_fret(self.absolute)
        self.a = self.absolute
        self.r = self.relative

    def __next__(self):
        if self.index < len(self.a):
            a = self.a[self.index]
            r = self.r[self.index]
            self.index = self.index + 1
            return a, r
        else:
            raise StopIteration

    def __len__(self): return len(self.a)
    def __contains__(self, item : Literal['x'] | int ): return item in self.a or item in self.r
    def __str__(self) -> str: return '<Fretting: '+self.raw+'>'
            
    @staticmethod
    def max_fret( n : int ) -> str:
        return ''.join( tuple('X' if i == -1 else str(i) for i in range(-1, n+1)) )
    # Output 'x012[...]n'

    @staticmethod
    def filter_frets(*frets : str, minimum_notes : int, additional_rules : Iterable[str] = ('False',)) -> tuple[str, ...]:
        def enough_notes(fretting): return sum( 1 if fret != 'X' else 0 for fret in fretting ) >= minimum_notes
        def properly_muted(fretting):
            for i, item in enumerate(fretting):
                if i == 0: continue
                match (fretting[i-1], fretting[i]):
                    case ('X', 'X'): return False
                    case ('0', 'X'): return False
                    case     _     : continue
            return True
        
        out : list[str] = list(frets)
        del_list : list[int] = []
        for i, fretting in enumerate(out):
            if not enough_notes(fretting):
                del_list.append(i)
                continue
            if not properly_muted(fretting):
                del_list.append(i)
                continue
            for item in additional_rules:
                if eval(item):
                    del_list.append(i)
                    continue

        for i in reversed(del_list): del out[i]
        return tuple(out) 

standard = Tuning( *(Note(item) for item in ('E2', 'A2', 'D3', 'G3', 'B3', 'E4')) )
print( standard )
print( standard.notes_from_frets(Fretting('X02220')) )


#
#
#
# nota : natural, #, b, ##, bb
# buscar mayor coincidencia
# 