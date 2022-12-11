## TO DO List (from JetBrains Academy)

#### Program usage: 
The program allows user to create a database for storing tasks and their deadlines.

Available actions:
- add task;
- delete task;
- show today's tasks;
- show week's tasks;
- show all tasks;
- show missed tasks.

The database is created using SQLAlchemy ORM and stored in a file "todo.db" in the same directory as the script file.

#### Technologies used:
- *Python/SQLAlchemy*

#### Usage 
```
python todo.py
```

### Implementation:
(The greater-than symbol followed by a space (```> ```) in examples represents the user input. It's not part of the input.)

- Creates a database file. Name ```todo.db```;
- ```Today's tasks``` item should also print today's date (refer to the Example section for the format).
- ```Add a task``` item should ask for the deadline of the task. Users need to input the deadline in the following format: ```YYYY-MM-DD```;
- ```All tasks```. It prints all tasks sorted by the deadline;  
- ```Missed tasks```Week's tasks```Missed tasks```. It prints all tasks for the next 7 days from today;
- ```Missed tasks```. It prints all the tasks with a missed deadline. Order the tasks by the deadline date;
- ```Delete a task```. It deletes the chosen task. Print ```Nothing to delete``` if the tasks list is empty. This menu should also print all the tasks sorted by the deadline date and ask to enter the number for the task.
- ```Exit``` to stop the program
- Example: 

```
> python todo.py
```

```
1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add a task 
6) Delete a task 
0) Exit
> 4

Missed tasks:
1. Learn the for-loop. 19 Apr

1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add a task 
6) Delete a task 
0) Exit
> 6

Choose the number of the task you want to delete:
1. Learn the for-loop. 19 Apr
2. Learn the basics of SQL. 29 Apr
> 1
The task has been deleted!

1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add a task 
6) Delete a task 
0) Exit
> 4

Missed tasks:
All tasks have been completed! 

1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add a task
6) Delete a task
0) Exit
> 0

Bye!
```

#### Contributing
Pull requests are welcome. For major changes please open an issue first to discuss what you would like to change.
