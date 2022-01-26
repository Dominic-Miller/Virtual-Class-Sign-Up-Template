#Lists which hold the names of everyone in each class.
Algebra1 = ['Scott Guera', 'Ivan Odonell', 'Miles Nash', 'Xander Murray', 'Bella Mcneil', 'Cameron Larson', 'Heidy Chung']
Course1 = 'Algebra 1'

Algebra2 = ['Diana Mcclain', 'Sergio Mason', 'Thalia Munoz', 'Shane Hester', 'Jayda Sawyer', 'Sanai Lynch']
Course2 = 'Algebra 2'

PreCalc = ['Mayah Yoder', 'Rudy Bowman', 'Sadie Nash', 'Jacob Stanton', 'Evie Mata']
Course3 = 'Pre Calculus'

Calculus = ['Jarrett Harris', 'Aiden Cardenas', 'Bryant Valencia', 'Mario Avery', 'Aydin Hickman', 'Alfred Gates', 'Tyler Brewer', 'Serena Hayden', 'Amber Cherry']
Course4 = 'Calculus'

Statistics = ['Makenna Cline', 'Anna Barrera', 'Sofia Huang', 'Ana Perkins', 'Rishi Bolton', 'Diamond Vincent', 'Victoria Bolton', 'Abdullah Reyes', 'Camron Cooper', 'Elle Brock', 'Adeline Murphy', 'Daniel Carter']
Course5 = 'Statistics'

Biology = ['Lena Floyd', 'Roman Campos', 'Athena Hopkins', 'Ace Rodgers', 'Philip Ballard', 'Wesley Bennett', 'Parker Fowler', 'Kyson Phillips', 'Chad Salinas',]
Course6 = 'Biology'

Chemistry = ['Nathaniel Meyer', 'Lukas Rivas', 'Eduardo Miles', 'Lea Guerrero', 'Isla Ellison', 'Chandler Yu', 'Nicole Gamble']
Course7 = 'Chemistry'

Physics = ['Justice Dalton', 'Jamari Alvarado', 'Shamar Myers', 'Pedro Roberts', 'Leia Horton', 'Jasmin Sandoval', 'Marianna Huber', 'Quincy Burton', 'Saniyah Santiago', 'Trent Zimmerman', 'Frankie Barr']
Course8 = 'Physics'

Astronomy = ['Tyrese Meza', 'Kyla Herbert', 'Marley Wilkerson', 'Juliana Bishop', 'Anaya Ward', 'Houston Gallagher', 'Dennis Levine', 'Zain Stewart', 'Krish Lozano', 'Beatrice Clay', 'Patricia Melendez', 'Ezra Tran', 'Ramiro Howe', 'Ann Fisher', 'Jean Pha,', 'Angelo Wall']
Course9 = 'Astronomy'

WorldHistory = ['Andrew Richards', 'Aimee Galvan', 'Selena Beasley', 'Jan Dunn']
Course10 = 'World History'

AmericanHistory = ['Kyra Barker', 'Trevin Lam', 'Jonas Kennedy', 'Rhianna Hanson', 'Ethan Terry', 'Hunter Cooper', 'Mary Jimenez', 'Austin Dawson', 'Quincy Kramer', 'Orlando Cherry']
Course11 = 'American History'

EuropeanHistory = ['Dylan English', 'Paula Flowers', 'Salma Dickerson', 'Eli Watson', 'Destinee Cervantes', 'Cael Woodard', 'Beau Howard', 'Hailie Hines', 'Paul Mayer', 'Akira Hartman', 'Salma Williams']
Course12 = 'European History'

Geography = ['Scarlett Gilmore', 'Kendrick Mcknight', 'Kolten Nash']
Course13 = 'Geography'

Journalism = ['Carolyn Clayton', 'Daphne Liu', 'Caroline Oconnor', 'Paris House', 'Roselyn Odom', 'Chasity Stone', 'Giovanna Chang', 'Campbell Navarro', 'Bella Lutz', 'Tia Rios', 'Erica David']
Course14 = 'Journalism'

