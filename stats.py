from collections import Counter
def count_words(text):
    return len(text.split())
def count_chars(text):
    return dict(
            sorted(
        Counter(
            filter(str.isalpha , text.lower())
        ).items() , 
        key= lambda x : -x[1]
    )
    )


