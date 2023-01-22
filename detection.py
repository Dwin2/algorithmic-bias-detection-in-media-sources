totalArticles = 100
articles, neg_words, pos_words = [], [], []
keywords = {
    'South Asian' : [0, 0],
    'Chinese' : [0, 0],
    'Black' : [0, 0],
    'Filipino' : [0, 0],
    'Arab' : [0, 0],
    'Latin American' : [0, 0],
    'Southeast Asian' : [0, 0],
    'West Asian' : [0, 0],
    'Korean and Japanese' : [0, 0],
    'Indigenous': [0, 0],
    'White' : [0, 0],
}

for i in range(1, totalArticles+1):
    file = "./Articles/article" + str(i) + ".txt"
    with open(file, "r") as f:
        articles.append(list(map(str.strip, f.readlines(), )))

with open("./Adjectives/negative_words.txt", "r") as f:
    neg_words = list(map(str.strip, f.readlines(), ))

with open("./Adjectives/positive_words.txt", "r") as f:
    pos_words = list(map(str.strip, f.readlines(), ))

cnt = 1
for article in articles:
    for line in article:
        for keyword in keywords:
            if keyword not in line: continue
            for word in neg_words:
                if word not in line: continue
                keywords[keyword][0] += 1
            for word in pos_words:
                if word not in line: continue
                keywords[keyword][1] += 1
    print(cnt)
    cnt += 1

for keyword in keywords:
    print(keyword, keywords[keyword])