AmericanLiterature = ['Nia Hale', 'Tyrese Vega', 'Jasmine Daugherty', 'Hugo Floyd', 'Dangelo Cook']
Course15 = 'American Literature'

Composition = ['Alaina Montes', 'Melvin Obrien', 'Maggie Brock', 'David Jarvis', 'Amirah Berry', 'Bryant Boyle', 'Chance Harris', 'Sanai Williams', 'Grace Salazar', 'Lamont Glass', 'Gordon Bass', 'Lillianna Landry']
Course16 = 'Composition'

CreativeWriting = ['Graham Bowen', 'Clark Henry', 'Rosa Harper', 'Nicole Tate', 'Freddy Olson', 'Jalen Christian']
Course17 = 'Creative Writing'

Spanish = ['Franco Barneyy', 'Ali Shaffer', 'Santio Lang', 'Carly Howe', 'Molly Sutton', 'Heaven Todd', 'Alvin Todd', 'Parker Fowler', 'Layla Shepard', 'Zachariah Jenkins']
Course18 = 'Spanish'

SignLanguage = ['Andrew Combs', 'Pheonix Howe', 'Abbigail Good', 'Leah Donovan', 'Dale Brady', 'Jesus Joseph', 'Harold Greene', 'Kylie Manning', 'Darren Fox', 'Rey Ellis', 'Emelia Wheeler', 'Shyann Holloway']
Course19 = 'Sign Language'

French = ['Skye Vincent', 'Ryleigh Savage', 'Dangelo Taylor', 'Zachariah Curtis', 'Charlie Parks', 'Tatiana Coffey', 'Geovanni Brooks', 'Micah Cherry', 'Trenton Macias', 'Dayami Orr', 'Davin Horne', 'Barbara Gentry', 'Leroy Clements', 'Bryson Sellers', 'Anderson Luna', 'Darrell Summers', 'Riya Henson', 'Jeremy Monroe', 'Meadow Gill', 'Jaylyn Gray']
Course20 = 'French'

Latin = ['Abagail Pace', 'Kaelyn Hernandez', 'Nathen Pennington', 'Issac Hartman', 'Renee Warner', 'Ricardo Cruz', 'Samson Owens', 'Dania Hart', 'Aisha Combs', 'Easton Sloan', 'Harold Barrett']
Course21 = 'Latin'

#My list before being filled, holding the courses the student chooses to fill their schedule with.
Student_Schedule = []

time = ['9:20-10:05am', '10:10-10:55am', '11:00-11:45am', '11:50-12:35pm', '12:40-1:25pm', '1:30-2:05pm']

#Asking for the students name and grade, telling them the number of classes they must sign up for.
Student_Name = input("What is your name?: ")
Student_Grade = ''
while Student_Grade == '':
  Student_Grade = input(f'\nHey {Student_Name}! What grade are you going into?: ')
  if Student_Grade == '9' or Student_Grade == '9th':
    print("\nWow 9th grade! Welcome to High School!")
    break
  elif Student_Grade == '10' or Student_Grade == '10th':
    print("\n10th grade! Last year being an underclassman!")
    break
  elif Student_Grade == '11' or Student_Grade == '11th':
    print("\n11th grade! Almost there only 2 years left!")
    break
  elif Student_Grade == '12' or Student_Grade == '12th':
    print("\n12th grade! Last year in High School!")
    break
  else:
    print('Please enter a valid grade 9th-12th.')
    Student_Grade = ''
    continue

print('\nYou must Sign up for at least 6 classes to complete your schedule.')
Continue = '?'
while Continue != '':
  Continue = input('\nPress Enter to Continue.')
  if Continue == '':
    break

#Function which tells the student who is in the class and if they can even sign up for the class, if they choose to sign up the class is added to their schedule.

