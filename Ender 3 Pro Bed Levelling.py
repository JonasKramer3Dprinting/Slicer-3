def travel(x, y, z, speed):
    string = "G0 X" + str(x) + " Y" + str(y) + " Z" + str(z) + " F" + str(speed) + "\n"
    return string

g_code = ""
for a in range(0, int(input("Wiederholungen: ")), 1):
    g_code = g_code + travel(30, 30, 0, 600) + travel(200, 30, 0, 600) + travel(200, 200, 0, 600) + travel(30, 200, 0, 600)

name = input("Name: ")
with open(name + ".gcode", "w") as file:
    file.write(g_code)
