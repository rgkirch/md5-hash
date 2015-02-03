with open("byteFile", "w") as out_file:
    a = bytearray()
    a.append(0x62)
    out_file.write(a)
