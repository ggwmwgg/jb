## Easy Rider Bus Company (from JetBrains Academy)

#### Description 
Program to work with data in JSON format, creating lists, iterators, dictionaries, itertools library, and re library.

#### Technologies used:
- *Python*

#### Usage 
```
python easyrider.py
```
### Implementation:
(The greater-than symbol followed by a space (```> ```) in example represents the user input. It's not part of the input.)

- Check that the types of variables match and all the required fields are filled.
- Check if the syntax is correct (using "re" library).
- Make sure that the information about the bus lines and the number of stops is correct.
- Find all departure stations, final stops, and transfer stops to fill in the missing specifications.
- Make sure that the stops follow each other and their estimated arrival times make sense.
- Check that there are no wrongly marked on-demand stops.
	- The string containing the data in JSON format is passed to standard input.
	- Check that all the departure points, final stops, and transfer stations are not "On-demand".
	- Display the unique names of the stops containing this type of issue. Sort them in ascending order.
	- If everything is fine, print ```OK```.
- Example:
	Input 1:
	```
	[
		{
			"bus_id": 128,
			"stop_id": 1,
			"stop_name": "Prospekt Avenue",
			"next_stop": 3,
			"stop_type": "S",
			"a_time": "08:12"
		},
		{
			"bus_id": 128,
			"stop_id": 3,
			"stop_name": "Elm Street",
			"next_stop": 5,
			"stop_type": "O",
			"a_time": "08:19"
		},
		{
			"bus_id": 128,
			"stop_id": 5,
			"stop_name": "Fifth Avenue",
			"next_stop": 7,
			"stop_type": "O",
			"a_time": "08:25"
		},
		{
			"bus_id": 128,
			"stop_id": 7,
			"stop_name": "Sesame Street",
			"next_stop": 0,
			"stop_type": "F",
			"a_time": "08:37"
		},
		{
			"bus_id": 256,
			"stop_id": 2,
			"stop_name": "Pilotow Street",
			"next_stop": 3,
			"stop_type": "S",
			"a_time": "09:20"
		},
		{
			"bus_id": 256,
			"stop_id": 3,
			"stop_name": "Elm Street",
			"next_stop": 6,
			"stop_type": "",
			"a_time": "09:45"
		},
		{
			"bus_id": 256,
			"stop_id": 6,
			"stop_name": "Sunset Boulevard",
			"next_stop": 7,
			"stop_type": "O",
			"a_time": "09:59"
		},
		{
			"bus_id": 256,
			"stop_id": 7,
			"stop_name": "Sesame Street",
			"next_stop": 0,
			"stop_type": "F",
			"a_time": "10:12"
		},
		{
			"bus_id": 512,
			"stop_id": 4,
			"stop_name": "Bourbon Street",
			"next_stop": 6,
			"stop_type": "S",
			"a_time": "08:13"
		},
		{
			"bus_id": 512,
			"stop_id": 6,
			"stop_name": "Sunset Boulevard",
			"next_stop": 0,
			"stop_type": "F",
			"a_time": "08:16"
		}
	]
	```
	Output 1:
	```
	On demand stops test:
	Wrong stop type: ['Elm Street', 'Sunset Boulevard']
	```
	
	
	Input 2:
	```
	[
		{
			"bus_id": 512,
			"stop_id": 4,
			"stop_name": "Bourbon Street",
			"next_stop": 6,
			"stop_type": "S",
			"a_time": "08:13"
		},
		{
			"bus_id": 512,
			"stop_id": 6,
			"stop_name": "Sunset Boulevard",
			"next_stop": 0,
			"stop_type": "F",
			"a_time": "08:16"
		}
	]
	```
	Output 2:
	```
	On demand stops test:
	OK
	```
	
#### Contributing

Pull requests are welcome. For major changes please open an issue first to discuss what you would like to change.