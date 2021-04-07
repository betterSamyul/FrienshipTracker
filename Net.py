import turtle
import math

people_full = {
    'Person1' : ['Person2', 'Person4', 'Person5'],
    'Person2' : ['Person1', 'Person3', 'Person5'],
    'Person3' : ['Person1', 'Person2'],
    'Person4' : ['Person1', 'Person3', 'Person2'],
    'Person5' : ['Person1', 'Person2', 'Person3']
    # Add an infinite amount of people
}


def build(chosen):
    people = [i for i in chosen]
    locations = {}
    oogway = turtle.Pen()
    oogway.hideturtle()
    oogway.speed(0)
    oogway.up()
    oogway.goto(-300, 300)

    for p in range(round(math.sqrt(len(chosen)))):
        for index in range(round(math.sqrt(len(chosen)))):
            print(people[index], index)
            oogway.write(people[index])
            locations[people[index]] = oogway.position()
            oogway.goto(oogway.position() + (600 / math.sqrt(len(chosen)), 0))

        for index in range(round(math.sqrt(len(chosen)))): people.pop(0)
        oogway.goto(-300, (oogway.position()[1] - 600 / math.sqrt(len(chosen))))

    for index in range(len(people)):
        print(people[index], index)
        oogway.write(people[index])
        locations[people[index]] = oogway.position()
        oogway.goto(oogway.position() + (600 / math.sqrt(len(chosen)), 0))

    for person in chosen:
        for link in chosen[person]:
            oogway.goto(locations[person])
            oogway.down()
            oogway.goto(locations[link])
            oogway.up()

def remaining(chosen):
    print('\n', 'Remaining'.center(20, '-'))
    for person in chosen:
        if chosen[person] == []:
            print(person)

build(people_full)
remaining(people_full)
