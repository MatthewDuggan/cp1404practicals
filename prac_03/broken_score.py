"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    result = determine_result(score)
    print(result)


def determine_result(score):
    if 90 <= score <= 100:
        result = "Excellent"
    elif 50 <= score < 90:
        result = "Pass"
    elif 0 <= score < 50:
        result = "Bad"
    else:
        result = "Invalid Input"
    return result


main()
