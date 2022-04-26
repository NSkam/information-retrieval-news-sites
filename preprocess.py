#Se auto to arxeio kanoume preprocess ta keimena kai tokenize, pos tag, stemming kai dhmiourgoume to inverted file.
import os
import nltk
from stemming.porter2 import stem
import xml.etree.ElementTree as et

#gia ta onomata  twn telikwn arxeiwn
counter = 1

#gia to stemmed word list
counter_stemmed = 0

#destination twn telikwn arxeiwn
if not os.path.exists('postagged'):
    os.mkdir('postagged')

#ta closed pos tags
closed_pos = ["CD" , "CC" , "DT" , "EX" , "IN" , "LS" , "MD" , "PDT" , "POS" , "PRP" , "PRP$" , "RP" , "TO" , "UH" , "WDT" , "WP" , "WP$" , "WRB"]

#arxikopoioume pinakes
postinglist = []
idf_list = []
idf_list_values = []
stemmed_words_list = []
xml_index = []

#Se auth th synarthsh ypologizoume ta term frequency enws arxeiou,
def createInvertedIndexFromFile(text):

    uninque_terms = []
    termFreq = []
    for term in text:
        if term not in uninque_terms:
            uninque_terms.append(term)
            termFreq.append(text.count(term))
    # print(len(uninque_terms))
    # print(termFreq)
    return (uninque_terms, termFreq, len(text))
    
#Dexete ta terms kai thn syxnothta auton enos keimenou, to posting list pou mas boithaei gia na doume an yparxei hdh egrafh sto xml, to onoma tou trexontos arxeiou, kai ta idf values twn terms.
#Epeita dhmiourgei to index. An enas oros den yparxei sto posting list tote shmainei oti prepei gia auton na dhmiourgithei neo tag lemma.
def createXMLInvertedIndex(terms, term_freq, postingl, number_of_words,filename,xml_index, idf_list,idf_list_values):

    for term in terms:
        if term not in postingl:
            postingl.append(term)
            term_element = et.SubElement(xml_index, 'lemma', attrib={'name': term})
            term_index = terms.index(term)
            term_freq_value = term_freq[term_index]
            idf_index = idf_list.index(term)
            idf_value = idf_list_values[idf_index]
            weight = term_freq_value/idf_value
            #print(postingl)
            document_element = et.SubElement(term_element, 'document', attrib={'id': filename, 'weight': str(weight)})
        else:
            for elem in xml_index.findall('./lemma'):
                #print(et.tostring(elem))
                if elem.attrib['name'] == term:
                    term_index = terms.index(term)
                    term_freq_value = term_freq[term_index]
                    idf_index = idf_list.index(term)
                    idf_value = idf_list_values[idf_index]
                    weight = term_freq_value/idf_value
                    document_element = et.SubElement(elem, 'document', attrib={'id': filename, 'weight': str(weight)})
                    
    #print(xml_index)
    return xml_index

        

#Etoimazoume to xml inverted index
xml_index = et.Element('inverted_index')
#print(et.tostring(xml_index))

for file in os.listdir('dest'):
    
    stemmed_words = []
    
    #ftiaxnoume to path gia na mporoume na to kanoume read
    filepath = os.path.join("dest", file)
    
    with open(filepath) as f:
        text = f.read()
        tokens = nltk.word_tokenize(text) #kanoume tokenize to keimeno
        tokens_pos = nltk.pos_tag(tokens) #kanoume pos tag ta tokens
        #print(tokens_pos)
        
        #apothikeuoume ta tokens
        filepath_write = os.path.join("postagged", str(counter))
        with open(filepath_write,"w+") as w:
            w.write(str(tokens_pos))
    counter+=1#gia ta onomata twn pos tagged keimenwn
    #print(tokens_pos)
    try:
        #afairoume ta closed tags enw tautoxrona ypologizoume ta idf kai kanoume kai stemming
        for x in range(0,len(tokens_pos)):
            if tokens_pos[x][1] in closed_pos:
                #print(tokens_pos[x][0])
                tokens_pos.remove((tokens_pos[x][0], tokens_pos[x][1]))
                #print(tokens_pos)
            else:
                stemmed_word = stem(tokens_pos[x][0])#stemming
                stemmed_words.append(stemmed_word)
                
                #ypologizoume ta idf
                if stemmed_word not in idf_list:
                    idf_list.append(stemmed_word)
                    idf_list_values.append(1)
                else:
                    idf_index = idf_list.index(stemmed_word)
                    idf_list_values[idf_index]+=1
            
    except IndexError:
        print(x)#prepei gia na apofygoume indeation error
        
    stemmed_words_list.append(stemmed_words)#h synolikh lista gia ola ta keimena
    
    #print(stemmed_words)
    
for file in os.listdir('dest'):
    print(stemmed_words_list[counter_stemmed])
    temp = createInvertedIndexFromFile(stemmed_words_list[counter_stemmed])
    # temp[0] = terms | temp[1] = term freq | temp [2] = doc number of words
    #print(temp)
    xml_index = createXMLInvertedIndex (temp[0], temp[1], postinglist, temp [2], file, xml_index, idf_list, idf_list_values)
    counter_stemmed+=1
    
#print(et.tostring(xml_index))

#Apothikeuoume to index
with open("xml_index.xml","w+") as wr:
    wr.write(et.tostring(xml_index,encoding='unicode', method='xml'))

w.close()
f.close()
wr.close()

