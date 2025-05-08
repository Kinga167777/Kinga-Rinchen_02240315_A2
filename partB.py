# Constants
MAX_POKEDEX = 1025
CARDS_PER_PAGE = 64
ROWS_PER_PAGE = 8
COLUMNS_PER_PAGE = 8

# In-memory data storage
pokemon_binder_set = set()  # Stores unique Pokedex numbers
pokemon_binder_list = []    # Maintains order of insertion

def calculate_position(index):
    """Calculate page, row, and column from insertion index."""
    page = index // CARDS_PER_PAGE + 1
    position_on_page = index % CARDS_PER_PAGE
    row = position_on_page // COLUMNS_PER_PAGE + 1
    col = position_on_page % COLUMNS_PER_PAGE + 1
    return page, row, col

def add_pokemon_card():
    """Mode 1: Add Pokémon card by Pokedex number."""
    pokedex_number = input_int("Enter Pokedex number (1-1025): ", 1, MAX_POKEDEX)
    if pokedex_number in pokemon_binder_set:
        index = pokemon_binder_list.index(pokedex_number)
        page, row, col = calculate_position(index)
        print(f"Card already exists. Page: {page}, Position: ({row},{col})")
    else:
        pokemon_binder_set.add(pokedex_number)
        pokemon_binder_list.append(pokedex_number)
        index = len(pokemon_binder_list) - 1
        page, row, col = calculate_position(index)
        print(f"Added Pokedex #{pokedex_number}. Page: {page}, Position: ({row},{col})")
        if len(pokemon_binder_list) == MAX_POKEDEX:
            print("You have caught them all!!")

def reset_binder():
    """Mode 2: Reset binder with confirmation."""
    print("WARNING: This will delete all cards from the binder.")
    confirm = input("Type 'CONFIRM' to reset or 'EXIT' to cancel: ").strip().upper()
    if confirm == "CONFIRM":
        pokemon_binder_set.clear()
        pokemon_binder_list.clear()
        print("Binder reset successfully.")
    elif confirm == "EXIT":
        print("Reset cancelled.")
    else:
        print("Invalid input. Reset not performed.")

def view_placements():
    """Mode 3: View current binder status."""
    total = len(pokemon_binder_list)
    percent = (total / MAX_POKEDEX) * 100
    print(f"\nTotal cards in binder: {total}")
    print(f"Percentage completion: {percent:.2f}%")
    if total == 0:
        print("Binder is currently empty.")
    else:
        for idx, poke in enumerate(pokemon_binder_list):
            page, row, col = calculate_position(idx)
            print(f"Pokedex #{poke} -> Page: {page}, Position: ({row},{col})")

def exit_binder_manager():
    """Mode 4: End session."""
    print("Exiting Pokemon Card Binder Manager. Goodbye!")

def pokemon_card_binder_main():
    """Main loop for the binder manager."""
    print("Welcome to Pokemon Card Binder Manager!")
    while True:
        print("\nMain Menu:")
        print("1. Add Pokemon card")
        print("2. Reset binder")
        print("3. View current placements")
        print("4. Exit")
        choice = input_int("Enter your choice (1-4): ", 1, 4)
        if choice == 1:
            add_pokemon_card()
        elif choice == 2:
            reset_binder()
        elif choice == 3:
            view_placements()
        elif choice == 4:
            exit_binder_manager()
            break

# Use this function to get integer input safely
def input_int(prompt, min_val=None, max_val=None):
    while True:
        try:
            val = int(input(prompt))
            if min_val is not None and val < min_val:
                print(f"Value must be at least {min_val}.")
            elif max_val is not None and val > max_val:
                print(f"Value must be at most {max_val}.")
            else:
                return val
        except ValueError:
            print("Invalid input. Please enter a number.")

# To run the binder manager independently
if __name__ == "__main__":
    pokemon_card_binder_main()
