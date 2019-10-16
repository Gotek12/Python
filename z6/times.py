#!/usr/bin/python
# -*- coding: iso-8859-2 -*-


class Time:
    """Klasa reprezentuj�ca odcinek czasu."""

    def __init__(self, s=0):
        """Zwraca instancj� klasy Time."""
        self.s = int(s)

    def __str__(self):
        """Zwraca string 'hh:mm:ss'."""
        sec = self.s % (24 * 3600)
        h = sec // 3600  # dzielenie ca�kowite
        sec %= 3600
        m = sec // 60
        sec %= 60
        return "{0:02d}:{1:02d}:{2:02d}".format(h, m, sec)

    def __repr__(self):
        """Zwraca string 'Time(s)'."""
        return "Time({0})".format(self.s)

    def __add__(self, other):
        """Dodawanie odcink�w czasu."""
        return Time(self.s + other.s)

    def __cmp__(self, other):  # por�wnywanie, -1|0|+1
        """Por�wnywanie odcink�w czasu."""
        return cmp(self.s, other.s)

    def __int__(self):  # int(time1)
        """Konwersja odcinka czasu do int."""
        return self.s