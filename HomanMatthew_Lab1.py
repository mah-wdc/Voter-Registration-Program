# Matthew Homan
# 5/20/2023
# Week 1 - Lab 1
# SDEV 300 6380
# This program collects information from a user for voter registration.

"""Main which contains voter registration logic"""


def main():
    """
    This is a docstring that describes main.

    The user will be prompted for information.
    The information will be validated and the user
    prompted to continue or not. Once all fields
    have been entered and validated, it will
    print all the collected information.

    """

    # Print the welcome statement
    print("\nWelcome to the Python Voter Registration Application.")

    # Call continue_answer
    continue_answer = registration_continue()

    while continue_answer in ["yes", "yes."]:

        # Call get_user_first_name
        first_name = str()
        first_name = get_user_first_name()

        # Call continue_answer
        continue_answer = registration_continue()
        if continue_answer in ["no", "no."]:
            print("Thank you. Good bye.")
            break

        # Call get_user_last_name
        last_name = str()
        last_name = get_user_last_name()

        # Call continue_answer
        continue_answer = registration_continue()
        if continue_answer in ["no", "no."]:
            print("Thank you. Good bye.")
            break

        # Call voter_age
        age = validate_voter_age_is_number()

        # If statement to break for user under 18
        if age < 18:
            print("You are ineligible to register until you are 18. Good bye.\n")
            break

        # Call continue_answer
        continue_answer = registration_continue()
        if continue_answer in ["no", "no."]:
            print("Thank you. Good bye.")
            break

        # Call validate_citizenship
        citizen_status = validate_citizenship()
        # If user not a U.S. citizen, break
        if citizen_status not in ["yes", "yes."]:
            print("You must be a U.S. citizen to vote. Good bye.\n")
            break

        # Call continue_answer
        continue_answer = registration_continue()
        if continue_answer in ["no", "no."]:
            print("Thank you. Good bye.")
            break

        # Call voter_state
        state = voter_state()

        # Call continue_answer
        continue_answer = registration_continue()
        if continue_answer in ["no", "no."]:
            print("Thank you. Good bye.")
            break

        # Call voter_zipcode
        zip_number = voter_zipcode()

        # Print results
        print("Thanks for registering to vote. Here is the information we received:\n")
        print("Name (first last): ", first_name, last_name)
        print("Age: ", age)
        print("U.S. Citizen: Yes")
        print("State: ", state)
        print("Zipcode: ", zip_number)
        print("Thanks for trying the Voter Registration Application. "
              "Your voter registration card should be shipped within 3 weeks.\n")
        break


def get_user_first_name():
    """
        This is a docstring that describes first_name.

        This prompts a user for their first name and checks it against
        the allowed values. It then returns a valid age to main.

    """
    first_name = str("xxxx")

    # While loop to allow logic to check for valid response
    while first_name == "xxxx":

        flag1 = bool(False)
        flag2 = bool(False)

        # Prompt user for first name
        print("What is your first name?")
        first_name = str(input())

        # For loop to check the string for numbers
        for char in first_name:
            if char.isdigit():
                flag1 = bool(True)

        # Call isspace to check if the string is only spaces
        flag2 = first_name.isspace()

        # If statement to check for valid response
        if len(first_name) == 0 or flag1 or flag2:
            print("Invalid name. Name can not be blank or have numbers.")
            first_name = "xxxx"

    return first_name


def get_user_last_name():
    """
        This is a docstring that describes last_name.

        This prompts a user for their last name and checks it against
        the allowed values. It then returns a valid last name to main.

    """

    last_name = str("xxxx")

    # While loop to allow logic to check for valid response
    while last_name == "xxxx":

        flag1 = bool(False)
        flag2 = bool(False)

        # Prompt user for last name
        print("What is your last name?")
        last_name = str(input())

        # For loop to check the string for numbers
        for char in last_name:
            if char.isdigit():
                flag1 = bool(True)

        # Call isspace to check if the string is only spaces
        flag2 = last_name.isspace()

        # If statement to check for valid response
        if len(last_name) == 0 or flag1 or flag2:
            print("Invalid name. Name can not be blank or have numbers.")
            last_name = "xxxx"

    return last_name


