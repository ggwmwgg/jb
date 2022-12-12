## Food Blog Backend (from JetBrains Academy)

#### Program usage: 
A simple backend that allows to populate an SQLite3 database. Knowledge for auto-increment primary key and how to use foreign keys to create relationships between tables, many-to-many relations, with SQL queries, and with database cursor methods.

#### Technologies used:
- *Python/argparse/SQLITE3*

#### Usage 
```
python fb.py
```

### Implementation:
(The greater-than symbol followed by a space (```> ```) in examples represents the user input. It's not part of the input.)

- Example 1: 

```
> python fb.py food_blog.db
```

```
> python fb.py food_blog.db
Pass the empty recipe name to exit.
Recipe name: > Milkshake
Recipe description: > Blend all ingredients and put in the fridge.
1) breakfast  2) brunch  3) lunch  4) supper
Enter proposed meals separated by a space: > 1 3 4
Input quantity of ingredient <press enter to stop>: > 500 ml milk
Input quantity of ingredient <press enter to stop>: > 1 cup strawberry
Input quantity of ingredient <press enter to stop>: > 1 tbsp sugar
Input quantity of ingredient <press enter to stop>: >
Pass the empty recipe name to exit.
Recipe name: > Hot cacao
Recipe description: > Pour the ingredients into the hot milk. Mix it up.
1) breakfast  2) brunch  3) lunch  4) supper
Enter proposed meals separated by a space: > 1 2
Input quantity of ingredient <press enter to stop>: > 250 ml milk
Input quantity of ingredient <press enter to stop>: > 2 tbsp cacao
Input quantity of ingredient <press enter to stop>: >
Pass the empty recipe name to exit.
Recipe name: > Hot cacao
Recipe description: > Pour the ingredients into the hot milk. Mix it up.
1) breakfast  2) brunch  3) lunch  4) supper
Enter proposed meals separated by a space: > 1 4
Input quantity of ingredient <press enter to stop>: > 250 ml milk
Input quantity of ingredient <press enter to stop>: > 2 tbsp cacao
Input quantity of ingredient <press enter to stop>: > 1 tsp sugar
Input quantity of ingredient <press enter to stop>: >
Pass the empty recipe name to exit.
Recipe name: > Fruit salad
Recipe description: > Cut strawberries and mix with other fruits. you can sprinkle everything with sugar.
1) breakfast  2) brunch  3) lunch  4) supper
Enter proposed meals separated by a space: > 3 4
Input quantity of ingredient <press enter to stop>: > 10 strawberry
Input quantity of ingredient <press enter to stop>: > 50 g black
Input quantity of ingredient <press enter to stop>: > 1 cup blue
Input quantity of ingredient <press enter to stop>: > 1 tsp sugar
Input quantity of ingredient <press enter to stop>: >
Pass the empty recipe name to exit.
Recipe name: > 
```

- Example 2:

```
> python fb.py food_blog.db --ingredients="sugar,milk" --meals="breakfast,brunch"
```

```
Recipes selected for you: Hot cacao, Milkshake
```

- Example 3:
```
> python food_blog.py food_blog.db --ingredients="sugar,milk,strawberry" --meals="brunch"
```

```
There are no such recipes in the database.
```

#### Contributing
Pull requests are welcome. For major changes please open an issue first to discuss what you would like to change.
