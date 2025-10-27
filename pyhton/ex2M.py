def count_words(text):
    text = text.lower()
    words = text.split()
    d = {}
    for word in words:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    
    return d

text = "AI is the future. The future is now"
res=count_words(text)
print(res)