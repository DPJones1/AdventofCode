<h1> Day One </h1>
<b>Task:</b> To find the total distance between the left list and the right list, add up the distances between all of the pairs you found. In the example above, this is 2 + 1 + 0 + 1 + 2 + 5, a total distance of 11!

Your actual left and right lists contain many location IDs. What is the total distance between your lists?

<b>How did I solve this?</b>

- Figure out the ask
- Putting all the data into a csv file
- Then focus on putting into chronological order
- Then work out the differences per line

<b>Step by step: </b>

1. Put the data in a csv file
2. Use logic to create the columns and seperate the data with commas
3. Skip the first line in te csv file where I have put the column headers "next(file)"
4. Then implement logic to sort each column in order
5. Once the data is sorted, the absolute difference between each line is then implemented with a loop to to iterate through each line
6. Finally print the total sum found in differences
