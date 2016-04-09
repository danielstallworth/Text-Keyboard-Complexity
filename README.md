# Text-Keyboard-Complexity
Enter some text in a file, get out the score for the complexity of typing the text on a US keyboard.
	Solution:
		Score is based on location on keyboard -> top row: 2, numbers: 3, middle(except g,h which are 2): 1, bottom: 2, space: 0
		"chicken" score of 2+2+2+2+1+2+2=13
		"hugging" score of 2+2+2+2+2+2+2=14
		"asdf" score of 4
	First thought:
		Split keyboard into 2 halves, calc distance between the adjacent letters using graphs with weights for each letter in each half. 
		At first glance it would seem that the more distant adjacent letters from each other would be harder to get to, but in practice they take about the same amount of time to think of where they are on the keyboard and to actually move the closest finger to the location of the letter. It doesn't really matter what the adjacent letters are, but where the fingers are the last time they pressed a key and whether they have time to get back to the starting position in the middle row. The method above is both simple and probably the most accurate this endeavor is going to get.
