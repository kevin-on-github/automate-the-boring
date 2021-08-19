import csv
import secrets


class Words:
    def __init__(self):
        with open('wordlist.csv') as f:
            self.csv_read = csv.reader(f, delimiter=',')
            self.list_of_rows = list(self.csv_read)

    def verb(self):
        verb = self.list_of_rows[1 + secrets.randbelow(60)][1]
        return verb

    def noun(self):
        noun = self.list_of_rows[1 + secrets.randbelow(60)][2]
        return noun
    
    def adjec(self):
        adjec = self.list_of_rows[1 + secrets.randbelow(60)][3]
        return adjec


w = Words()

print(f'The {w.noun()} {w.verb()} my {w.noun()}, and {w.verb()} the {w.adjec()} {w.noun()} while attempting to {w.verb()}.')







'''
def generateRandom():

    with open('wordlist.csv') as f:
        csv_read = csv.reader(f, delimiter=',')
        list_of_rows = list(csv_read)
        verb = list_of_rows[secrets.randbelow(61)][1]
        noun = list_of_rows[secrets.randbelow(61)][2]
        adjec = list_of_rows[secrets.randbelow(61)][3]
        print(f'That {noun} really is {adjec}. Im gonna {verb}.')


generateRandom()
'''