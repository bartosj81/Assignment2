"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45
DINING_HALL_PER_MONTH = 330

# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    """Give back what one semester costs."""
    semester = annual_cost / SEMESTERS_PER_YEAR
    return semester


def cost_per_month(annual_cost):
    """Give back what one month of the academic year costs."""
    month = annual_cost / MONTHS_PER_YEAR
    return month


def cost_per_day(annual_cost):
    """Give back what one class day costs."""
    day = annual_cost / (SEMESTERS_PER_YEAR * CLASS_DAYS_PER_SEMESTER)
    return day


def cost_per_credit(annual_cost, credits):
    """Give back what one credit costs. credits is the number taken this semester."""
    credit_cost = annual_cost / (credits * SEMESTERS_PER_YEAR)
    return credit_cost


def cost_per_class(annual_cost, credits):
    """Give back what one 50-minute CS 1430 class meeting costs."""
    class_cost = (annual_cost / (credits * SEMESTERS_PER_YEAR)) * CS1430_CREDITS / CS1430_MEETINGS_PER_SEMESTER
    return class_cost


# ---- PROGRAM ----

def main():
    # Ask for the total cost for one year here.
    # Then ask for the credits this semester.
    annual_cost = float(input("Enter the total cost for one year: "))
    credits = int(input("Enter the number of credits for this semester: "))
    

    while True:
        # Show your menu here.
        print("\nMenu:")
        print("1. Cost per semester")
        print("2. Cost per month")
        print("3. Cost per day")
        print("4. Cost per credit")
        print("5. Cost per class")
        print("Q. Quit")

        choice = input("Choose an option: ")

        if choice == "Q":
            break

        if choice == "1":
            print("{:.2f}".format(cost_per_semester(annual_cost)))
        elif choice == "2":
            print("{:.2f}".format(cost_per_month(annual_cost)))
        elif choice == "3":
            print("{:.2f}".format(cost_per_day(annual_cost)))
        elif choice == "4":
            print("{:.2f}".format(cost_per_credit(annual_cost, credits)))
        elif choice == "5":
            print("{:.2f}".format(cost_per_class(annual_cost, credits)))


# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
