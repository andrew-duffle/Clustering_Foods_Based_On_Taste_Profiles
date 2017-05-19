# -*- coding: utf-8 -*-
import numpy as np
#import matplotlib
import matplotlib.pyplot as plt
from matplotlib import style 
style.use("ggplot")
#import mpl_toolkits.mplot3d.axes3d as p3
#from matplotlib.mlab import PCA as mlabPCA

from sklearn.cluster import  MiniBatchKMeans,KMeans,AgglomerativeClustering
#from sklearn.cluster import MeanShift 
#from sklearn.datasets.samples_generator import make_blobs
#from sklearn.metrics.pairwise import paired_distances, cosine_similarity
#from sklearn.manifold import MDS
#from scipy.cluster import hierarchy
from sklearn.decomposition import PCA
import pandas as pd
import csv ########???????

def ClusterPlot():
    #
    with open('srep00196-s2.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        data=[]
        for row in reader:
            data.append(row)
    
    data= data[5:] ######leave out 500 when clustering all
    
    
    with open('data.csv','w', newline='') as fp:
        a = csv.writer(fp, delimiter=',')
        headers = [['Food','Compared_to','Weight']]
        a.writerows(headers)
        data_to_write = data
        a.writerows(data_to_write)
    
    data_df= pd.read_csv('data.csv')
    pivot_data=pd.DataFrame(pd.pivot_table(data_df,index=["Food"],columns='Compared_to', values='Weight',fill_value=0))
    pivot_data=pivot_data.astype(int)
    
    #######################################################
    pivot_data.to_csv('pivot.csv')
    
    with open('pivot.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        data=[]
        for row in reader:
            data.append(row)
            
    names=[]
    
    for row in data:
        names.append(row[0])
        del row[0]
    del (data[0]) #remove some header rows
    del (names[0]) #remove some header rows
    feature=[]
    
    for l1 in data:
        feature.append([int (i) for i in l1])
    
        
    #feature=feature[0:10000]    #remove after complete to get full data set this gets 1000 items
    
    
    #start
    #######MiniBatch with print of clusters
    Number_Clusters=7 #need to adjust up or down based on number of target clusters 100+
    batch=1000
    
    mbk=MiniBatchKMeans(init='k-means++', n_clusters=Number_Clusters,batch_size=batch,
                        n_init=20, max_no_improvement=30, verbose=0,random_state=5)
                        
    feature=np.array(feature)
    
    X_PCA=PCA(n_components=2, whiten=True).fit_transform(feature)
    #print(X_PCA)
    
    mbk.fit(feature) 
    
    labels=mbk.predict(feature) 
    
    colors = ['k.','w.','r.','y.','g.','c.','b.','m.','k.','b.']   
    ClustersToPlot=7
    toPlot={}
    nth=0
    for item in labels:
        if item < ClustersToPlot:
            plt.plot(X_PCA[nth][0], X_PCA[nth][1], colors[labels[nth]], markersize=10)
            #labels[item].append(X_PCA[nth])
            #if labels[nth] ==3:
                #print("cluster:",labels[item], "Cords:",X_PCA[nth],"Name:",names[nth])
        nth +=1
    
    plt.plot(-.6,0, marker='$1$', color="black",markersize=15,label="Nut:Seeds:Oils")#1**********
    plt.plot(.5,2, marker='$2$', color="black",markersize=15,label="Citrus Flavors")#0******
    plt.plot(1.5,-2.5, marker='$3$', color="black",markersize=15,label="Fowl:Pork:Meat:Milk High Fat")#3*******
    plt.plot(.75,-4, marker='$4$', color="black",markersize=15,label="Roasted:Smoked Meats")#5 *******
    plt.plot(2,2, marker='$5$', color="black",markersize=15,label="Berries:Bananas:Apricot Fruit and Berrie")#2***** 
    plt.plot(3.5,1, marker='$6$', color="black",markersize=15,label="Wine:Coffee:Tea Natural Flavors")#4*******
    plt.plot(4,4, marker='$7$', color="black",markersize=15,label="Beer:Bacon:Boiled Meats Traditional Flovors Close to 6")#6*******   
    plt.ylim(-15,5)
    plt.legend(loc='lower left',ncol=1,numpoints=1)#bbox_to_anchor=(2,.5),
    
    
    plt.show()
    
    
#ClusterPlot()    

#==============================================================================
# #Print out clusters
# n1=0
# for item in names:
#     if item == 'coffee':
#         print (X_PCA[n1])
#     else:
#         n1 +=1
# 
# 
# 
# clusters={}
# n=0
# for item in labels:
#     if item in clusters:
#         clusters[item].append(names[n])
#     else:
#         clusters[item]=[names[n]]
#     n +=1
# 
# for item in clusters:
#     #if item > 10:
#         
#     print ("--------------------------Cluster ", item)
#     for i in clusters[item]:
#         print (i)
# 
#==============================================================================


#==============================================================================
# #start
# ###############################High Work
# Hclust = AgglomerativeClustering(n_clusters=60, affinity='euclidean', linkage='ward').fit(feature)
# label=Hclust.labels_
# 
# ytdist=np.array(feature[:50])
# 
# clusters={}
# n=0
# for item in label:
#     if item in clusters:
#         clusters[item].append(names[n])
#     else:
#         clusters[item]=[names[n]]
#     n +=1
# 
# for item in clusters:
#     print ("--------------------------Cluster ", item)
#     for i in clusters[item]:
#         print (i)
#  
# #==============================================================================
# # #########Scipy High   works fine    
# # Z=hierarchy.linkage(ytdist,'single')
# # plt.figure()
# # dn=hierarchy.dendrogram(Z)
# # #hierarchy.set_link_color_palette(20*['m','c','y','k'])
# # #fig, axes =plt.subplot(1,2,figsize=(8,3))
# # plt.show()
# # print(names[0])
# # print(names[3])
# # print(names[4])
# # print(Z)
# #==============================================================================
#
#==============================================================================





