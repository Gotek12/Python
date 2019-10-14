#!/usr/bin/python3
# -*- coding: iso-8859-2 -*-

##created by: Wojciech Ładyga

import builtins
import string

#2.1
print("2.2 - Keywords")
print(dir(__builtins__))
# wynik: ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']

#2.10
print("\n2.10")
line = "Mamy napis \nwielowierszowy line \n\n4fun "
print(line)
#dzielimy linie - split() i liczymy dł - len()
print("Ilosc wyrazów w napisie: ",len(line.split()))
#wynik: 5

#2.11
print("\n2.11")
slowo = "word"
wynik = ""
for i in range(0, len(slowo)):
    wynik += slowo[i]
    if i != len(slowo)-1:
        wynik += "_"
print(slowo, " -> ", wynik)
#wynik: w_o_r_d

#2 sposób
list = [slowo[i] for i in range(0, len(slowo))]
print(slowo, " -> ", '_'.join(list))
#wynik: w_o_r_d

#2.12
print("\n2.12")
last = ""
first = ""
lineTmp = line.split()
for i in lineTmp:
    first += i[0]
    last += i[len(i)-1]
print("Pierwsze znaki: -> ", first)
#wynik: Mnwl4
print("Ostatnie znaki -> ", last)
#wynik: ysyen

#2.13
print("\n2.13")
dlugosc = 0
slowa = line.split()
for i in slowa:
    dlugosc += len(i)
print("Długość wyrazow w napisie -> ", dlugosc)
#wynik: 31

#2 sposób
print("Długość wyrazow w napisie #2 ->", sum(1 for i in line if i.isspace()!= True))
#wynik: 31

#2.14
print("\n2.14")
maxi = 0
tmp = ""
for i in slowa:
    l = len(i)
    if l > maxi:
        tmp = i
        maxi = len(i)
print("Najdłuższe słowo -> ", tmp, " ma dl -> ", maxi)
#wynik: wielowierszowy, 14

#2 sposób
print("Najdłuższe słowo -> ", max(slowa), " ma dl -> ", len(max(slowa)))
#wynik: wielowierszowy, 14

#2.15
print("\n2.15")
wynik = ""
L = [7, 6, 5, 4, 3, 2, 1]
for i in range(len(L)):
    wynik += str(L[i])
print(wynik)

#2 sposób
print(''.join(map(str, L))) #z konwersj int to string
#wynik: 7654321

#3 - jeśli chcemy aby były posortowane i odzielone przecinkiem
K = L.sort()
print(', '.join(map(str, L)))
#wynik: 1, 2, 3, 4, 5, 6, 7

#2.16
print("\n2.16")
line = "Tworca pythona jest GvR"
newLine = line.replace("GvR", "Guido van Rossum")
print(newLine)
#wynik: Autorem pythona Guido van Rossum

#2.17
print("\n2.17")
line = "java, c, python, a moze inny jezyk programowania,\nktory jest lepszy"
listaSplit = line.split()
#alfabetycznie
print(sorted(listaSplit))
#wynik: ['a', 'c,', 'inny', 'java,', 'jest', 'jezyk', 'ktory', 'lepszy', 'moze', 'programowania,', 'python,']

#po długości
print(sorted(listaSplit, key=len))
#wynik: ['a', 'c,', 'moze', 'inny', 'jest', 'java,', 'jezyk', 'ktory', 'lepszy', 'python,', 'programowania,']

#2.18
print("\n2.18")
liczba = 10203000400500060060
newLiczba = str(liczba)
counter = 0
for i in range(len(newLiczba)):
    if newLiczba[i] == "0":
        counter += 1
print("Ilość powtarzających się 0 to -> ", counter)
#wynik: 13

#2.19
print("\n2.19")
L = [12, 123, 32, 23, 234, 45, 6, 67, 8, 125, 176]
LStr = []
for i in range(len(L)):
    LStr.append(str(L[i]).zfill(3)) #dopełnienie każdego el do 3
print(LStr)
#wynik: ['012', '123', '032', '023', '234', '045', '006', '067', '008', '125', '176']