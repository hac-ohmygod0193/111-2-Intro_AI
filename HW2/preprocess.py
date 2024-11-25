import nltk
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.corpus import stopwords
from nltk.tokenize.toktok import ToktokTokenizer



def remove_stopwords(text: str) -> str:
    '''
    E.g.,
        text: 'Here is a dog.'
        preprocessed_text: 'Here dog.'
    '''
    stop_word_list = stopwords.words('english')
    tokenizer = ToktokTokenizer()
    tokens = tokenizer.tokenize(text)
    tokens = [token.strip() for token in tokens]
    filtered_tokens = [token for token in tokens if token.lower() not in stop_word_list]
    preprocessed_text = ' '.join(filtered_tokens)

    return preprocessed_text


def preprocessing_function(text: str) -> str:
    #preprocessed_text = remove_stopwords(text)
    # TO-DO 0: Other preprocessing function attemption
    # Begin your code 
    # remove punctuation
    import re
    from nltk.stem import WordNetLemmatizer
    from nltk.stem.porter import PorterStemmer
    ps=PorterStemmer()
    lm = WordNetLemmatizer()
    sentence = lm.lemmatize(text)
    #sentence = ps.stem(preprocessed_text)
    
    TAG_RE = re.compile(r'<[^>]+>')
    # Removing html tags
    sentence = TAG_RE.sub('', sentence)
    # Remove punctuations and numbers
    sentence = re.sub('[^a-zA-Z]', ' ', sentence)
    # Removing multiple spaces
    sentence = re.sub(r'\s+', ' ', sentence)
    #print(sentence)
    return sentence

preprocessing_function("Robert DeNiro plays the most unbelievably intelligent illiterate of all time.")