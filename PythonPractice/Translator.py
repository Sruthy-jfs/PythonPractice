from translate import Translator
translator = Translator(to_lang='en')
try:
    with open ('translate.txt','r') as my_file:
        text1=my_file.read()
        translation=translator.translate(text1)
        with open( 'translate2.txt','w') as mytrans_file:
             mytrans_file.write(translation)
except FileNotFoundError:
    print('File not found')
