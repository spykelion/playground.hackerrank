def designerPdfViewer(h, word):
    letters = [
        'a','b','c','d','e',
        'f','g','h','i','j',
        'k','l','m','n','o',
        'p','q','r','s','t',
        'u','v','w','x','y','z'
    ]
    heights = []
    selected_word = []
    values = []

    for x in range(len(h)):
        heights.append({letters[x]:h[x]})
        
    for h in heights:
        for key, value in h.items():
            if key in word:
                selected_word.append({key,value})
                values.append(value)


    tallest = max(values)
    
    print(tallest," * ",len(word)," = " ,tallest*len(word))

c = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,7]
ordered = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
designerPdfViewer(c, 'zaba')