def registration_continue():
    """
        This is a docstring that describes registration_continue.

        This prompts the user to continue or not with registering.
        It returns the answer to main.

    """

    continue_answer = str("xxxx")

    # While loop to allow logic to check for valid response
    while continue_answer == "xxxx":

        print("Do you want to continue with Voter Registration? (Yes/No)")
        continue_answer = str(input())
        continue_answer = continue_answer.lower()

        # If statement to check for valid response
        if continue_answer not in ["yes", "yes.", "no", "no."]:
            print("Invalid answer.  Please answer Yes or No")
            continue_answer = str("xxxx")

    return continue_answer


def validate_voter_age_is_number():
    """
        This is a docstring that describes validate_voter_age_is_number.

        This prompts a user for their age and checks it against
        the allowed values. It then returns a valid age to main.

    """

    flag1 = bool(False)
    flag2 = bool(False)
    flag3 = bool(True)
    num_age = int(0)
    str_age = str("x")

    # While loop to allow logic to check for valid response
    while str_age == "x":

        print("What is your age?")
        str_age = str(input())

        flag1 = str_age.isnumeric()
        flag2 = str_age.isspace()

        # If statement to check for valid response
        if not flag1 or flag2 or len(str_age) == 0:
            print("Invalid age.")
            str_age = "x"
        elif flag1:
            num_age = int(str_age)
            if num_age < 0 or num_age > 120:
                print("Invalid age")
                flag3 = False
                str_age = "x"
        elif flag3:
            num_age = int(str_age)
            print("num_age is", num_age, "and str_age is", str_age)
            break

    return num_age


def validate_citizenship():
    """
        This is a docstring that describes validate_citizenship.

        This prompts a user for their U.S.citizenship status
        and checks it against the allowed values. It then
        returns a yes or no to main.

    """

    flag1 = bool(False)
    citizen_status = str()

    while not flag1:

        # Prompt user for U.S. citizenship status
        print("Are you a U.S. citizen? (Yes/No)")
        citizen_status = str(input())
        citizen_status.lower()

        # If statement to check for valid response
        if citizen_status not in ["yes", "yes.", "no", "no."]:
            print("Invalid entry")
        else:
            break

    return citizen_status

def voter_state():
    """
        This is a docstring that describes voter_state.

        This prompts a user for their state and checks it against
        the allowed values. It then returns a valid state to main.

    """

    state = "AA"

    # While loop to allow logic to check for valid response
    while state not in ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "DC",
                        "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY",
                        "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT",
                        "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH",
                        "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT",
                        "VT", "VA", "WA", "WV", "WI", "WY"]:
        print("What state do you live in? (Ex. NY)")
        state = str(input())
        state = state.upper()
        # If statement to check for valid response
        if state not in ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "DC",
                        "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY",
                        "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT",
                        "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH",
                        "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT",
                        "VT", "VA", "WA", "WV", "WI", "WY"]:
            print("Invalid state. State must be in its official abbreviation.\n"
                  "For example, New York would be \'NY\'.")

    return state


def voter_zipcode():
    """
        This is a docstring that describes voter_zipcode.

        This prompts a user for their zipcode and checks it against
        the allowed values. It then returns a valid zipcode to main.

    """

    zip_number = str("xxxxx")

    # While loop to allow logic to check for valid response
    while zip_number == "xxxxx":
        print("What is your zipcode?")
        zip_number = str(input())

        # If statement to check for valid response
        if zip_number.isnumeric() and len(zip_number) == 5:
            break

        print("Invalid zipcode. Zipcode must be 5 digits.")

        # Reassign value to zip_number to continue the loop
        zip_number = "xxxxx"

    return zip_number


# Runs the main
main()
