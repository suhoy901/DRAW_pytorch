import numpy as np
import torch.autograd
import torch
import matplotlib.pyplot as plt
import os

USE_CUDA = torch.cuda.is_available()
T = 10
B = 28
A = 28
N = 5

def Variable(data, *args, **kwargs):
    if USE_CUDA:
        data = data.cuda()
    return torch.autograd.Variable(data,*args, **kwargs)

def unit_prefix(x, n=1):
    for i in range(n): x = x.unsqueeze(0)
    return x

def align(x, y, start_dim=0):
    xd, yd = x.dim(), y.dim()
    if xd > yd: y = unit_prefix(y, xd - yd)
    elif yd > xd: x = unit_prefix(x, yd - xd)

    xs, ys = list(x.size()), list(y.size())
    nd = len(ys)
    for i in range(start_dim, nd):
        td = nd-i-1
        if   ys[td]==1: ys[td] = xs[td]
        elif xs[td]==1: xs[td] = ys[td]
    return x.expand(*xs), y.expand(*ys)

def xrecons_grid(X,B=28,A=28):
    """
    plots canvas for single time step
    X is x_recons, (batch_size x img_size)
    assumes features = BxA images
    batch is assumed to be a square number
    """
    padsize=1
    padval=.5
    ph=B+2*padsize
    pw=A+2*padsize
    batch_size=X.shape[0]
    N=int(np.sqrt(batch_size))
    X=X.reshape((N,N,B,A))
    img=np.ones((N*ph,N*pw))*padval
    
    for i in range(N):
        for j in range(N):
            startr=i*ph+padsize
            endr=startr+B
            startc=j*pw+padsize
            endc=startc+A
            img[startr:endr,startc:endc]=X[i,j,:,:]
    return img

def save_image(x,count=0, dir_name='', batch_size=64):
    for t in range(T):
        img = xrecons_grid(x[t],B,A)
        plt.matshow(img, cmap=plt.cm.gray)
        imgname = dir_name + '/count_%d_%s_%d.png' % (count, 'test', t)
        plt.savefig(imgname)

def loss_plot(hist, path = 'Train_hist.png', model_name = ''):
    x = range(len(hist['loss']))

    y = hist['loss']

    plt.plot(x, y, label='loss')
    
    plt.xlabel('Iter')
    plt.ylabel('Loss')

    plt.legend(loc='upper right')
    plt.grid(True)
    
    path = os.path.join(path, model_name + '_loss.png')

    plt.savefig(path)

    plt.close()