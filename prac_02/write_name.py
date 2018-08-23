OUTPUT_FILE = "name_output"
out_file = open(OUTPUT_FILE,'w')
name = input("Enter your name:")
print(name, file=out_file)
out_file.close()
