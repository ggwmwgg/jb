## Flashcards (from JetBrains Academy)

#### Description 
Flashcards game, where you can create, delete, import or export flashcards, store them as well as user scores.

#### Technologies used:
- *Python*

#### Usage 
```
python flashcards.py
```
```
python flashcards.py --import_from=derivatives.txt
```
```
python flashcards.py --export_to=animals.txt
```
```
python flashcards.py --import_from=words13june.txt --export_to=words14june.txt
```
```
python flashcards.py --export_to=vocab.txt --import_from=vocab.txt
```
### Implementation:
(The greater-than symbol followed by a space (```> ```) in examples represents the user input. It's not part of the input.)

- Display information about a single card on the screen.
- Compare the lines and work with conditions: display the card and the user's answer on the screen.
- Practice arrays and looops: create a new card for the program to play.
- Learn to use hashtables, display key values, work with exceptions in order to fix problem of repeating cards.
	- Example:
	```
	Input the number of cards:
	> 2
	The term for card #1:
	> print()
	The definition for card #1:
	> outputs text
	The term for card #2:
	> print()
	The term "print()" already exists. Try again:
	> str()
	The definition for card #2:
	> outputs text
	The definition "outputs text" already exists. Try again:
	> converts to a string
	Print the definition of "print()":
	> outputs text
	Correct!
	Print the definition of "str()":
	> converts to a string
	Correct!
	```
	
- Work with files: create a menu that allows you to add, delete, save, and upload saved cards in the game.
	- Example:
	```
	Input the action (add, remove, import, export, ask, exit):
	> import
	File name:
	> ghost_file.txt
	File not found.

	Input the action (add, remove, import, export, ask, exit):
	> add
	The card:
	> Japan
	The definition of the card:
	> Tokyo
	The pair ("Japan":"Tokyo") has been added.

	Input the action (add, remove, import, export, ask, exit):
	> add
	The card:
	> Russia
	The definition of the card:
	> UpdateMeFromFile
	The pair ("Russia":"UpdateMeFromFile") has been added.

	Input the action (add, remove, import, export, ask, exit):
	> import
	File name:
	> capitals.txt
	28 cards have been loaded.

	Input the action (add, remove, import, export, ask, exit):
	> ask
	How many times to ask?
	> 1
	Print the definition of "Russia":
	> Moscow
	Correct!

	Input the action (add, remove, import, export, ask, exit):
	> export
	File name:
	> capitalsNew.txt
	29 cards have been saved.

	Input the action (add, remove, import, export, ask, exit):
	> exit
	Bye bye!
	```

- Using statistics, set a correct answer for each card and theach the game to determine which cards was the hardest to solve.
	- Example:
	```
	Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
	> hardest card
	There are no cards with errors.

	Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
	> import
	File name:
	> capitals.txt
	28 cards have been loaded.

	Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
	> hardest card
	The hardest card is "France". You have 10 errors answering it.

	Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
	> ask
	How many times to ask?
	> 1
	Print the definition of "Russia":
	> Paris
	Wrong. The right answer is "Moscow", but your definition is correct for "France" card.

	Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
	> hardest card
	The hardest cards are "Russia", "France". You have 10 errors answering them.

	Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
	> reset stats
	Card statistics have been reset.

	Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
	> hardest card
	There are no cards with errors.

	Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
	> log
	File name:
	> todayLog.txt
	The log has been saved.

	Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):
	> exit
	Bye bye!
	```
	
#### Contributing

Pull requests are welcome. For major changes please open an issue first to discuss what you would like to change.