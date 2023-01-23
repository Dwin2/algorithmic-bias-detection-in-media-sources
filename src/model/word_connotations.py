#load up libraries (you may need to install some of these, with conda install or pip install, if not already installed)
from gensim import models
from gensim.models import Word2Vec, KeyedVectors
from itertools import combinations
from numpy import mean, std, equal
from sklearn import *
from seaborn import stripplot
import matplotlib.pyplot as plt
from pylab import rcParams
from pylab import xlim

import build_lexicon 
import word_lists 
import dimension
import semantic_svm

currentmode = Word2Vec.load('/Users/darwin.li/Downloads/modelA_ALLYEARS_500dim_10CW')
