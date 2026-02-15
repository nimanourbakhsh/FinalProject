library = [
 ["Little Woman", "Pride and Prejudice", "Red Rising", "The Master and Margarita", "Ender's Game"],
 ["The Arabian Nights", "The Tiger and The Wolf", "The Ruin of Kings", "Sword Catcher"],
 ["Why Plato Matters Now", "The Edge of Sentience", "Facing Down the Furies"],
 ["Pride and Prejudice", "Great Expectations", "Orlando"]
]

import copy

fiction = copy.deepcopy(library[0])
fantasy = copy.deepcopy(library[1])
philosophy = copy.deepcopy(library[2])
classic = copy.deepcopy(library[3])

categories = ["Fiction", "Fantasy", "Philosophy", "Classic"]


#Actions: Call a book, Call a category, Add to category, Remove from Category, find a book, book not found, call alls
print("Welcome to The Books Library\n")
while True:
    try:
        act = int(input("Here are the things you can do:\n\n1. Find Categories\n2. Choose a Book from Categories\n3. Find a Book\n4. Remove a Book from a Category\n5. Add a Book to a Category\n6. See All The Books\n\nPlease choose one: "))
        if act == 1:
            break
        elif act == 2:
            break
        elif act == 3:
            break
        elif act == 4:
            break
        elif act == 5:
            break
        elif act == 6:
            break
        else:
            print("Please choose a task from 1 to 5!")
    except ValueError:
        print("Please choose a task by typing it's number!")
        continue


match act:
    case 1:
        print("\nHere all the categories:\n")
        print("Fiction\nFantasy\nPhilosophy\nClassic\n")
        while True:
            try:
                inp = input("To see contents of a category, type it: ")
                if inp == "Fiction":
                    catchose = 0
                    break
                elif inp == "Fantasy":
                    catchose = 1
                    break
                elif inp == "Philosophy":
                    catchose = 2
                    break
                elif inp == "Classic":
                    catchose = 3
                    break
                else:
                    print("Please choose a correct category!")
            except NameError:
                print("Please choose a correct category!")
                continue
        print(library[catchose])

    case 2:
        print("\nCategories:\n")
        print("Fiction\nFantasy\nPhilosophy\nClassic\n")
        while True:
            try:
                inp = input("Choose one from above: ")
                if inp == "Fiction":
                    inin = 0
                    break
                elif inp == "Fantasy":
                    inin = 1
                    break
                elif inp == "Philosophy":
                    inin = 2
                    break
                elif inp == "Classic":
                    inin = 3
                    break
                else:
                    print("Please choose a correct category!")
            except NameError:
                print("Please choose a correct category!")
                continue

        print(f"Here are the {inin} books:\n")
        for index, item in enumerate(library[inin], start=1):
            print(f"{index}. {item}")

        while True:
            try:
                cnt = int(input("\nNow choose the Book by typing it's number: "))
                if 0 < cnt <= len(library[inin]):
                    break
                else:
                    print("Please choose a correct number!")
            except ValueError:
                print("Please choose a correct number!")
                continue

        print("Your choice is:")
        print(library[inin][cnt - 1])

    case 3:
       while True:
           try:
               srch = input("\nTo search for a book type it's name: ")

               if fiction.count(f"{srch}") == 1:
                   print(f"{srch} is in Fiction category.")
                   break
               elif fantasy.count(srch) == 1:
                   print(f"{srch} is in Fantasy category.")
                   break
               elif philosophy.count(srch) == 1:
                   print(f"{srch} is in Philosophy category.")
                   break
               elif classic.count(srch) == 1:
                   print(f"{srch} is in Classic category.")
                   break
               else:
                   print("Book NOT Found!")
           except ValueError:
               print("Please type the book name!")

    case 4:
        print("\nCategories:\n")
        print("Fiction\nFantasy\nPhilosophy\nClassic\n")
        while True:
            try:
                inp = input("To remove a book from a category, first choose the category: ")
                if inp == "Fiction":
                    catchose = 0
                    break
                elif inp == "Fantasy":
                    catchose = 1
                    break
                elif inp == "Philosophy":
                    catchose = 2
                    break
                elif inp == "Classic":
                    catchose = 3
                    break
                else:
                    print("Please choose a correct category!")
            except NameError:
                print("Please choose a correct category!")
                continue
        print(f"Here are the {catchose} books:\n")
        for index, item in enumerate(library[catchose], start=1):
            print(f"{index}. {item}")

        while True:
            try:
                cnt = int(input("\nNow choose the Book to remove by typing it's number: "))
                if 0 < cnt <= len(library[catchose]):
                    break
                else:
                    print("Please choose a correct number!")
            except ValueError:
                print("Please choose a correct number!")
                continue

        library[catchose].pop(cnt-1)
        print("\nDONE\n")
        for index, item in enumerate(library[catchose], start=1):
            print(f"{index}. {item}")

    case 5:
        print("\nCategories:\n")
        print("Fiction\nFantasy\nPhilosophy\nClassic\n")
        while True:
            try:
                inp = input("To add a book to a category, first choose the category: ")
                if inp == "Fiction":
                    catchose = 0
                    break
                elif inp == "Fantasy":
                    catchose = 1
                    break
                elif inp == "Philosophy":
                    catchose = 2
                    break
                elif inp == "Classic":
                    catchose = 3
                    break
                else:
                    print("Please choose a correct category!")
            except NameError:
                print("Please choose a correct category!")
                continue

        new_book = input(f"Type the book name to add to {inp} books:\n")
        library[catchose].append(new_book)
        print("\nDONE\n")
        for index, item in enumerate(library[catchose], start=1):
            print(f"{index}. {item}")

    case 6:
        print("\nHere are all the books:\n")
        for cater in range(len(categories)):
            print(f"{cater+1}. {categories[cater]}: {library[cater]}")