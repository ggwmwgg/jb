## Arithmetic Exam Application (from JetBrains Academy)

#### Description
Program that will generate a mathematical expression for a user to solve with various levels of difficulty and saving results/showing progress of learning.

#### Technologies used:
- *Python*

#### Usage 
```
python arithmetic.py
```
### Implementation:
(The greater-than symbol followed by a space (```> ```) in example represents the user input. It's not part of the input.)
- With the first message, the program should ask for a difficulty level:
	- simple operations with numbers 2-9
	- integral squares 11-29
- A user enters an answer. For the first difficulty level: the task is a simple math operation; the answer is the result of the operation. For the second difficulty level: the task is an integer; the answer is the square of this number. In case of another input: ask to re-enter. Repeat until the format is correct.
- The application gives 5 tasks to a user.
- The user receives one task, prints the answer. If the answer contains a typo, print ```Incorrect format```. and ask to re-enter the answer. Repeat until the answer is in the correct format. If the answer is a number, print ```Right!``` or ```Wrong!``` Go to the next question.
- After five answers, print ```Your mark is N/5```. where ```N``` is the number of correct answers.
- Output ```Would you like to save your result to the file? Enter yes or no.``` In case of ```yes```, ```YES```, ```y```, ```Yes```: the app should ask the username and write ```Name: n/5 in level X (<level description>)```. (```X``` stands for the level number) in the ```results.txt``` file. For example — ```Alex: 3/5 in level 1 (simple operations with numbers 2-9)```. The results should be saved to the file immediately after the user gave the positive answer to the question ```Would you like to save your result to the file?```. If the file ```results.txt``` does not exist, it will be created.
- In case of ```no``` or any other word: exit the program.
- Example:
```
Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29
> 11
Incorrect format.
Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29
> 2
11
> 121
Right!
15
> 100
Wrong!
21
> 441'
Wrong format! Try again.
21
> 441
Right!
17
> 289
Right!
13
> 169
Right!
Your mark is 4/5. Would you like to save the result? Enter yes or no.
> yes
What is your name?
> Kate
The results are saved in "results.txt".
```

#### Contributing

Pull requests are welcome. For major changes please open an issue first to discuss what you would like to change.