def main():
    spacecraft={"name":"James"}
    # spacecraft["distance"]=0.01
    spacecraft.update({"distance":0.01,"orbit":"Sun"})

    print(create_report(spacecraft))

def create_report(spacecraft):
    return f"""
    ================Report==========

    Name : {spacecraft.get("name","N/A")}
    Distance : {spacecraft.get("distance","N/A")}
    Orbit : {spacecraft.get("orbit","N/A")}

    ================================
    """

main()