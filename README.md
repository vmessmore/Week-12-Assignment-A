#Incremental Build Model
#Tori Messmore
#CSCI 102-Section C
#Week 12-Part A

The PrintOutput function was copied and pasted directly from the Week 10 lab.

The LoadFile function reads in each line of the given file separately and appends it to a list of lines, since this was the most efficient way I could think of to do this.

The UpdateString function loops through the given string and adds each character to a new string until the index is equal to the number input into the fucntion, at which point the given change string is added to the new string instead. The entire new string is then output. I chose to do this in this way because it makes the program more efficient and it is relatively readable.

The FindWordCount function uses the built in list.count() function to determine the number of times the input string appears in the input list. This is the easiest and quickest way I could think of.

The ScoreFinder function was probably my most complex (still not very) since it introduced a boolean to keep track of whether or not a name was found in the list of players. If the name did exist in the list of players, the players name and correspoing score were reported, but if the boolean remained false (the input name was not one of the players), the output was "player not found".

The Union function involved two separate for loops: one to loop the first input list, and one to loop the second. Each loops did the same thing, however, taking each element of the list, checking to see if the element was already present in the new output list, and adding the element to the new list if it was not there already. This allows the program to avoid duplicate elements both from the same input list and from different input lists without extra lines of code.

The Intersection function simply loops through one list, seeing if the current element exists in the second list, and adding it to a new output list if it does (ignoring it if not). I did this because it seemed like the simplest solution in the least amount of lines.

The NotIn function does the exact opposite of the Intersection function, in fact, I copy-pasted the Intersection function and added "not" in the if statement, so that the element would be added to the output list if it was NOT present in the other list. I did this because I noticed how similar the logic of these two functions would be and took advantage of the efficiency that I could implement.
