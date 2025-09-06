class User:
    """Simple attempt to model a User."""

    def __init__(self, first_name: str, last_name: str, **kwargs) -> None:
        """
        Set the instance variables of a User.
        :param first_name: the first name of the user.
        :param last_name: the last name of the user.
        :param kwargs: any additional information about the user.
        """
        self.first_name = first_name.lower()
        self.last_name = last_name.lower()
        self.user_info = kwargs
        self.login_attempts = 0


    def describe_user(self) -> None:
        """Print a summary of the user's information."""
        print(f"full name: {self.first_name.title()} {self.last_name.title()}")

        for key, value in self.user_info.items():
            print(f"{key}: {value}")


    def greet_user(self) -> None:
        """Display a greeting to the user."""
        full_name = f"{self.first_name} {self.last_name}".title()
        print(f"Hello, {full_name}")

    def increment_login_attempts(self) ->None:
        """Increment the login attempts by 1."""
        self.login_attempts += 1


    def reset_login_attempts(self) -> None:
        """Reset the login attempts counter to 0."""
        self.login_attempts = 0


    def __str__(self) -> str:
        """Return a string representation of the user."""
        all_information = f"User({self.first_name}, {self.last_name}"
        for value in self.user_info.values():
            all_information += f", {value}"
        all_information += ")"

        return all_information


class Admin(User):
    """An administrator is a special type of User with added privileges."""

    def __init__(self, first_name: str, last_name: str, **kwargs) -> None:
        """
        Initialize the instance variables of a user.
        Then set the attributes of an Admin.
        :param first_name: the first name of the admin.
        :param last_name: the last name of the admin.
        :param kwargs: additional information about the admin.
        """
        super().__init__(first_name, last_name, **kwargs)
        self.privileges = Privileges()



class Privileges:
    """Attempt to model the privileges an admin would have."""

    def __init__(self) -> None:
        """Initialize the attributes of a Privilege object."""
        self.privileges = ['can add post', 'can delete post', 'can add user'
            , 'can ban user', 'can manage accounts']


    def show_privileges(self) -> None:
        """Display the privileges of an admin."""
        print("Privileges of an administrator: ")
        for privilege in self.privileges:
            print(f"\t{privilege}")