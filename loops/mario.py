def main():
    names=["Mario","Luigi","Daisy","Yoshi"]
    names.append("Princess")
    names.extend(["Doe","terry"])
    names.insert(0,"Rich")
    names.reverse()

    # for i in range(len(names)):
    for name in names:
        invite(name)

def invite(name):
    print(f"Welcome, {name}")


main()