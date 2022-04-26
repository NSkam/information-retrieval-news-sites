#Arxika analoga thn eisodo tha mporoume na kalesoume thn preprocess pou tha kataskeuazei to eurethrio h na kanoume load hdh etoimo.
#0--> Kataskeuh
#1--> Load

import sys
import xml.etree.ElementTree as et
import time

parser = et.XMLParser(encoding="utf-8")

#0 gia kataskeuh eurethriou kai 1 gia load eurethriou
if sys.argv[1] == "0":
    os.system('python preprocess.py')
    with open("xml_index.xml") as f:
        index_file = f.read()
        index = et.fromstring(index_file, parser=parser)
       
elif sys.argv[1] == "1":
    with open("xml_index.xml") as f:
        index_file = f.read()
        index = et.fromstring(index_file, parser=parser)
       
#Pairnoume to query apo to xrhsth
#query = input("Please enter your query here: ")
query_list = ["Listen", "BBC", "reduc", "Californian","acr","wildfir","unanim","inconsist", "shelter", "charter","interim","Area","inspect","reorganis","distract","sore","smile","committe","Emergenc","rider motocross", "supervisor lifeguard", "deeper swept", "sorri careless", "truck verbal", "Station destroy", "arson wooden", "pavilion Passeng", "ticket convey", "free rundown","transfer togeth","Listen BBC","reduc Californian","acr wildfir","unanim inconsist", "shelter charter","interim Area","inspect reorganis","distract sore","smile committe","Emergenc free","Listen BBC reduc", "Californian acr wildfir","unanim inconsist shelter", "charter interim Area","inspect reorganis distract","sore smile committe","Emergenc rider motocross","hear Chelsea wage","twice relax consum", "supervisor lifeguard run-up", "deeper swept Brexit", "sorri careless Low", "truck verbal Helen", "Station destroy trade", "arson wooden festiv", "pavilion Passeng Christma", "ticket convey competit", "free rundown toy","transfer togeth depend","Listen BBC uniform","reduc Californian hike","acr wildfir Price","unanim inconsist ship", "shelter charter cloth","interim Area babi","inspect reorganis tenur","distract sore smile committe","Emergenc free rider motocross", "supervisor lifeguard deeper swept", "sorri careless truck verbal", "Station destroy arson wooden", "pavilion Passeng ticket convey", "free rundown transfer togeth","Listen BBC reduc Californian","acr wildfir unanim inconsist", "shelter charter interim Area","inspect reorganis distract sore","smile committe Emergenc free","Listen BBC reduc Emergenc", "Californian acr wildfir committe","unanim inconsist shelter smile", "charter interim Area sore","inspect reorganis distract Area","sore smile committe reorganis","Emergenc rider motocross distract","hear Chelsea wage interim","twice relax consum wildfir", "supervisor lifeguard run-up Listen", "deeper swept Brexit BBC", "sorri careless Low Brexit", "truck verbal Helen Californian", "Station destroy trade reduc", "arson wooden festiv acr", "pavilion Passeng Christma Station", "ticket convey competit truck", "free rundown toy trade","transfer togeth depend destroy","Listen BBC uniform wooden", "free rundown Christma Station", "arson wooden Listen BBC"]
#print(len(query_list))
start_time = time.time()
for query in query_list:
    query_terms = query.split()#pairnoume ta terms tou query

    document_list = []
    retrieval_list = []

    #Diatrexei to index gia ta terms tou query kai prosthetei opou xreiazete ta baroi tous
    for term in query_terms:
        for elem in index.findall('./lemma'):
        #print(et.tostring(elem))
            if elem.attrib['name'] == term:
                for document in elem:
                    if document.attrib['id'] not in document_list:
                        document_list.append(document.attrib['id'])
                        retrieval_list.append([document.attrib['id'], float(document.attrib['weight'])])
                    else:
                        term_index = document_list.index(document.attrib['id'])
                        retrieval_list[term_index][1] += float(document.attrib['weight'])

    retrieval_list.sort(reverse=True, key=lambda x: x[1])#kanei sort thn lista
    #print(retrieval_list)
print("Total time:  %s seconds" % (time.time() - start_time))
print("Average Time: %s seconds" % ((time.time() - start_time)/100))