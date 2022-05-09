import pandas as pd
import bs4 as bs
import regex as re
import datetime
import os
import matplotlib.pyplot as plt

__version__ = "0.1.0"

def extract(file): 
    """
    Extraction de données d'une page Europesse (nombre limités de champs)
    """
    corpus_html = bs.BeautifulSoup(open(file, encoding="utf8"),"lxml")    
    corpus = [] #tableau que l'on va remplir avec les données
    for i in corpus_html.find_all("article"):
        
        #on regarde s'il y a un titre dans l'article
        try:
            titre = i.find("div",{"class":"titreArticle"}).text 
        except:
            titre = None #sinon on renvoie rien
            
        #Pareil pour la date/header
        try:
            header = i.find("span",{"class":"DocHeader"}).text
        except:
            header = None
        
        #Le nom de la publicatoin
        try:
            publication = i.find("span",{"class":"DocPublicationName"}).text
        except:
            publication = None
         
        #le contenu
        try:
            text = i.find("div",{"class":"DocText clearfix"}).text
        except:
            text = None
            
        #le contenu
        try:
            auteur = i.find("div",{"class":"docAuthors"}).text
        except:
            auteur = None
            
        #On ajoute ces éléments au corpus
        corpus.append([header,titre,publication,text,auteur])
        
    return corpus #On renvoie les informations


def reco_date(x):
    """
    Recoder la date telle que présente dans un fichier europresse
    """
    mois = {"janvier":"01","février":"02","mars":"03",
            "avril":"04","mai":"05","juin":"06","juillet":"07",
            "août":"08","septembre":"09","octobre":"10","novembre":"11",
            "décembre":"12"}
    
    t = re.findall("\w+ \w+ [0-9]{4}",x)
    
    if len(t) <1:
        return None

    t = t[0]
    
    for i in mois:
        if i in t:
            t = t.replace(i,"/%s/"%mois[i]).replace(" ","")

    t = datetime.datetime.strptime(t,"%d/%m/%Y")
            
    return t