#######################
# Sangay Penjor
# 1. Electrical
# 02230075
########################
# REFERENCES
# @DQ-Logo
# @Blackbox.ai
########################
# SOLUTION
# Your Solution Score:49977
# CSF101_CAP/input_5_cap1.txt
########################## Read the input.txt file
def read_input(Input_your_file_name): # We define a fucntion "read_input"
    a = [] # We need to create an empty list to used in opponent pick
    with open(Input_your_file_name, 'r') as files: # For each line in the file
        for b in files: # It will use whitespace as a delimiter to split the lines into two sections.
            opponent_pick, output = b.split() # Create a tuple containing the two parts and append at the given list
            a.append((opponent_pick, output)) # Create a tuple containing the values of 'opponent_picked' and 'outcome', and append it to the given list
    return a # Return the list containing 'opponent_picked' and 'output'

# Calculating the point score in each game/round
def figureout_score(Overall_Games_Played): # it will Calculates the score based on "Overall_Games_Played"
    Points = 0 # The starting points for each round is 0
    for opponent_pick, outcome in Overall_Games_Played: # Iterate through each game in "Overall_Games_Played"  and reveal the values of 'opposition_picked' and 'outcome'
       
     #A mean opponent picked rock  
     #B mean opponent picked paper
     #C mean opponent picked scissors
        if outcome == 'X':  # X mean We need to LOSE
            if opponent_pick == 'A': 
                Points += 3 #  Scissor lose aganist Rock
            elif opponent_pick == 'B': 
                Points += 1  #  paper defeat rock
            elif opponent_pick == 'C': 
                Points += 2 #  Scissors defeat papper
        elif outcome == 'Y':  # Y mean We need to produce a DRAW
            if opponent_pick == 'A': 
                Points += 4  # Rock declares a draw with Rock.
            elif opponent_pick == 'B': 
                Points += 5  # Paper declear a draw with Paper
            elif opponent_pick == 'C': 
                Points += 6  # Scissors declear a draw with Scissors
        elif outcome == 'Z':  # Z mean We need to WIN
            if opponent_pick == 'A': 
                Points += 8  # Paper wins over Rock
            elif opponent_pick == 'B': 
                Points += 9 # Scissors wins over Paper
            elif opponent_pick == 'C': 
                Points += 7 # Rock wins over Scissor

    print(f"The final accumulation of points is:{Points}") #it  will Print out the total sum of(game played) the points from the given input file

# program is being run 
Input_your_file_name = "input_5_cap1.txt"  # The respected Index Number(last digit of index number ) for the students
figureout_score(read_input(Input_your_file_name)) #Making use of the information acquired from reading the input file, determine the score.
