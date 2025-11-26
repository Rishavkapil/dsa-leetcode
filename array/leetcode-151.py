## First lets try to reverse the nameing normally


# name = " hello world "
name = " a good   example "
n = len(name)
print(name)
continues_space = 0
rev = ""
each_word  = "" 
for ch in name:
    if ch != ' ':
        each_word =  each_word+ ch
    else:
        if each_word:
            if rev:
                rev = " " + rev
        rev = each_word + rev
        each_word = ""
# print(each_word, len(each_word))

rev = each_word + " " + rev
print(rev)

rev = rev.strip()

print(rev)
