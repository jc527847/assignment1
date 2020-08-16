"""
Name: chenchen
Date started: 14/8/2020
"""
# Import CSV file and append them to a list. Frame work of main function done.

import csv

place_list = []

with open('places.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        print(line)
        place_list.append(line)

place_list.sort(
    key=lambda l: (l[1], l[0])
)


def main():

    print('{} places loaded from places.csv'.format(len(place_list)))
    running = True
    while running:
        # Display the menu
        running = Menu()

# Menu function responsible for displaying the menu
def Menu():
    choice_valid = False
    # Loop unitil valid choice is entered.
    while choice_valid == False:

        choice = input(  # Get input and change to lower case
            '\nMenu:\nL - List places\nA - Add new place\nM - Mark a place as visited\nQ - Quit\n>>> ').lower()
        choice_valid = Menu_Handler(choice)
    if choice == 'l':  # Selection
        place_list.sort(key=lambda l: (l[1], l[0]))
        List_Places()
        return True
    elif choice == 'a':
        Add_new_places()
        return True
    elif choice == 'm':
        Markplacevisited()
        return True
    else:
        with open('places.csv', 'w', newline='\n') as f:  # Write to csv and quit
            writer = csv.writer(f)
            for i in place_list:
                writer.writerow(i)
        print('{} places saved to places.csv\nHave a nice day :)'.format(len(place_list)))
        return False


# Menu error handling.
def Menu_Handler(choice):

    if(choice != 'l' and choice != 'a' and choice != 'm' and choice != 'q'):
        print('Invalid Menu Choice!')
        return False
    else:
        return True


# List all places.
def List_Places():
    visited = 0
    unvisited = 0
    for i in range(len(place_list)):

        if(place_list[i][-1] == 'u'):
            unvisited += 1
            print('  {}. * {} - {}  ({})'.format(i, place_list[i][0], place_list[i][1], place_list[i][2]))
        else:
            visited += 1
            print('  {}.   {} - {}  ({})'.format(i, place_list[i][0], place_list[i][1], place_list[i][2]))

    print('{} places visited, You still want to visit {} places'.format(visited, unvisited))


# Add new places function
def Add_new_places():
    # Loop to validate until correct
    invalid = True
    while invalid:
        name = input('Name: ')
        invalid = Add_new_place_handler(name)

    invalid = True
    while invalid:
        country = input('Country: ')
        invalid = Add_new_place_handler(country)

    invalid = True
    while invalid:
        priority = input('Priority: ')
        try:
            priority = int(priority)
        except:  # Exception
            print('Invalid input; enter a valid number')
            continue

        if priority == '':
            print('Priority cannot be blank')

        elif priority< 0:
            print('Priority must be >= 0')
        else:
            invalid = False
    print('{} by {} ({}) added to song list'.format(name, country, priority))
    place = [name, country, priority, 'u']
    place_list.append(place)


# Function for handling add new places input
def Add_new_place_handler(name):
    if(name == ''):
        print('Input cannot be blank')
        return True
    else:
        return False

# Function for marking a place as visited
def  Markplacevisited():
    visited = 0
    # See whether a place is visited or unvisited
    for i in place_list:
        if i[-1] == 'l':
            visited += 1
        else:
            visited -= 1
    if (visited == len(place_list)):
        print('No more places to visited!')
        return
    else:

        invalid = True
        while invalid:
            number = input('Enter the number of place to mark as visited\n>>>')
            invalid = MarkplacevisitedHandler(number)

        if (place_list[int(number)][3] == 'l'):
            print('You have already learned {}'.format(place_list[int(number)][0]))

        elif (place_list[int(number)][3] == 'u'):
            print('{} by {} learned '.format(place_list[int(number)][0], place_list[int(number)][1]))
            place_list[int(number)][3] = 'l'


# Function for handling correct output for marking a place as visited
def  MarkplacevisitedHandler(number):
    try:
        number = int(number)
    except:
        print('Invalid input; enter a valid number')
        return True
    if number < 0:
        print('Number must be >= 0')
        return True
    elif number >= len(place_list):
        print('Invalid song number')
        return True
    else:
        return False


main()  # Activate main function