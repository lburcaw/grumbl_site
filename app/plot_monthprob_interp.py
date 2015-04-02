import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
import random as rand

def interp_probs(arr):
    xnew = np.linspace(1, 12, 20)
    months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    labels = ['Building','Noise','Street','Vermin']
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    #fig.canvas.draw()
    for i in [0,20,40,60,80,100]:
        plt.plot([1,12],[i,i],color='w',linewidth=2)
    for i in [3,6,9,12]:
        plt.plot([i,i],[-1,100],color='w',linestyle = ':')
    swatch = ['#FFFE83','#0CA1F1','#35B81C','#FF7F00']
    q = 0
    for col in arr.T:
        f2 = interp1d(np.arange(1,13), col, kind='cubic')
        ax.plot(xnew,100*f2(xnew),label=labels[q],linewidth=4,color=swatch[q])
        plt.ylim([-1,100])
        plt.xlim([1,12])
        plt.xticks(np.arange(1,13),rotation=70)
        plt.yticks(fontsize=22,color='w')
        ax.set_xticklabels(months,fontsize=22,color='w')
        plt.ylabel('Probability (%)',fontsize=22,color='w')
        q += 1
    
    ax.set_frame_on(False)
    legend = plt.legend(loc=9, fontsize=20, bbox_to_anchor=(1.2, .6),frameon=1)
    frame = legend.get_frame()
    for text in legend.get_texts():
        text.set_color('w')

    frame.set_facecolor('black')
    frame.set_edgecolor('white')
    fig.set_facecolor('black')
    fig.patch.set_alpha(0.7)
    ax.set_axis_bgcolor('black')
    ax.patch.set_alpha(0.2)
    ax.yaxis.grid(True)
    plt.title('Typical Probabilities for the Year',fontsize=25,color='w')
    monthprob_name = 'monthprob'+str(int(rand.random()*1e6))
    plt.savefig('app/static/img/'+monthprob_name,facecolor=fig.get_facecolor(), edgecolor='none',bbox_inches='tight')
    return(monthprob_name)