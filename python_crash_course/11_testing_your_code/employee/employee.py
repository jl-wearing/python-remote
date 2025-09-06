class Employee:
    """A simple attempt to model an Employee."""

    # Constants used by the program.
    RAISE_AMOUNT = 5_000.00

    def __init__(self, first_name: str, last_name: str, annual_salary: float) -> None:
        """
        Set the parameters of an employee.
        :param first_name: the first name of the employee
        :param last_name: the last name of the employee
        :param annual_salary: the annual salary of the employee
        """
        self.first_name = first_name.lower()
        self.last_name = last_name.lower()
        self.annual_salary = annual_salary


    def give_raise(self, amount=RAISE_AMOUNT) -> None:
        """Give an employee a raise."""
        if amount <= 0:
            return
        self.annual_salary += amount