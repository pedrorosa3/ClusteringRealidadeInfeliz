# 2022-2023 Programacao 2 LTI
# Grupo 35
# 60294 Pedro Rosa
# 60259 Matias D'Avó

import math 
import random

# Minkowski distance

def minkowskiDist(v1, v2, p):
    """
    Minkowski distance
    
    Requires:
    v1 and v2 are equal-dimension lists of numbers,
    representing feature vectors;
    p represents Minkowski order
    Ensures:
    Minkowski distance of order p between v1 and v2
    """
    dist = 0.0
    for i in range(len(v1)):
        dist += abs(v1[i] - v2[i])**p
    return dist**(1.0/p)

############## 25.1 Types Example and Cluster



class Example(object):
    """
    Example for clustering
    """

    def __init__(self, name, features, label = None):
        """
        Constructor

        Requires:
        features is list of numbers representing the feature vector;
        label is string with the label of the example
        Ensures:
        object of type Example created
        """
        self._name = name
        self._features = features
        self._label = label


    def dimensionality(self):
        """
        Dimensionality of the feature vector

        Ensures:
        dimensionality of the feature vector
        """
        return len(self._features)


    def setName(self, name):
        """
        Name setting

        Ensures:
        self._name = name
        """
        self._name = name

        
    def setFeatures(self, features):
        """
        Features setting

        Ensures:
        self._features = features
        """
        self._features = features
        

    def setLabel(self, label):
        """
        Label setting

        Ensures:
        self._label = label
        """
        self._label = label

    
    def getFeatures(self):
        """
        Features

        Ensures:
        feature vector
        """
        return self._features[:]


    def getLabel(self):
        """
        Object label

        Ensures:
        object label
        """
        return self._label


    def getName(self):
        """
        Object Name

        Ensures:
        object name
        """
        return self._name


    def distance(self, other):
        """
        Euclidean distance wrt a given example

        Requires:
        other is an example
        Ensures:
        the Euclidean distance between feature vectors
        of self and other
        """
        return minkowskiDist(self._features, other.getFeatures(), 2)


    def __str__(self):
        """
        String representation

        Ensures:
        string representation in the form "name:features:label"
        """
        return self._name + ',' + str(self._features) + ',' + str(self._label)


class Cluster(object):
    """
    Cluster of examples
    """
    
    def __init__(self, examples):
        """
        Constructor

        Requires:
        examples is a list of objects of a type that has
        a method returning the list of features of an object and
        a method returning the distance among them;
        Ensures:
        object of type Cluster is created
        """
        self._examples = examples
        self._centroid = self.computeCentroid()


    def update(self, examples):
        """
        Update the cluster with a given collection of examples

        Requires:
        examples a list of objects of the type of members in self._examples
        Ensures:
        examples = getExamples();
        returns how much the centroid has changed
        """
        oldCentroid = self._centroid
        self._examples = examples
        if len(examples) > 0:
            self._centroid = self.computeCentroid()
            return oldCentroid.distance(self._centroid)
        else:
            return 0.0


    def computeCentroid(self):
        """
        Compute centroid of the cluster

        Ensures:
        centroid of the cluster
        """

        dim = self._examples[0].dimensionality()
        totVals = [0]*dim
        for e in self._examples:
            for i in range(dim):
                totVals[i] = totVals[i]+e.getFeatures()[i]
        totValsAveraged = []
        for i in range(dim):
            totValsAveraged.append(totVals[i]/float(len(self._examples)))
        centroid = Example('centroid', totValsAveraged)
        return centroid
    

    def getExamples(self):
        """
        Examples in the cluster

        Ensures:
        list with examples in the cluster
        """
        return self._examples


    def getCentroid(self):
        """
        Centroid of the cluster

        Ensures:
        centroid of the cluster
        """
        return self._centroid

            
    def size(self):
        """
        Size of the cluster

        Ensures:
        number of examples in cluster
        """
        return len(self._examples)
    

    def variability(self):
        """
        Variability

        Ensures:
        variance of the cluster
        """
        totDist = 0.0
        for e in self._examples:
            totDist += (e.distance(self._centroid))**2
        return totDist
    

    def members(self):
        """
        Generator method
        """
        for e in self._examples:
            yield e
            

    def __str__(self):
        """
        String representation

        Ensures:
        string representation in the form
        "Cluster with centroid [...] contains:
         ex1 ex2 ... exN "
        """
        names = []
        for e in self._examples:
            names.append(e.getName())
        names.sort()
        result = 'Cluster with centroid '\
                 + str(self._centroid.getFeatures()) + ' contains:\n'
        for e in names:
            result = result + e + ', '
        return result[:-2] #remove trailing comma and space




############## 25.2 K-means Clustering



