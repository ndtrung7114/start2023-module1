def main():
    print("You can find out the date of the month when your friend was born by asking five questions.")
    print("Each question asks whether the day is in one of the five sets of numbers.")
    print("The birthday is the sum of the first numbers in the sets where the date appears.")
    print("The program can guess your birth date. Run to see how it works")

    sets = [
        [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31],
        [2, 3, 6, 7, 10, 11, 14, 15, 18, 19, 22, 23, 26, 27, 30, 31],
        [4, 5, 6, 7, 12, 13, 14, 15, 20, 21, 22, 23, 28, 29, 30, 31],
        [8, 9, 10, 11, 12, 13, 14, 15, 24, 25, 26, 27, 28, 29, 30, 31],
        [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
    ]

    day = 0
    for i in range(5):
        answer = input(f"Is the day in set {i + 1}? (yes/no): ")
        if answer.lower() == "yes":
            day += sets[i][0]
    
    print(f"Your friend's birth date is on the {day}th of the month.")

if __name__ == "__main__":
    main()

