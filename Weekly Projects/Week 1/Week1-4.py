# In a long career for Yorkshire, Geoffrey Boycott played 609 matches, batted 1014
# times, was not out 162 times, and scored 48426 runs. Write a program to calculate
# and display Boycott's batting average.
# Note: A batting average is the number of runs scored divided by the number of
# completed innings (i.e. the total times batted minus the times not out).

Played = 609
Batted = 1014
NotOut = 162
Runs = 48426

CompletedInnings = Batted - NotOut
BattingAverage = int((Runs/CompletedInnings))
print(BattingAverage)