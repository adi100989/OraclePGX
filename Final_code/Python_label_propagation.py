__author__ = 'adi100989'

import community
import networkx as nx
import matplotlib.pyplot as plt

def label_prop():
    #G=nx.read_adjlist("facebook_combined.adj",create_using=nx.Graph(),nodetype=int)
    #print "graph loaded"
    #print len(G.nodes())
    #G=nx.read_edgelist("facebook_combined.txt", create_using = nx.Graph(), nodetype = int)
    G=nx.read_edgelist("small_graph.edge", create_using = nx.Graph(), nodetype = int)
    print nx.info(G)
    #g=nx.generate_adjlist(G,delimiter=',')
    #print len(g.nodes()), len(g.edges())


    for i in G.nodes():
        G.node[i]['label']=i
        G.node[i]['ID']=i
        G.node[i]['l_1']=-99
        G.node[i]['l_2']=-99
        G.node[i]['l_next']=-99
    com=set()
    for i in G.nodes():
        com.add(G.node[i]['label'])
    print "the number of unique labels= ",len(com)


    '''
    for n,nbrs in G.adjacency_iter():
        for nbr,edict in nbrs.items():
            if nbr==200:
                print n, nbrs, G.node[nbr]['label']
    '''
    mainStop=False
    i=0
    while(not mainStop):
        if i==6:
            set_communities=set()
            for n in G.nodes():
                set_communities.add(G.node[n]['label'])
                print G.node[n]['label'],
            print "\n the number of communities after convergence==",len(set_communities)
            return i

        i+=1
        mainStop=False
        l1_stop=True
        l2_stop=True
        for n in G.nodes():
            if(not(G.node[n]['label']==G.node[n]['l_1'])):
                l1_stop=False
        for n in G.nodes():
            if(not(G.node[n]['label']==G.node[n]['l_2'])):
                l2_stop=False

        #print l1_stop, l2_stop
        if( not (l1_stop or l2_stop)):
            #print "in not loop"
            #for n,nbrs in G.adjacency_iter() :
            for n in G.nodes():
                dict={}
                dict.clear()
                for nbr in G.neighbors(n):
                #for nbr,d in nbrs.items():
                    temp=G.node[nbr]['label']
                    if not dict.has_key(temp):
                        #dict[temp]=1
                        dict.update({temp:1})
                    else:
                        dict[temp]+=1
                #print dict
                max_key=-99
                max_freq=-99
                max_list=[]
                #print dict
                for element in dict:
                    if max_freq<=dict[element]:
                        max_freq=dict[element]

                for element in dict:
                    if dict[element]==max_freq:
                        max_list.append(element)
                max_key=max(max_list)
                #print " iteration ",i,"max list is ",n,max_list
                if(max_key==-99):
                    max_key=G.node[n]['label']

                #max_key= max(dict,key=dict.get)
                #print "FINAL",max_key
                G.node[n]['l_next']=max_key

            for n in G.nodes():
                G.node[n]['l_2']=G.node[n]['l_1']
                G.node[n]['l_1']=G.node[n]['label']
                G.node[n]['label']=G.node[n]['l_next']

        else:
            print "The Community converges"
            mainStop=True
            set_communities=set()
            x=0
            for n in G.nodes():
                set_communities.add(G.node[n]['label'])

            print set_communities

            print "the number of communities after",i," iterations==",len(set_communities)
            for n in G.nodes():
                print G.node[n]['label'],
            return i

def main():
    label_prop()

if __name__ == '__main__':
    main()
