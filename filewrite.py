with open("journal.txt", "a") as journal:
    while True:
        text = input("Enter a journal entry (press q to quit): ")
        if text == "q":
            break
        journal.write(text+"\n")