emoticon="v:v"

def main():
    global emoticon
    say("Is anyone there?")
    emoticon = ":D"
    say("Oh, hi there")

def say(phrase):
    print(phrase,emoticon)

main()