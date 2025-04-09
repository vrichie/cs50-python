SHOWS = [
    "  Breaking Bad  ",  # Extra spaces
    "game of thrones",   # All lowercase
    "Stranger Things!",  # Special character
    "The Office",        # Proper capitalization
    "FRIENDS",           # All uppercase
    "Sherlock123",       # Contains numbers
    "  the mandalorian ",# Extra spaces and lowercase
    "Money Heist!!",     # Special characters
    "Better.Call.Saul",  # Periods instead of spaces
    "Peaky_BLINDERS"     # Underscore instead of space
]

def main():
    cleaned_shows = []
    for show in SHOWS:
        cleaned_shows.append(show.strip().title().replace("."," ").replace("_",""))
    print(' \n'.join(cleaned_shows))
main()