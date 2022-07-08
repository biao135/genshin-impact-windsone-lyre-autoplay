file = open("Senbonzakura.txt", "r")
content = list(file.readline())
file.close()
for i in range (1, len(content)):
    if content[i-1] != ' ' and content[i-1] != '.' and content[i] == ' ':
        content.insert(i, '.')
        i+=1
file = open("Senbonzakura.txt", "w")
file.write("".join(content))
file.close()
