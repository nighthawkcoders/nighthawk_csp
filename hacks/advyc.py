# advyc.py - adventure starter
import questy, advy

def main():
    banner = "You are on a treasure adventure... \nWhere do you want to start your journey?"

    options = [
        ["At the Beach?", advy.beach],
        ["On top of the Mountains?", advy.mountain],
        ["Navigating a lake?", advy.lake]
    ]
    q = questy.Question(banner, options)
    q.question()

if __name__ == "__main__":
    main()
