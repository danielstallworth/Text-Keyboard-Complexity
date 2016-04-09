
""" Enter some text, get out the score for the complexity of typing the text on a US keyboard. 
	Solution:
		Score is based on location on keyboard -> top row: 2, numbers: 3, middle(except g,h which are 2): 1, bottom: 2, space: 0
		"chicken" score of 2+2+2+2+1+2+2=13
		"hugging" score of 2+2+2+2+2+2+2=14
		"asdf" score of 4
	First thought:
		Split keyboard into 2 halves, calc distance between the adjacent letters using graphs with weights for each letter in each half. 
		At first glance it would seem that the more distant adjacent letters from each other would be harder to get to, but in practice they take about the same amount of time to think of where they are on the keyboard and to actually move the closest finger to the location of the letter. It doesn't really matter what the adjacent letters are, but where the fingers are the last time they pressed a key and whether they have time to get back to the starting position in the middle row. The method above is both simple and probably the most accurate this endeavor is going to get.
"""

# Get the characters for each row
top_row = "qwertyuiopgh[]\\"
top_row_shift = "QWERTYUIOPGH{}|"
middle_row = "asdfjkl;'\n"
middle_row_shift = "ASDFJKL:\""
bottom_row = "zxcvbnm,./"
bottom_row_shift = "ZXCVBNM<>?"
numbers = "1234567890-=`"
numbers_shift = "~!@#$%^&*()_+"

# Read in passage from a file and 
# Get a score for the file by iterating the count through each letter

final_count = 0
f = open("sample.txt")
for line in f:
	for char in line:
		if char in top_row:
			final_count = final_count + 2
		elif char in top_row_shift:
			final_count = final_count + 3
		elif char in middle_row:
			final_count = final_count + 1
		elif char in middle_row_shift:
			final_count = final_count + 2
		elif char in bottom_row:
			final_count = final_count + 2
		elif char in bottom_row_shift:
			final_count = final_count + 3
		elif char in numbers:
			final_count = final_count + 3
		elif char in numbers_shift:
			final_count = final_count + 4


print "Complexity is: ", final_count





