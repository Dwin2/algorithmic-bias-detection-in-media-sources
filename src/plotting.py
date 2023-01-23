import matplotlib.pyplot as plt
import numpy as np
from detection import keywords

X, neg, pos = [], [], []
for keyword in keywords:
    if len(keywords[keyword][0]) > 0 or len(keywords[keyword][1]) > 0:
        neg.append(len(keywords[keyword][0]))
        pos.append(len(keywords[keyword][1]))
        X.append(keyword)

X_axis = np.arange(len(X))
print(neg, pos)
plt.bar(X_axis - 0.2, pos, 0.4, label = 'Positive Words')
plt.bar(X_axis + 0.2, neg, 0.4, label = 'Negative Words')
  
plt.xticks(X_axis, X)
plt.xlabel("Groups")
plt.ylabel("Number of Words")
plt.title("Classifying Word Connotations Per Group")
plt.legend()
plt.show()