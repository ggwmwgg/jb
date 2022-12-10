import csv
import random
import os.path
from json import dumps
import logging
import shutil
import argparse


flash = {}

parser = argparse.ArgumentParser()
parser.add_argument("--import_from", help = "import from filename")
parser.add_argument("--export_to", help = "export to filename")
args = parser.parse_args()

logger = logging.getLogger()
logging.basicConfig(filename='log.txt', filemode='a', format='%(asctime)s [%(levelname)s]: %(message)s')
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)
logger.addHandler(console_handler)


def addf():

    # Get/check key
    logging.info(f"The card:")
    term = str(input(f"The card:\n"))
    logging.info(term)
    for x, y in flash.items():
        if term == x:
            logging.info(f'Card "{x}" already exists:')
            term = input(f'Card "{x}" already exists:\n')

    # Get/check value
    logging.info("The definition of the card:")
    definition = str(input(f"The definition of the card:\n"))
    logging.info(f"{definition}")
    for x, y in flash.items():
        if definition == y['definition']:
            logging.info(f'''The definition "{y['definition']}" already exists:''')
            definition = input(f'''The definition "{y['definition']}" already exists:\n''')

    flash[term] = {}
    flash[term]['definition'] = definition
    flash[term]['mistakes'] = 0

    # Print key:value
    for x, y in flash.items():
        if term == x:
            logging.info(f"The pair ({x}:{y['definition']}) has been added.")
            print(f"The pair ({x}:{y['definition']}) has been added.")


def removef():

    # Try to remove a key, if not print msg
    logging.info(f"Which card?")
    rm = str(input(f"Which card?\n"))
    logging.info(f"{rm}")
    logging.info(f"{flash}")
    try:
        del flash[rm]
        logging.info(f"The card has been removed.")
        print("The card has been removed.")
    except:
        logging.info(f'''Can't remove "{rm}": there is no such card.''')
        print(f'''Can't remove "{rm}": there is no such card.''')


def importf():

    logging.info("File name:")
    f = str(input("File name:\n"))
    logging.info(f"{f}")
    file_exists = os.path.exists(f)
    if file_exists:
        with open(f, 'r', newline='\n') as file:
            reader = csv.DictReader(file)
            count = 0
            for x in reader:
                t = x['term']
                flash[t] = {}
                flash[t]['definition'] = x['definition']
                flash[t]['mistakes'] = x['mistakes']
                count += 1

        logging.info(f"{count} cards have been loaded.")
        print(f"{count} cards have been loaded.")
    else:
        logging.info("File not found.")
        print("File not found.")


def exportf():

    kek = len(flash)
    logging.info("File name:")
    f = str(input("File name:\n"))
    logging.info(f"{f}")
    with open(f, 'w', newline='\n') as file:
        fieldnames = ['term', 'definition', 'mistakes']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for x, y in flash.items():
            writer.writerow({'term': x, 'definition': y['definition'], 'mistakes': y['mistakes']})

    logging.info(f"{kek} cards have been saved.")
    print(f"{kek} cards have been saved.")


def export_to():
    kek = len(flash)
    logging.info(f"File name: {args.export_to}")
    f = str(args.export_to)
    logging.info(f"{f}")
    with open(f, 'w', newline='\n') as file:
        fieldnames = ['term', 'definition', 'mistakes']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for x, y in flash.items():
            writer.writerow({'term': x, 'definition': y['definition'], 'mistakes': y['mistakes']})

    logging.info(f"{kek} cards have been saved.")
    logging.info(f"{flash} cards have been saved.")
    print(f"{kek} cards have been saved.")


def import_from():

    global flash
    logging.info(f"File name: {args.import_from}")
    f = str(args.import_from)
    logging.info(f"{f}")
    file_exists = os.path.exists(f)
    if file_exists:
        with open(f, 'r', newline='\n') as file:
            reader = csv.DictReader(file)
            count = 0
            for x in reader:
                t = x['term']
                flash[t] = {}
                flash[t]['definition'] = x['definition']
                flash[t]['mistakes'] = x['mistakes']
                count += 1

        logging.info(f"{count} cards have been loaded.")
        logging.info(f"{flash} cards have been loaded.")
        print(f"{count} cards have been loaded.")
    else:
        logging.info("File not found.")
        print("File not found.")


def askf():

    logging.info("How many times to ask?")
    num = int(input("How many times to ask?\n"))
    logging.info(f'{num}')
    gang = list(flash)

    for n in range(num):
        term = random.choice(gang)
        kok = str(input(f'Print the definition of "{term}":\n'))
        logging.info(f'Print the definition of "{term}":')
        logging.info(f'{kok}')
        if flash[term]['definition'] == kok:
            logging.info("Correct!")
            print("Correct!")
        else:
            count = 0
            flash[term]['mistakes'] = int(flash[term]['mistakes'])
            flash[term]['mistakes'] += 1
            for x, y in flash.items():
                if y['definition'] == kok:
                    count = count + 1
                    logging.info(f'''Wrong. The right answer is {flash[term]['definition']}, but your definition is correct for "{x}"''')
                    print(f'''Wrong. The right answer is {flash[term]['definition']}, but your definition is correct for "{x}"''')
            if count == 0:

                logging.info(f'''Wrong. The right answer is {flash[term]['definition']}.''')
                print(f'''Wrong. The right answer is {flash[term]['definition']}.''')


def hardest():

    count = 0
    coco = 0
    lists = []
    for x, y in flash.items():
        if int(y['mistakes']) > count:
            count = int(y['mistakes'])

    for x, y in flash.items():
        if int(y['mistakes']) == count:
            coco += 1

    if coco == 1:
        for x, y in flash.items():
            if int(y['mistakes']) == count:

                logging.info(f'''The hardest card is {x}. You have {count} errors answering it''')
                print(f'''The hardest card is {x}. You have {count} errors answering it''')
    elif count == 0:

        logging.info("There are no cards with errors.")
        print("There are no cards with errors.")
    else:
        for x, y in flash.items():
            if int(y['mistakes']) == count:
                lists.append(x)

        logging.info(f'''The hardest cards are {dumps(lists)[1:-1]}.''')
        print(f'''The hardest cards are {dumps(lists)[1:-1]}.''')


def rstats():

    count = 0
    for x, y in flash.items():
        y['mistakes'] = count

    logging.info(f"Card statistics have been reset.")
    print("Card statistics have been reset.")


def log():
    logging.info("File name:")
    name = str(input("File name:\n"))
    try:
        shutil.copyfile('log.txt', name)
    except shutil.SameFileError:
        pass
    logging.info(name)
    logging.info("The log has been saved.")
    print("The log has been saved.")
    logging.shutdown()

if args.import_from is not None:
    import_from()

# Menu implementation in loop
while True:

    action = str(input(f"Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):\n"))
    if action == "add":
        logging.info(f"User input: Add")
        addf()

    elif action == "remove":
        logging.info(f"User input: Remove")
        removef()

    elif action == "import":
        logging.info(f"User input: Import")
        importf()

    elif action == "export":
        logging.info(f"User input: Export")
        exportf()

    elif action == "ask":
        logging.info(f"User input: Ask")
        askf()

    elif action == "hardest card":
        logging.info(f"User input: Hardest card")
        hardest()

    elif action == "reset stats":
        logging.info(f"User input: Reset stats")
        rstats()

    elif action == "log":
        logging.info(f"User input: Log")
        log()

    elif action == "exit":
        logging.info(f"User exit")
        print("Bye bye!")
        break

if args.export_to is not None:
    export_to()