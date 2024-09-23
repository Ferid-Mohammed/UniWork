# The Head of Computing at the University of Poppleton is tasked with dividing a
# group of students into lab groups. A lab group is 24 students, since this is the
# number of PCs in a lab. Write a program that calculates how many groups are
# needed for the following number of students: 113, 175, 12. Display how many full
# groups there will be, and how many students will be in the smaller "left over"
# group

Day1 = 113
Day2 = 175
Day3 = 12
Limit = 24

print('There are', Day1//Limit, 'full groups and', Day1 % Limit, 'students left over')
print('There are', Day2//Limit, 'full groups and', Day2 % Limit, 'students left over')
print('There are', Day3//Limit, 'full groups and', Day3 % Limit, 'students left over')
