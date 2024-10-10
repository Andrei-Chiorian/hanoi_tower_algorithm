NUMBER_OF_DISKS = 5
A = list(range(NUMBER_OF_DISKS, 0, -1))
B = []
C = []


def move(n, source, auxiliary, target):
    # This function moves n disks from source to target, using auxiliary as a temporary
    # repository for disks that are out of the way.
    if n <= 0:
        # If n is 0 or negative, then there are no disks to move, so we do nothing
        return

    # Move n - 1 disks from source to auxiliary, so they are out of the way
    # This is the recursive step, where we call ourselves to move
    # n - 1 disks from source to auxiliary.
    move(n - 1, source, target, auxiliary)

    # Move the nth disk from source to target
    # This is the part of the move where we actually move a disk from
    # source to target.
    target.append(source.pop())

    # Display our progress
    # We print out the state of the rods after each move
    print(A, B, C, '\n')

    # Move the n - 1 disks that we left on auxiliary onto target
    # This is the recursive step, where we call ourselves to move
    # n - 1 disks from auxiliary to target.
    move(n - 1, auxiliary, source, target)


# initiate call from source A to target C with auxiliary B
move(NUMBER_OF_DISKS, A, B, C)