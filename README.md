I first considered the project requirement and what I would need. I considered various solutions.

1. Placing the data into a database then using that to display the data.
2. Using Python and pandas or dataframes to organize the data.
3. Using Python but manually print the data into a table.

I was really unsure what was wanted, so considering the prompt stated that they are looking for knowledge of data structures, loops, and logic, I decided to go with option 3. This option I felt would best show these concepts.

Then it was on to the code. 

First, I made a demo JSON file and python file. The contents of the current JSON file are not that important and the subsequent code would work with more or less data points. But I still created one to use for demos and sample.

My first step was to get the JSON data and place the team names into a teams variable. I then used this to display the team names which will be the opponents in the header.

It looks like this: 
![alt text](https://github.com/ByeolBaram/sports_reference_table/blob/main/pictures/header.png)

Next, I looped through each team to place their records in their corresponding row.

First, I only wrote the teams names to check to make sure that the teams were properly placed in their corresponding squares.

![alt text](https://github.com/ByeolBaram/sports_reference_table/blob/main/pictures/teams_opponents.png)

Then, I first did a check to see if the team in the header was the same team. Since teams don't face themselves, I placed an X in that box.

![alt text](https://github.com/ByeolBaram/sports_reference_table/blob/main/pictures/own_team_exception.png)

For all the other teams, I used the data and only checked the wins against each team. The wins column was then placed into the table.
You could alternatively check only the losses against each team, but then your chart would be inverted.

After doing this, the project was basically complete. But the data was unaligned and looked like this: 
![alt text](https://github.com/ByeolBaram/sports_reference_table/blob/main/pictures/results_unaligned.png)

The reasoning for this was I manually added spaces, but this would only work if everything was the exact same amount of characters.

![alt text](https://github.com/ByeolBaram/sports_reference_table/blob/main/pictures/unaligned_data_reasoning.png)

To fix this, I changed to using ljust of string manipulation. This would ensure that everything would align correctly. 
I didn't need to, but I went back and added ljust to other previous lines to standardize and make the code more consistent.

Now, the final result looks like this:

![alt text](https://github.com/ByeolBaram/sports_reference_table/blob/main/pictures/final_result.png)
