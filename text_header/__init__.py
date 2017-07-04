def text_header(text):
    splits = text.lstrip().rstrip().split('\n')
    
    print("\n{0}\n*".format("*" * 100))
    for split in splits:
        print("*", split)
    print("*\n{0}\n".format("*" * 100))
    
        