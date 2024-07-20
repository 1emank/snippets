from __future__ import annotations

class example:
    count = 0
    last_value = None
    # Initialization and conversion             # The following methods define what happens when:
    def __new__(cls, param):                    # class(data) -> self   # Usually for inheritance
        """__new__(cls, ...): Creates a new class instance."""
        cls.last_value = param
        cls.count = cls.count + 1
        return super.__new__(param)
    def __init__(self, param) -> None:          # class(data)  
        """__init__(self, ...): Initializes a the new class instance."""
        self.data = param
        self.elements = [0, param, param+10, param+20]
    def __del__(self) -> None:                  # del self
        """__del__(self): Prepares the deletion of the object."""
        print('Deleting')
        example.count = example.count - 1
    def __repr__(self) -> str:                  # repr(self)            # str(self)
        """__repr__(self): Returns a string with an "official" representation of the object."""
        return f'<example: {self.data}'
    def __str__(self) -> str:                   # str(self)
        """__str__(self): Returns a string with an informal representation of the object, readble for the user."""
        return str(self.data)
    def __bool__(self):                         # bool(self)
        """__bool__(self): Defines the conversion of the object to a boolean with bool()."""
        return bool(self.data)
    def __int__(self):                          # int(self)             # Transformación arbitraria
        """__int__(self): Defines the conversion of the object to an integer with int()."""
        return self.data
    def __index__(self):                        # operator.index(self)  # Lossless Integer value
        """__index__(self): Defines the conversion of the object to an integer
        value without loss of information (used by operator.index). It's the
        default method when other numeric representations aren't defined."""
        return self.data
    def __float__(self):                        # float(self)
        """__float__(self): Implementa la conversión a flotante (float())."""
        return float(self.data)
    def __complex__(self):                      # complex(self)
        """__complex__(self): Implementa la conversión a número complejo (complex())."""
        return complex(self.data)
    def __round__(self):                        # round(self)
        """__round__(self) - round to nearest (ties to even): """
        pass
    def __floor__(self):                        # math.floor(self)
        """__floor__(self): - round down (towards negative infinity): """
        pass
    def __ceil__(self):                         # math.ceil(self)
        """__ceil__(self): - round up (towards positive infinity): """
        pass
    def __trunc__(self):                        # math.trunc(self)
        """__trunc__(self): - round towards zero: """
        pass

    # Métodos de Comparación
    def __lt__(self, other):                    # self < other
        """__lt__(self, other): Menor que (<)."""
        return self < other
    def __le__(self, other):                    # self <= other
        """__le__(self, other): Menor o igual que (<=)."""
        return self <= other
    def __eq__(self, other):                    # self == other
        """__eq__(self, other): Igual a (==)."""
        return self.data == other
    def __ne__(self, other):                    # self != other
        """__ne__(self, other): Distinto de (!=)."""
        return self != other
    def __gt__(self, other):                    # self > other
        """__gt__(self, other): Mayor que (>)."""
        return self.data > other
    def __ge__(self, other):                    # self >= other
        """__ge__(self, other): Mayor o igual que (>=)."""
        return self.data >= other

    # Métodos de Contenedores

    def __contains__(self, item):               # X in self
        return item in self.elements
        """__contains__(self, item): Verifica si un ítem está contenido (in)."""
    def __len__(self):                          # len(self)
        """__len__(self): Devuelve la longitud del contenedor (len())."""
        return len(self.elements)
    def __getitem__(self, index : int | slice): # self[x]
        """__getitem__(self, key): Obtiene un ítem ([])."""
        return self.elements[index]
    def __setitem__(self, index, value):        # self[x] = y
        """__setitem__(self, key, value): Establece un ítem ([])."""
        self.elements[index] = value
    def __delitem__(self, index):               # del self[x]
        """__delitem__(self, key): Elimina un ítem (del)."""
        del self.elements[index]
    def __iter__(self):                         # for item in self | a, b, c = self
        """__iter__(self): Devuelve un iterador (iter())."""
        self.index = 0
        return self
    def __next__(self):                         # for item in self | a, b, c = self
        """__next__(self): Devuelve el siguiente ítem (next())."""
        if self.index < len(self.elements):
            out = self.elements[self.index]
            self.index = self.index + 1
            return out
        else:
            raise StopIteration        
    
    #Métodos de Aritmética y Operadores
    def __add__(self, other):                   # self + other
        """__add__(self, other): Suma (+)."""
        try: return self.data + other
        except: return NotImplemented # Important
    def __radd__(self, other):                  # other + self
        """__radd__(self, other): Suma reflejada (+)."""
        self.__add__(other)
    def __sub__(self, other):                   # self - other
        """__sub__(self, other): Resta (-)."""
        try: return self.data - other
        except: return NotImplemented # Important
    def __rsub__(self, other):                  # other - self
        """__rsub__(self, other): Resta reflejada (-)."""
        try: return other - self.data
        except: return NotImplemented
    def __mul__(self, other):                   # self * other
        """__mul__(self, other): Multiplicación (*)."""
        try: return self.data * other
        except: return NotImplemented # Important
    def __rmul__(self, other):                  # other * self
        """__rmul__(self, other): Multiplicación reflejada (*)."""
        self.__mul__(other)
    def __truediv__(self, other):               # self / other
        """__truediv__(self, other): División (/)."""
        try: return self.data / other
        except: return NotImplemented # Important
    def __rtruediv__(self, other):              # other / self
        """__rtruediv__(self, other): División reflejada (/)."""
        try: return other / self.data
        except: return NotImplemented # Important
    def __floordiv__(self, other):              # self // other
        """__floordiv__(self, other): División entera (//)."""
        try: return self.data // other
        except: return NotImplemented # Important
    def __rfloordiv__(self, other):             # other // self
        """__rfloordiv__(self, other): División entera reflejada (//)."""
        try: return other // self.data
        except: return NotImplemented # Important
    def __mod__(self, other):                   # self % other
        """__mod__(self, other): Módulo (%)."""
        try: return self.data % other
        except: return NotImplemented # Important
    def __rmod__(self, other):                  # other % self
        """__rmod__(self, other): Módulo reflejado (%)."""
        try: return other % self.data
        except: return NotImplemented # Important
    def __pow__(self, other):                   # self ** other
        """__pow__(self, other): Potencia (**)."""
        try: return self.data ** other
        except: return NotImplemented # Important
    def __rpow__(self, other):                  # other ** self
        """__rpow__(self, other): Potencia reflejada (**)."""
        try: return other ** self.data
        except: return NotImplemented # Important
    def __and__(self, other):                   # self and other    self & other
        """__and__(self, other): Operación AND bit a bit (&, and)."""
        try: return self.data and other 
        except: return NotImplemented # Important
    def __rand__(self, other):                  # other and self    other & self
        """__rand__(self, other): Operación AND bit a bit reflejada (&, and)."""
        self.__and__(other)
    def __or__(self, other):                    # self or other     self | other
        """__or__(self, other): Operación OR bit a bit (|, or)."""
        try: return self.data or other
        except: return NotImplemented # Important
    def __ror__(self, other):                   # other of self     other | self
        """__ror__(self, other): Operación OR bit a bit reflejada (|, or)."""
        self.__or__(other)
    def __xor__(self, other):                   # self ^ other
        """__xor__(self, other): Operación XOR bit a bit (^)."""
        try: return self.data ^ other
        except: return NotImplemented # Important
    def __rxor__(self, other):                  # other ^ self
        """__rxor__(self, other): Operación XOR bit a bit reflejada (^)."""
        self.__xor__(other)
    def __lshift__(self, other):                # self << other     # Mueve un bit a la izquierda
        """__lshift__(self, other): Desplazamiento de bits a la izquierda (<<)."""
        try: return self.data << other
        except: return NotImplemented # Important
    def __rlshift__(self, other):               # other << self     # Esencialmente multiplica x2
        """__rlshift__(self, other): Desplazamiento de bits a la izquierda reflejado (<<)."""
        try: return other << self.data
        except: return NotImplemented # Important
    def __rshift__(self, other):                # self >> other     # Mueve un bit a la derecha
        """__rshift__(self, other): Desplazamiento de bits a la derecha (>>)."""
        try: return self.data >> other
        except: return NotImplemented # Important
    def __rrshift__(self, other):               # other >> self     # Esencialmente divide //2 
        """__rrshift__(self, other): Desplazamiento de bits a la derecha reflejado (>>)."""
        try: return other >> self.data
        except: return NotImplemented # Important

    # Métodos de Asignación Aritmética
    def __iadd__(self, other):                  # self += other
        """__iadd__(self, other): Asignación de suma (+=)."""
        self.data = self.data + other
    def __isub__(self, other):                  # self -= other
        """__isub__(self, other): Asignación de resta (-=)."""
        self.data = self.data - other
    def __imul__(self, other):                  # self *= other
        """__imul__(self, other): Asignación de multiplicación (*=)."""
        self.data = self.data * other
    def __itruediv__(self, other):              # self /= other
        """__itruediv__(self, other): Asignación de división (/=)."""
        self.data = self.data / other
    def __ifloordiv__(self, other):             # self //= other
        """__ifloordiv__(self, other): Asignación de división entera (//=)."""
        self.data = self.data // other
    def __imod__(self, other):                  # self %= other
        """__imod__(self, other): Asignación de módulo (%=)."""
        self.data = self.data % other
    def __ipow__(self, other):                  # self **= other
        """__ipow__(self, other): Asignación de potencia (**=)."""
        self.data = self.data ** other
    def __iand__(self, other):                  # self &= other
        """__iand__(self, other): Asignación de AND bit a bit (&=)."""
        self.data = self.data & other
    def __ior__(self, other):                   # self |= other
        """__ior__(self, other): Asignación de OR bit a bit (|=)."""
        self.data = self.data | other
    def __ixor__(self, other):                  # self ^= other
        """__ixor__(self, other): Asignación de XOR bit a bit (^=)."""
        self.data = self.data ^ other
    def __ilshift__(self, other):               # self <<= other
        """__ilshift__(self, other): Asignación de desplazamiento a la izquierda (<<=)."""
        self.data = self.data << other
    def __irshift__(self, other):               # self >>= other
        """__irshift__(self, other): Asignación de desplazamiento a la derecha (>>=)."""
        self.data = self.data >> other


    # Otros Métodos Mágicos
    """__call__(self, *args, **kwargs): Permite que una instancia sea llamada como una función (())."""
    """__enter__(self): Implementa la entrada de contexto con with."""
    """__exit__(self, exc_type, exc_value, traceback): Implementa la salida de contexto con with."""
    """__copy__(self): Soporte para la copia superficial."""
    """__deepcopy__(self, memo): Soporte para la copia profunda."""

    @staticmethod
    def backups():
        print("""
            Method          Dunder      Backup(s)

            bool            __bool__    __len__
            str             __str__     __repr__
            int             __int__     __index__
            float           __float__   __index__
            complex         __complex__ __float__   __index__
            operator.index  __index__   None
            math.ceil       __ceil__    __float__   __index__
            math.floor      __floor__   __float__   __index__
            math.trunc      __trunc__   None
            """)