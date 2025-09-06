class AnonymousSurvey:
    """Collect anonymous answers to a survey question."""

    def __init__(self, question: str) -> None:
        """Store a question and prepare to store responses."""
        self.question = question.lower()
        self.responses = []


    def show_question(self):
        """Show the survey question."""
        print(self.question)

    def store_response(self, new_response: str) -> None:
        """Store a single response to the survey."""
        self.responses.append(new_response.lower())

    def show_results(self) -> None:
        """Show all responses that have been give."""
        print("Survey results: ")
        for response in self.responses:
            print(response)


def main():
    """Mainline logic for testing the AnonymousSurvey class."""
    # Define a question and make a survey.
    question = 'What language did you first learn to speak?'
    language_survey = AnonymousSurvey(question)

    # Show the question, and store responses to the question.
    language_survey.show_question()
    print("Enter 'q' at any time to quit.\n")
    while True:
        response = input('Language: ')
        if response.lower() == 'q':
            break
        language_survey.store_response(response)

    # Show the survey results.
    print(f"\nThank you to everyone who participated in the survey!")
    language_survey.show_results()

# Call the main function.
if __name__ == '__main__':
    main()