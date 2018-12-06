import pandas as pd

f2 = open('hindi_parse/2.txt')
df = pd.read_csv('hindi_parse/rules.csv')

i = 0
while True:
    open('hindi_parse/1.txt', 'w').close()
    f2_content = f2.readline()
    f3 = open('hindi_parse/text.txt','w')
    if f2_content == '':
        break
    f3.write(f2_content)
    f3.close()
    import os
    os.system("python hindi_parse/pipeline.py -p predict -l hin -t pos -m crf -f 'txt' -i hindi_parse/text.txt ")


    tags = []
    words = []

    with open("hindi_parse/1.txt") as file:
        for line in file:
            line = line.strip() #or some other preprocessing
            tags.append(line)
    try:
        if tags[-1] == 'SYM':
            tags.pop()
    except:
    	print "[ERROR] Rule not found"
    	f = open('hindi_parse/text1.txt','a+')
    	f.write("Rule not made" + '\n')
    	continue

    tag_str = ''
    for tag in tags:
        tag_str = tag_str + ' ' + tag
    if tag_str[0]==' ':
        tag_str = tag_str[1:]

    loc = df.loc[df['tags'] == tag_str]
    try:
    	loc,_ = str(loc['list']).split('\n')
    except ValueError:
    	print "[ERROR] Rule not found"
    	f = open('hindi_parse/text1.txt','a+')
    	f.write("Rule not made" + '\n')
    	continue

    loc = loc[5:]
    while loc[0] == ' ':
        loc = loc[1:]
    locs = loc.split(' ')


    with open("hindi_parse/text.txt") as file:
    	content = file.readline()
    	words = content.split(' ')

    isl_sent = ''

    for loc in locs:
        if words[int(loc)][-1:] == '\n':
            words[int(loc)] = words[int(loc)][:-1]

        isl_sent = isl_sent + ' ' + words[int(loc)].format('utf-8')
    f = open('hindi_parse/text1.csv','w')
    isl_sent = isl_sent[1:]
    f.write(isl_sent + '\n')
    f.close()
    i = i + 1

