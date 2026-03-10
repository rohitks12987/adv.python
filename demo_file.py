with open("poem.txt", "w") as f:
    f.write("Roses are red,\nViolets are blue,\nSugar is sweet,\nAnd you are handsome.\n")
print("--- Reading initial content ---")
with open("poem.txt", "r") as f:
    print(f.read())
print("\n--- Overwriting the file ---")
with open("poem.txt", "w") as f:
    f.write("This will overwrite the existing content of the file.")
print("\n--- Reading overwritten content ---")
with open("poem.txt", "r") as f:
    print(f.read())
