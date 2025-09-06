# Program to simulate printing designs.

def print_models(unprinted_designs):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    :param unprinted_designs: The list of unprinted designs.
    :return: The list of printed designs.
    """
    completed_models = []
    while unprinted_designs:
        # Get the design in the front of the queue.
        current_design = unprinted_designs.pop(0)

        # Output the current design being printed.
        print(f"Printing model: {current_design}")

        # Move the current design to completed designs.
        completed_models.append(current_design)

    return completed_models

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed: ")
    for model in completed_models:
        print('\t', model, sep='')

def main():
    """Mainline logic for printing models."""
    # Create a list of designs to be completed.
    unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']

    # Simulate printing each design.
    completed_models = print_models(unprinted_designs[:])

    # Show completed models.
    show_completed_models(completed_models)

# Call the main function.
if __name__ == '__main__':
    main()