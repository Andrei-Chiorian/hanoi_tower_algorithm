NUMBER_OF_DISKS = 3
number_of_moves = 2 ** NUMBER_OF_DISKS - 1
rods = {
    'A': list(range(NUMBER_OF_DISKS, 0, -1)),
    'B': [],
    'C': []
}


def make_allowed_move(rod1, rod2):
    # we're going to try to take the top disk from rod1 and move it to rod2
    # this is only allowed if either rod2 is empty, or the top disk
    # of rod1 is smaller than the top disk of rod2
    forward = False
    if not rods[rod2]:
        # rod2 is empty, so we can move the disk from rod1 to rod2
        forward = True
    elif rods[rod1] and rods[rod1][-1] < rods[rod2][-1]:
        # the top disk of rod1 is smaller than the top disk of rod2
        # so we can move the top disk of rod1 to rod2
        forward = True
    if forward:
        # we are moving the top disk of rod1 to rod2
        print(f'Moving disk {rods[rod1][-1]} from {rod1} to {rod2}')
        # remove the top disk from rod1 and add it to rod2
        rods[rod2].append(rods[rod1].pop())
    else:
        # we are moving the top disk of rod2 to rod1
        print(f'Moving disk {rods[rod2][-1]} from {rod2} to {rod1}')
        # remove the top disk from rod2 and add it to rod1
        rods[rod1].append(rods[rod2].pop())

    # display our progress
    print(rods, '\n')


def move(n, source, auxiliary, target):
    # display starting configuration
    print(rods, '\n')
    for i in range(number_of_moves):
        remainder = (i + 1) % 3
        # if remainder is 1, then we are in the first third of the moves
        if remainder == 1:
            # If n is odd, then the first move is allowed between source and target
            if n % 2 != 0:
                print(f'Move {i + 1} allowed between {source} and {target}')
                make_allowed_move(source, target)
            # if n is even, then the first move is allowed between source and auxiliary
            else:
                print(f'Move {i + 1} allowed between {source} and {auxiliary}')
                make_allowed_move(source, auxiliary)
        # if remainder is 2, then we are in the second third of the moves
        elif remainder == 2:
            # If n is odd, then the second move is allowed between source and auxiliary
            if n % 2 != 0:
                print(f'Move {i + 1} allowed between {source} and {auxiliary}')
                make_allowed_move(source, auxiliary)
            # if n is even, then the second move is allowed between source and target
            else:
                print(f'Move {i + 1} allowed between {source} and {target}')
                make_allowed_move(source, target)
        # if remainder is 0, then we are in the third third of the moves
        elif remainder == 0:
            # the third move is always allowed between auxiliary and target
            print(f'Move {i + 1} allowed between {auxiliary} and {target}')
            make_allowed_move(auxiliary, target)


# initiate call from source A to target C with auxiliary B
move(NUMBER_OF_DISKS, 'A', 'B', 'C')
