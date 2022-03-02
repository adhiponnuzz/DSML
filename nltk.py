from nltk.corpus.reader import tagged
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize,word_tokenize
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
sw=set(stopwords.words('english'))
txt="Hello.I am Darsana Prasad.I am a native of Athani."
tokenized=nltk.word_tokenize(txt)
for i in tokenized:
  wordlist=word_tokenize(i)
  wordlist=[w for w in wordlist if not w in sw]
  tagged=nltk.pos_tag(wordlist)
  print(tagged)
