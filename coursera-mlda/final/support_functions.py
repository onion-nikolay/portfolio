__author__ = 'onion_bass'


from sklearn.pipeline import Pipeline
import string


def text_classifier(vectorizer, classifier):
    return Pipeline([("vectorizer", vectorizer),
                     ("classifier", classifier)])


def preProcessing(input_string, lowercase=True, remove_reductions=True,
                  glue_not=False, remove_punctuation=True,
                  remove_stopwords=False, transform_numbers=True):
    """
    This preprocessing was mae for English texts just to try what can be
    useful for basic sentiment analysis. Experiments showed, that 'not'
    should not be glued with the next words, and stopwords shouldn't be
    removed."""
    _string = input_string.encode('utf-8')

# Step 1. Lowercase.
    if lowercase:
        _string = _string.lower()

# Step 2. Remove reductions ("n't", "'ve", etc.).
    reductions = {"n't": " not", "n 't": " not", "'ve": " have",
                  "'d": "", "'s": " is", "'m": " am",
                  "ain't": "have not", "...": " _ELLIPSIS",
                  "!": " _EXCLAMATION", "dont": "do not", "'re": " are",
                  "?": " _QUESTION"}
    if remove_reductions:
        for word in reductions:
            _string = _string.replace(word, reductions[word])

# Step 3. Glue "not" with the next words ("not word" turns into "not_word").
    if glue_not:
        _string = _string.replace("not ", "not_")

# Step 4. Remove punctuation (but not "_", we need it).
    if remove_punctuation:
        _string = _string.translate(None,
                                    string.punctuation.translate(None, "_"))

# Step 5. Remove stopwords.
    if remove_stopwords:
        pronouns = ['i', 'me', 'my', 'myself', 'you', 'your', 'yourself',
                    'yourselves', 'we', 'us', 'our', 'ourselves',
                    'he', 'him', 'his', 'himself', 'she', 'her', 'hers',
                    'herself', 'it', 'its', 'itself', 'they', 'them',
                    'their', 'themselves', 'ours', 'theirs', 'this',
                    'that', 'these', 'those', 'who', 'what', 'which',
                    'whose', 'whoever', 'whatever', 'whichever', 'some',
                    'something', 'somebody', 'someone', 'any',
                    'anything', 'anybody', 'anyone']

        auxiliary = ['be', 'am', 'is', 'are', 'was', 'were', 'been',
                     'will', 'have', 'has', 'had', 'do', 'does', 'did',
                     'done', 'should', 'might', 'must', 'would', 'can',
                     'could']

        prepositions = ['with', 'at', 'from', 'into', 'during', 'until',
                        'among', 'throughout', 'towards', 'upon',
                        'of', 'to', 'in', 'for', 'on', 'by', 'about',
                        'through', 'over', 'before', 'between', 'after',
                        'since', 'without', 'under', 'within', 'along',
                        'across', 'behind', 'beyond', 'except',
                        'but', 'up', 'out', 'around', 'down', 'off',
                        'above', 'near']

        articles = ['a', 'an', 'the']

        conjunctions = ['and', 'but', 'that', 'but', 'or', 'as',
                        'if', 'when', 'than', 'because', 'while',
                        'where', 'after', 'so', 'though', 'since',
                        'until', 'whether', 'before', 'although',
                        'once', 'unless']

        stopwords = pronouns+auxiliary+prepositions+articles+conjunctions
        for word in stopwords:
            _word = " "+word+" "
            _string = _string.replace(_word, " ")

    words = _string.split()

# Step 6. Transform numbers into _NUMBER label.
    if transform_numbers:
        for index, element in enumerate(words):
            if element.isdigit():
                words[index] = "_NUMBER"

    output_string = " ".join(words)
    return output_string
