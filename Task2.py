# Recursive function to calculate the minimal number of moves for Towers of Hanoi

def hanoi_moves(disks):
    """
    Recursively calculates the minimal number of moves required
    to solve the Towers of Hanoi for a given number of disks.
    """
    if disks == 1:
        return 1  # Base case: Only one disk needs 1 move
    else:
        # Recursive case: 2 * moves for (n-1) disks + 1 move for the largest disk
        return 2 * hanoi_moves(disks - 1) + 1

def solve_towers_of_hanoi():
    """
    Asks the user for the number of disks and prints the minimal number of moves.
    """
    disks = int(input("Enter the number of disks: "))
    if disks <= 0:
        print("Please enter a positive number of disks.")
    else:
        moves = hanoi_moves(disks)
        print(f"The minimal number of moves to solve the Towers of Hanoi with {disks} disks is: {moves}")

# Running the function to solve Towers of Hanoi
solve_towers_of_hanoi()
