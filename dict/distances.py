distances = {
    "Voyager 1":163,
    "Voyager 2":136,
    "Pioneer 10":80,
    "New":58
}

def main():
    for name in distances.keys():
        print(name)
        # print(name,distances.get(name,"N/A"),sep=" : ")
    for values in distances.values():
        print(values)

main()