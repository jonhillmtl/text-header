import pprint

def text_header(text):
    if isinstance(text, dict):
        text = pprint.pformat(text)
    else:
        text = str(text)
        
    splits = text.lstrip().rstrip().split('\n')
    
    print("\n{0}\n*".format("*" * 100))
    for split in splits:
        print("*", split)
    print("*\n{0}\n".format("*" * 100))
    
        