## Smart Calculator (from JetBrains Academy)

#### Description: 
Smart calculator which supports functions mentioned in implementation 

#### Technologies used:
- *Python*

#### Usage 
```
python calculator.py
```
### Implementation:
(The greater-than symbol followed by a space (```> ```) in example represents the user input. It's not part of the input.)

- Read two integer numbers from the same line and prints their sum in the standard output. Numbers can be positive, negative, or zero.
- Reads two numbers in a loop and prints the sum in the standard output.
- If a user enters only a single number, the program should print the same number. If a user enters an empty line, the program should ignore it.
- Add to the calculator the ability to read an unlimited sequence of numbers.
- Encounting an empty line, do not output anything.
- The program must calculate expressions like these: ```4 + 6 - 8```, ```2 - 3 - 4```, and so on.
- Decompose your program using functions to make it easy to understand and edit later.
- The program should print ```Invalid expression``` in cases when the given expression has an invalid format. If a user enters an invalid command, the program must print ```Unknown command```. All messages must be printed without quotes. The program must never throw an exception.
- To handle incorrect input, you should remember that the user input that starts with ```/``` is a command, in other situations, it is an expression.
- Do not forget to write methods to decompose your program.
- ```/help``` command should print information about your program. When the command ```/exit``` is entered, the program must print ```Bye!``` , and then stop.
- Program should support variables. Use ```dict``` to store them.
- Program should support multiplication ```*```, integer division ```/``` and parentheses ```(...)```. To do this, use infix to postfix conversion algorithm above and then calculate the result using stack.
- Sequence of ```+``` (like ```+++``` or ```+++++```) is an admissible operator that should be interpreted as a single plus. A sequence of ```-``` (like ```--``` or ```---```) is also an admissible operator and its meaning depends on the length. If a user enters a sequence of ```*``` or ```/```, the program must print a message that the expression is invalid.
- Example:
```
> 8 * 3 + 12 * (4 - 2)
48
> 2 - 2 + 3
3
> 4 * (2 + 3
Invalid expression
> -10
-10
> a=4
> b=5
> c=6
> a*2+b*3+c*(2+3)
53
> 1 +++ 2 * 3 -- 4
11
> 3 *** 5
Invalid expression
> 4+3)
Invalid expression
> /command
Unknown command
> /exit
Bye!
```

#### Contributing

Pull requests are welcome. For major changes please open an issue first to discuss what you would like to change.