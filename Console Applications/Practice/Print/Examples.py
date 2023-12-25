class Examples:
    @staticmethod
    def ProcessExamples():
        while True:
            try:
                choice = int(input("Please select an example from 1-15: "))
                
                if choice == 1:
                    Examples.Example1()
                else:
                    print("Your choice is invalid")
                    continue
            except ValueError:
                print("Selection chosen is incorrect")
                continue
            
            while True:
                decision = input("Do you want to do another example? - Yes or No: ").upper()
                print()
                
                if decision == "YES":
                    break
                elif decision == "NO":
                    return
                else:
                    print("Your decision is invalid. Try again")
                    
    @staticmethod
    def Example1():
        print("Writes a string to the console followed by a newline escape sequence\n")