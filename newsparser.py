#Se auto to arxeio tha kanoume parse tis selides pou kaname crawl. Xrhsimopoiuoume tis bibliothikes beatifulsoup(gia na kanoume parse tags me sygekrimeno class) kai codec gia na diavasoume ta html.

from bs4 import BeautifulSoup
import os
import codecs
from langdetect import detect #gia na sigourepsoume oti tha exoume mono ta agglika keimena

#gia ta onomata  twn telikwn arxeiwn
counter = 1

#destination twn telikwn arxeiwn
if not os.path.exists('dest'):
    os.mkdir('dest')

#for every file in news
for file in os.listdir('news'):
    #print(item)
    #ftiaxnoume to path gia na mporoume na to kanoume read
    filepath = os.path.join("news", file)
    try:
        with codecs.open(filepath, encoding='utf8') as f: #xrhsimoipei utf8 encoding
            html = f.read()#diabazoume to arxeio
            #print(html)
            textparser = BeautifulSoup(html, 'html.parser')
            #e3agoume to keimeno symfwna me merika attributes pou kathoristikan koitwntas to html
            text = textparser.find_all('p', attrs={'class': 'ssrcss-1q0x1qg-Paragraph eq5iqo00'})
            if text == []:
                text = textparser.find_all('p', attrs={'class': 'newsround-story-body__text'})
            elif text ==[]:
                text = textparser.find_all('span', attrs={'data-reactid': '.27q88ybbm8c.0.0.0.1.$paragraph-3.$link-2.0'})
            for content in text:
                final_text = content.text.strip() #afairoume ta tags
                if detect(final_text) != 'en':
                    continue            
                #print(final_text)
                filepath_write = os.path.join("dest", str(counter))
                with open(filepath_write,"a+") as w:
                    w.write(final_text)
        counter+=1
    except:
        print("error")
        continue
                   
f.close()
w.close()