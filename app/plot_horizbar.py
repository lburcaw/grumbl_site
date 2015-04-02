import numpy as np
import matplotlib.pyplot as plt
import random as rand

#perc must be rounded int
def plot_hbar(labels,perc,date):
    plt.clf()
    fig = plt.figure(figsize=(8,6))
    ax = fig.add_subplot(1,1,1)
    pos = np.arange(len(labels))
    plt.subplots_adjust(bottom=0.15,top=0.95,left=0.2)
    plt.barh(pos, perc,align='center',alpha=0.7,linewidth=0,color='#0CA1F1')
    ax.set_xlabel('Probability (%)',fontsize=20,color='white') 
    ax.tick_params(axis='x', colors='white')
    plt.xticks(fontsize=20)
    plt.yticks(pos,labels,fontsize=20)
    ax.tick_params(axis='y', colors='white')
    ax.set_frame_on(False)

    for p, cm, pr in zip(pos, labels,perc):
        plt.annotate(str(pr)+'%', xy=(pr+1,p), va='center',color='white',fontsize=20)
    plt.xlim([0, 110])
    plt.tick_params(axis="both", which="both", bottom="off", top="off",  
                labelbottom="on", left="off", right="off", labelleft="on") 
    plt.title('Probabilities for ' + date.title(), color='w',fontsize=25)
    fig.set_facecolor('black')
    fig.patch.set_alpha(0.7)
    ax.set_axis_bgcolor('black')
    ax.patch.set_alpha(0.2)
    hbar_name = 'hbar_'+str(int(rand.random()*1e6))
    plt.savefig('app/static/img/'+hbar_name,facecolor=fig.get_facecolor(), edgecolor='none',bbox_inches='tight')
    return(hbar_name)