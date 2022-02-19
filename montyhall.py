''' Monty Hall Simulation
This program is made to simulate and create data from the classic Monty Hall 
problem.
'''
import csv
import random

''' monty_simulation
Simulates one case 

player_switch: true will make the simulated player always switch their choise 
while false will make them keep. 
'''
def monty_simulation(player_switch):
    choices = [0, 1, 2]
    remove_choices = [0, 1, 2] # Which boxes the host can open

    winning_choice = random.choice(choices)
    player_choice = random.choice(choices)

    # remove the boxes that should not be opened
    remove_choices.remove(winning_choice) 
    if player_choice in remove_choices: remove_choices.remove(player_choice)

    # open a box
    choices.remove(random.choice(remove_choices))

#    print(choices)
    if player_switch:
        choices.remove(player_choice) # now there should only be one left
        player_choice = choices[0]

    if player_choice == winning_choice:
        return True
    else:
        return False

def run_simulation(iterations, player_switch):
    wins = 0
    loss = 0
    for i in range(iterations):
        if monty_simulation(player_switch):
            wins += 1
        else:
            loss += 1

    return wins, loss

if __name__ == '__main__':
    print('test case')
    wins, loss = run_simulation(100000, True)
    print('wins {}\nlosses {}\npercent {}'.format(wins, loss, wins/(wins+loss)))
    
    # Always switch
    with open('switch.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['iterations','wins','losses','percentage'])

        print('Switch 10')
        for i in range(10):
            wins, loss = run_simulation(10, True)
            csvwriter.writerow([wins+loss, wins, loss, wins/(wins+loss)])
        print('Switch 100')
        for i in range(10):
            wins, loss = run_simulation(100, True)
            csvwriter.writerow([wins+loss, wins, loss, wins/(wins+loss)])
        print('Switch 1000')
        for i in range(10):
            wins, loss = run_simulation(1000, True)
            csvwriter.writerow([wins+loss, wins, loss, wins/(wins+loss)])
        print('Switch 10000')
        for i in range(10):
            wins, loss = run_simulation(10000, True)
            csvwriter.writerow([wins+loss, wins, loss, wins/(wins+loss)])
        print('Switch 100000')
        for i in range(10):
            wins, loss = run_simulation(100000, True)
            csvwriter.writerow([wins+loss, wins, loss, wins/(wins+loss)])
        print('Switch 1,000,000')
        for i in range(10):
            wins, loss = run_simulation(1000000, True)
            csvwriter.writerow([wins+loss, wins, loss, wins/(wins+loss)])
            print(wins/(wins+loss))

    # No switching
    with open('no_switch.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['iterations','wins','losses'])

        print('Switch 10')
        for i in range(10):
            wins, loss = run_simulation(10, False)
            csvwriter.writerow([wins+loss, wins, loss, wins/(wins+loss)])
        print('Switch 100')
        for i in range(10):
            wins, loss = run_simulation(100, False)
            csvwriter.writerow([wins+loss, wins, loss, wins/(wins+loss)])
        print('Switch 1000')
        for i in range(10):
            wins, loss = run_simulation(1000, False)
            csvwriter.writerow([wins+loss, wins, loss, wins/(wins+loss)])
        print('Switch 10000')
        for i in range(10):
            wins, loss = run_simulation(10000, False)
            csvwriter.writerow([wins+loss, wins, loss, wins/(wins+loss)])
        print('Switch 100000')
        for i in range(10):
            wins, loss = run_simulation(100000, False)
            csvwriter.writerow([wins+loss, wins, loss, wins/(wins+loss)])
        print('Switch 1,000,000')
        for i in range(10):
            wins, loss = run_simulation(1000000, False)
            csvwriter.writerow([wins+loss, wins, loss, wins/(wins+loss)])
