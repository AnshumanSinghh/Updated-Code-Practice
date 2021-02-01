def password(oldpass): 
    pasw = ""
    for x in oldpass:
        if x.islower():
            nx = x.upper()
            pasw += nx
        else:
            nx = x.lower()
            pasw += nx
    return pasw

if __name__ == "__main__":
    oldpass = input()
    print(password(oldpass))
