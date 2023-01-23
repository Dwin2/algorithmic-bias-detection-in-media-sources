totalArticles = 100
articles, neg_words, pos_words = [], [], []
keywords = {
    'South Asian' : [[], []],
    'Chinese' : [[], []],
    'Black' : [[], []],
    'Filipino' : [[], []],
    'Arab' : [[], []],
    'Latin American' : [[], []],
    'Southeast Asian' : [[], []],
    'West Asian' : [[], []],
    'Korean and Japanese' : [[], []],
    'Indigenous': [[], []],
    'White' : [[], []],
}

for i in range(1, totalArticles+1):
    file = "./src/model/articles/article" + str(i) + ".txt"
    with open(file, "r") as f:
        articles.append(list(map(str.strip, f.readlines(), )))

with open("../src/model/adjectives/negative_words.txt", "r") as f:
    neg_words = list(map(str.strip, f.readlines(), ))

with open("./src/model/adjectives/positive_words.txt", "r") as f:
    pos_words = list(map(str.strip, f.readlines(), ))

cnt = 1
for article in articles:
    for line in article:
        for keyword in keywords:
            if keyword not in line: continue
            for word in neg_words:
                if word not in line: continue
                keywords[keyword][0].append(word)
            for word in pos_words:
                if word not in line: continue
                keywords[keyword][1].append(word)
    print(cnt)
    cnt += 1

for keyword in keywords:
    print(keyword, len(keywords[keyword][0]), len(keywords[keyword][1]))
