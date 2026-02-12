# 2022-2023 Programacao 2 LTI
# Grupo 35
# 60294 Pedro Rosa
# 60259 Matias D'Avó

import sys
from clustering import Example,kmeans,ReadFileCandidates,ReadFileTitles,ListtoObject,Cluster,trykmeans
k=int(sys.argv[1])
titles=sys.argv[2]
candidates=sys.argv[3]

list_candidates,exemplars=ReadFileCandidates(candidates,k)
dict_titles=ReadFileTitles(titles)

Exemplars=[]
if exemplars != [["void"]]:
    
    Exemplars=ListtoObject(dict_titles,exemplars)


Examples=ListtoObject(dict_titles,list_candidates)


final,centroids=trykmeans(Examples,k,1,Exemplars,True)



def SearchListFinal(list_candidates,final):
    """
    Check with features correspond to the name of the person 
    Requires: list_candidates is a list of list with the names and features of the candidates, and final is the name of a candidate.
    Ensures: str with the name and features of the person name.
    """
    
    for x in list_candidates:
            
        if final == x[0]:
            lista=""
            for line in range(len(x)):
                if line == 0:
                         
                    lista=lista+str(x[line])
                else:
                    lista=lista+"; "+str(x[line])   
            return lista     


def SearchListCentroid(exemplars,centroid):
    """
    Check with features correspond to the name of the person that is the centroid
    Requires: list_candidates is a list of lists with the names and features of the candidates, centroid is a example object
    Ensures: str with the name and the features of the person name that is a centroid 

    """
    
    
    for x in exemplars:
        if centroid.getName()== x[0]:
            
            lista=""
            for line in range(len(x)):
                 
                if line == 0:
                         
                    lista=lista+str(x[line])
                else:
                    lista=lista+"; "+str(x[line]) 
                     
            return lista
            



def WritetoFile(list_candidates,exemplars,final,centroids):
    """
    Write a File with the exemplars and each correspondant clusters to that exemplar.
    Requires: list_candidates is a list of lists with names and features of the candidates, centroids are the exemplars in example object.
    Ensures: .txt file with the information of the exemplars and each correspondant cluster to that exemplar. 
    """
    file=open("candidates.txt","w")
    
    
    for i in range(len(final)):

        

        file.write("#exemplar "+str(i+1)+":\n")
        if exemplars == [["void"]]:
            file.write((SearchListCentroid(list_candidates,centroids[i]))+"\n")
        else:
            file.write((SearchListCentroid(exemplars,centroids[i]))+"\n")


        file.write("#cluster "+str(i+1)+":\n")
        for x in range(final[i].size()):
            if final[i].getExamples()[x].getName() == centroids[i].getName():
                pass
            else:
                 file.write((SearchListFinal(list_candidates,final[i].getExamples()[x].getName()))+"\n")
        file.write("\n")         


    file.close()
    return file
               
WritetoFile(list_candidates,exemplars,final,centroids)