def kmeans(examples, k, verbose,exemplars):
    """
    K-means clustering
    
    Requires:
    examples a list of examples of a same type;
    k positive int, number of clusters;
    verbose Boolean, printing details on/off
    Ensures:
    list containing k clusters;
    if verbose is True, result of each iteration
    of k-means is printed
    """
    #Get k randomly chosen initial centroids, create cluster for each
    if exemplars==[]:
        
        initialCentroids = random.sample(examples, k)
    else:
        initialCentroids = exemplars
    
    clusters = []
    for e in initialCentroids:
        
        clusters.append(Cluster([e]))

    #Iterate until centroids do not change
    converged = False
    numIterations = 0
    while not converged:
        
        numIterations += 1

        #Create a list containing k distinct empty lists
        newClusters = []
        for i in range(k):
            newClusters.append([])

        #Associate each example with closest centroid
        for e in examples:
            #Find the centroid closest to e
            smallestDistance = e.distance(clusters[0].getCentroid())
            index = 0
            for i in range(1, k):
                distance = e.distance(clusters[i].getCentroid())
                if distance < smallestDistance:
                    smallestDistance = distance
                    index = i
            #Add e to the list of examples for the appropriate cluster
            newClusters[index].append(e)

        #Avoid having empty clusters
        for c in newClusters:
            if len(c) == 0:
                raise ValueError("Empty Cluster")

        #Update each cluster; check if a centroid has changed
        converged = True
        for i in range(len(clusters)):
            if clusters[i].update(newClusters[i]) > 0.0:
                converged = False

        #Trace intermediate levels of clustering if verbose on        
        if verbose:
            print('Iteration #' + str(numIterations))
            for c in clusters:
                print(c)
            print('') #add blank line        

        
            
    return clusters,initialCentroids

def dissimilarity(clusters):
    """
    Dissimilarity among clusters

    Ensures:
    dissimilarity among clusters as the summation
    of each cluster variance
    """
    totDist = 0.0
    for c in clusters:
        totDist += c.variability()
    return totDist


def trykmeans(examples, numClusters, numTrials,exemplars,
              verbose = False):
    """
    Best clustering outcome within a given number of trials
    of k-means clustering

    Requires:
    examples a list of examples of a same type;
    numClusters positive int, number of clusters;
    numTrials positive int, number of trials with k-means clustering
    Ensures:
    The clusters obtained with the lowest dissimilarity among them
    after running k-means clustering numTrials times over examples
    """
    best,initialcentroids = kmeans(examples, numClusters, verbose,exemplars)
    minDissimilarity = dissimilarity(best)
    
    for trial in range(1, numTrials):
        clusters,centroids = kmeans(examples, numClusters, verbose,exemplars)
        currDissimilarity = dissimilarity(clusters)
        if currDissimilarity < minDissimilarity:
            best = clusters
            minDissimilarity = currDissimilarity
            initialcentroids=centroids
            
    return best,initialcentroids



def ReadFileTitles(filename):
    """
    Reads the file and save the informations in a dictionary(keys are the titles and values are the number)
    Requires: filename is a .txt file
    Ensures: dictionary with the informations on the .txt file
    """
    dict={}

    content=[]
    try:
        file=open(filename,"r")
    except FileNotFoundError:
        print("Could not found this file")
        file.close()
    finally:
        for line in file.readlines()[1:]:
            content.append(line)
        file.close()
        titles=[]
        for i in content:
            contentdata=(i.rstrip().split("; "))
            titles.append(contentdata)
    for i in titles:
        
        dict[i[1]]=int(i[0])
        dict[i[2]]=int(i[0])
        

    return dict 


def ReadFileCandidates(filename,k):
    """
    Reads the file and save the informations in a list
    Requires: filename is a .txt file
    Ensures: List of lists with the information contained in the .txt file
    """
    content=[]
    
    try:
        file=open(filename,"r")
    except FileNotFoundError:
        print("Could not found this file")
        file.close()
    finally:
        for line in file.readlines()[3:]:
            content.append(line)
        
        candidates=[]
        exemplars=[]
        flag=False
        for i in range(len(content)):
            
            if content[i] == "#Exemplars:\n":
                
                flag=True
                
                content_exemplars=content[(i+1):]
                
                for y in content_exemplars:     
                    exemplarsdata=y.rstrip().split("; ")
                    exemplars.append(exemplarsdata)
                    
                       
            else:
                if flag==False:
                    contentdata=(content[i].rstrip().split("; "))
                    candidates.append(contentdata)
                  
            if (exemplars!=[] and exemplars!=[["void"]]):
                if len(exemplars)!=k:
                    raise Exception("The numbers of Exemplars in the inputFile is different than the "+str(k)+" clusters that you want to create.")

            

    return candidates,exemplars


def ListtoObject(dicttitles,listcandidates):
    """
    Create a list of Example objects with the information of the dictionary and the list of the candidates
    Requires: dictitles is a dictionary that associate a feature to a number, and listcandidates are list of list with name and features of the candidates 
    Ensures:  List of Examples Object with the name of the candidate and the features in a numbers.
    """
    examples=[]
    for i in listcandidates:
        try:
            candidato=Example(i[0],[dicttitles[i[1]],dicttitles[i[2]],dicttitles[i[3]],dicttitles[i[4]],dicttitles[i[5]],dicttitles[i[6]]])
            examples.append(candidato)
        except:
            raise Exception("Input File does not have candidates!")        
    return examples