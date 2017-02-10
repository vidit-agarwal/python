f = open("duplicate_file.txt", 'r').readlines()
f_set = set(f)
clean = open("clean_file.txt", "w")
for line in f_set :
    clean.write(line)
