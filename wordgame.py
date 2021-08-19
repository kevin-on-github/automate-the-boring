import csv
import secrets


def generateRandom():

    with open('wordlist.csv') as f:
        csv_read = csv.reader(f, delimiter=',')
        list_of_rows = list(csv_read)
        verb = list_of_rows[secrets.randbelow(61)][1]
        noun = list_of_rows[secrets.randbelow(61)][2]
        adjec = list_of_rows[secrets.randbelow(61)][3]
        print(f'That {noun} really is {adjec}. Im gonna {verb}.')


generateRandom()
