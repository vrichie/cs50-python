# students=["john","joe","Ron","Draco"]



# for student in students:
    # print(student)

# for i in range(len(students)):
    # print(students[i])



# dict
# students=[
#     {"name":"Hermione","house":"Gry","age":1},
#     {"name":"Terry","house":"tech","age":None},
# ]

# for student in students:
#     print(student["name"],student["house"],student["age"],sep=', ')


def main():
    spacecraft={"name":"James"}
    spacecraft["distance"]=0.01

    print(create_report(spacecraft))

def create_report(spacecraft):
    return f"""
    ================Report==========

    Name : {spacecraft.get("name","N/A")}
    Distance : {spacecraft.get("distance","N/A")}

    ================================
    """



