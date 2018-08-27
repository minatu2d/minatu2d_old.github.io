class Fool:
    def __init__(self, a, b):
        print("Constructor")
    def __str__(self):
        return "2"

f1 = Fool(1,2)
print(" This is :{0:02d}".format(f1))
