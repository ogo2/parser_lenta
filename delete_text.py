def text(text):
    p = list(text)

    i = 0
    while True:
        try:
            if p[i] == ':':
                p.pop(i)
                p.pop(i)
                return ''.join(p)
            else:
                p.pop(i)
        except Exception:
            return text
        
