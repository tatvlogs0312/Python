# car game

command = ""
started = False
while True:
    command = input("> ").lower()
    if command.lower() == "start":
        if started:
            print("car is already started")
        else:
            started = True
            print("Car started...")
    elif command.lower() != "quit":
        break
    elif command.lower() == "stop":
        if not started:
            print("car is already stopped!")
        else:
            print("car stopped...")
            started = False
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    else:
        print("Sorry, I don't understand that!")