def Student_Classes(choice, course):
  if len(choice) < 20:
    print(f'\nThere are {len(choice)} students currently signed up for {course}:')

    #This for loop uses iteration to display the names of each classmate on a separate line.
    for classmate in range(len(choice)): 
      print(choice[classmate])
    signup = input("\nWould you like to sign up for this class?: ")

    #This is selection which takes the users input and either adds or does not add the class to their list depending on their choice.
    if signup.upper() == "YES":
      Student_Schedule.append(course)
      print(f'\nYou have successfully signed up for {course}. You must sign up for at least {6 - len(Student_Schedule)} more classes.')
    
    elif signup.upper() == "NO":
      print(f'\nOkay, {course} has not been added to your schedule.')
  elif len(choice) >= 20:
    print("\nSorry, this class is full. Please select another course.")

  #This allows the user to read everything they just inputted before continuing.
  Continue = '?'
  while Continue != '':
    Continue = input('\nPress Enter to Continue.')
    if Continue == '':
      break


#This will take input from the user and sign them up for their desired classes.
course = 0
while len(Student_Schedule) <= 7:

  course = int(input('''
  What course would you like to sign up for?

  MATHMATICS:
  Press 1 for Algebra 1
  Press 2 for Algebra 2
  Press 3 for Pre-Calculus
  Press 4 for Calculus
  Press 5 for Statistics

  SCIENCES:
  Press 6 for Biology
  Press 7 for Chemistry
  Press 8 for Physics
  Press 9 for Astronomy

  SOCIAL STUDIES:
  Press 10 for World History
  Press 11 for American History
  Press 12 for European History
  Press 13 for Geography

  ENGLISH AND LITERATURE:
  Press 14 for Journalism
  Press 15 for American Literature
  Press 16 for Composition
  Press 17 for Creative Writing

  FOREIGN LANGUAGES:
  Press 18 for Spanish 
  Press 19 for Sign Language
  Press 20 for French
  Press 21 for Latin

  OR:
  Press 22 if you are done selecting

  Enter a number: '''))

  if course == 1:
    Student_Classes(Algebra1, Course1)

  elif course == 2:
    Student_Classes(Algebra2, Course2)

  elif course == 3:
    Student_Classes(PreCalc, Course3)

  elif course == 4:
    Student_Classes(Calculus, Course4)

  elif course == 5:
    Student_Classes(Statistics, Course5)

  elif course == 6:
    Student_Classes(Biology, Course6)

  elif course == 7:
    Student_Classes(Chemistry, Course7)

  elif course == 8:
    Student_Classes(Physics, Course8)

  elif course == 9:
    Student_Classes(Astronomy, Course9)

  elif course == 10:
    Student_Classes(WorldHistory, Course10)

  elif course == 11:
    Student_Classes(AmericanHistory, Course11)

  elif course == 12:
    Student_Classes(EuropeanHistory, Course12)

  elif course == 13:
    Student_Classes(Geography, Course13)

  elif course == 14:
    Student_Classes(Journalism, Course14)

  elif course == 15:
    Student_Classes(AmericanLiterature, Course15)

  elif course == 16:
    Student_Classes(Composition, Course16)

  elif course == 17:
    Student_Classes(CreativeWriting, Course17)

  elif course == 18:
    Student_Classes(Spanish, Course18)

  elif course == 19:
    Student_Classes(SignLanguage, Course19)

  elif course == 20:
    Student_Classes(French, Course20)

  elif course == 21:
    Student_Classes(Latin, Course21)

  elif course == 22:
    if len(Student_Schedule) < 6:
      print(f'\nYou must still sign up for at least {6 - len(Student_Schedule)} more classes.')
    else:
      break

  else:
    print("\nPlease Enter a Valid Number.")


#This will print out all of the classes you have signed up for.
print(f'\nThank you {Student_Name}! Your course schedule for {Student_Grade} grade is displayed below:\n')

x=0
y=1
for course in range(len(Student_Schedule)):
  print(f'Period {y}:')
  print(Student_Schedule[course])
  print(f'{time[x]}')
  print('\n')
  x+=1
  y+=1

