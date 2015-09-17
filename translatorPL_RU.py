# -*- coding: utf-8 -*-
import json
alphabet_f = open("alphabet.json", "r")
alphabet = json.load(alphabet_f)
alphabet_f.close()


def main(first=True):
    if first:
        print "--------------------------------------"
        print "Zamiennik polskich liter na rosyjskie"
        print "--------------------------------------"

    print "Podaj literę:"
    letter = raw_input()
    letter = letter.lower()

    if letter in alphabet:
        print "Rosyjski odpowiednik: "
        print alphabet[letter]
    else:
        print 'Chyba coś źle wpisałeś..'

    main(first=False)

if __name__ == "__main__":
    try:
        main(first=True)
    except KeyboardInterrupt:
        print "\nBye in polish xD"
