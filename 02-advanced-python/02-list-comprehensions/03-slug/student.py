# Write your code here
def slug(name):
    parts = name.split()
    fname = parts[0]
    lname = parts[1:]
    return "-".join([i.lower() for i in lname + [fname]])