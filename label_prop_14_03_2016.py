__author__ = 'adi100989'
import community
import networkx as nx
import matplotlib.pyplot as plt

def label_prop():
    G=nx.read_edgelist("facebook_combined.txt", create_using = nx.Graph(), nodetype = int)
    print nx.info(G)

    for i in G.nodes():
        G.node[i]['label']=i
        G.node[i]['ID']=i
        G.node[i]['l_1']=0
        G.node[i]['l_2']=0
        G.node[i]['l_next']=0

    '''
    for n,nbrs in G.adjacency_iter():
        for nbr,edict in nbrs.items():
            if nbr==200:
                print n, nbrs, G.node[nbr]['label']
    '''
    mainStop=False
    i=0
    while(i<100):
        if i==99:
            set_communities=set()
            for n in G.nodes():
                set_communities.add(G.node[n]['label'])
            print "the number of communities after 100 iterations==",len(set_communities)

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
            for n,nbrs in G.adjacency_iter():
                dict={}
                dict.clear()
                for nbr,d in nbrs.items():
                    temp=G.node[nbr]['label']
                    if not dict.has_key(temp):
                        dict={temp:1}
                    else:
                        dict[temp]+=1
                max_key=0
                max_key= max(dict,key=dict.get)
                G.node[n]['l_next']=max_key
                G.node[n]['l_2']=G.node[n]['l_1']
                G.node[n]['l_1']=G.node[n]['label']
                G.node[n]['label']=max_key
            '''
            for n in G.nodes():
                G.node[n]['l_2']=G.node[n]['l_1']
                G.node[n]['l_1']=G.node[n]['label']
                G.node[n]['label']=G.node[n]['l_next']
            '''


        else:
            print "The Community converges"
            mainStop=True

            print i
            return i

def main():
    label_prop()

if __name__ == '__main__':
    main()
