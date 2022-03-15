"""
questy.py - class style questions
"""


class Prompt:
    def __init__(self, prompt, action):
        self.Db = []
        self.prompt = prompt
        self.action = action


class Prompts:
    #Initializes dictionaries
    def __init__(self, options):
        #Parameter options is a list with format:
        #[0] - Prompt
        #[1] - Command

        self.exit = "Exit"
        self.banner = None
        self.singlepass = True
        self.lastchoice = None

        #Dictionaries for Prompts class
        self.options = {}   #question option
        self.commands = {}  #command line options

        #Exit for Prompts
        self.options[0] = Prompt(self.exit, None)
        #Exit for commands
        self.commands[self.exit.lower()] = None

        #Loop options to build Dictionaries
        for op in options:
            index = len(self.options)
            self.options[index] = Prompt(op[0], op[1])
            self.commands[op[0].lower()] = op[1]

    #setter for single or multiple pass
    def set_recurse(self, recurse):
        self.singlepass = not recurse

    #setter for banner
    def set_banner(self, banner):
        self.banner = banner

    #getter for user choice
    def get_choice(self):
        return self.lastchoice

    #question prompts
    def print_prompts(self):
        print()
        if self.banner != None:
            #alternate heading
            print(self.banner)

        #question prompts
        for key, value in self.options.items():
            print(key, '->', value.prompt)

    #menu selection and execute
    def choice(self):
        # get choice from user
        choice = input("Type your choice> ")
        # validate choice and run
        #execute selection
        try: #try converting to integer
            #convert to number
            choice = int(choice)
            if choice == 0: #exit choice, stop loop
                return True  #stop
            try:  #try as function function
                self.lastchoice = choice
                prompt = self.options[choice]
                action = prompt.action
                action()
            except:
                try:  #try as playground style
                    exec(open(action).read())
                except:
                    print(f"Bad action: {action}")
                #end function try
            #end playground try
        except ValueError: #not a number error
            print(f"Not a number: {choice}")
        except: #traps all other errors
            print(f"Invalid choice: {choice}")
        #end validation try
        return False or self.singlepass

    #command prompt and execute
    def command(self):
        #True keeps help command in loop
        while True:
            #banner
            print()
            if self.banner != None:
                print(self.banner)
            #selection
            choice = input("Type a command (h for help)> ")
            #help prints commands
            if choice == "h":
                for command in self.commands:
                    print(command)
            #exit leaves command shell
            elif choice == self.exit.lower():
                return True
            #all others try executions
            else:
                try:  # protects/traps errors from user
                    self.lastchoice = choice
                    action = self.commands[choice]
                    action()
                except:
                    try:
                        exec(open(action).read())
                    except:
                        print(f"Not a command: {choice}")
                    #end open try
                #end command try
                return False or self.singlepass
        #end while loop

    # question style
    def question(self):
        self.print_prompts()    #question options
        stop = self.choice()    #user action
        if stop:                #stop
            return
        self.question()         #continue via recursion

    #traditional menu style
    def menu(self):
        self.question()

    #shell based style
    def shell(self):
        stop = self.command()   #commnad prompt
        if stop:                #stop
            return
        self.shell()            #continue via recursion

class Question(Prompts):
    #Initializes dictionaries
    def __init__(self, banner, options):
        Prompts.__init__(self, options)
        self.set_recurse(False)
        self.set_banner(banner)

class Menu(Prompts):
    #Initializes dictionaries
    def __init__(self, banner, options):
        Prompts.__init__(self, options)
        self.set_recurse(True)
        self.set_banner(banner)
