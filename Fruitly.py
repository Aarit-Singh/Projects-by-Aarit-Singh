'''
**YOU DO NOT HAVE TO READ THIS**, this is a secondary overview of the project, goving into more detail.
  this is perhaps my favorite project i have ever done, it holds a very special place in my heart as the first ever* ML project i completed.
  i calculated my own mean and standard deviation of the data, applied transformations to and noralized the data to improve model accuracy
  i never finished the UI, as i didnt see a reason to, i didnt intend to publish this project, and i mainly did this as a stepping stone into the 
  greater pytorch ecoystem.
  '''

import tkinter
import torch 
from datetime import date
import io
from PIL import Image
from torch import nn, save, load
from torch.optim import Adam
import json
from torch.utils.data import DataLoader, dataset, Dataset
import torchvision
from torchvision import datasets
from torch import *
from torchvision.transforms import ToTensor, Resize
import torchvision.transforms as trforms 
from datasets import *
from time import *
import time
import math
from math import *
from tkinter import *
from PIL import Image, ImageTk
from classcheck import *

training_path = "Fruits_app/archive_fruits/archive/fruits-360_dataset/fruits-360/Training"
mean = [0.4914, 0.4822, 0.446]
std = [0.2023, 0.1994, 0.2010]
train_transforms = trforms.Compose([
    trforms.Resize(64),
    trforms.RandomHorizontalFlip(0.25),
    trforms.RandomRotation((45 | 90 | 270 )),
    trforms.ToTensor(),
    trforms.Normalize(torch.Tensor(mean),torch.Tensor(std)) #Normalizes dataset, strongly improves preformance, bascilly preforms a opperation on immage to make them more efficiant while training.
])
train_dataset = torchvision.datasets.ImageFolder(root = training_path, transform = train_transforms)
train_loader = torch.utils.data.DataLoader(dataset=train_dataset, batch_size = 32, shuffle = True)

class fruits_classifier(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Conv2d(3, 32, (3,3)), #creates conv2d layer for immage use, 1 input layer, 32 output layers for first, 3,3 kernal size passed to next layer
            nn.ReLU(),
            nn.Conv2d(32, 64, (3,3)),
            nn.ReLU(),
            nn.Conv2d(64, 64, (3,3)),
            nn.ReLU(),
            nn.Flatten(), #transforms tensor output to a vector output
            nn.Linear(64*(64-6)*(64-6),131) # applies linear transformation to object, pushed highest activation node out of the 131 output nodes corresponding to an individual fruit as the solution to the recognition task
        )
        
    def forward(self, x):
        x = x.view(x.size(0), -1)
        return self.model(x)


clf = fruits_classifier().to("cpu")
def checkstate( fp: str) -> str:
    with open(fp, 'rb') as fprime:
        n = fprime.read()
        global contents
        if n =="":
            contents = False
        else:
            contents = True
checkstate(fp = "Fruits_app/fruits_model.pt")
optimizes = Adam(clf.parameters(), lr = 1e-3)
lossfn = nn.CrossEntropyLoss()

        
epochs = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]                
retrain_self = True
if (retrain_self !=False) | (contents == False):
    print(("training underway, retrain set to: {}, and contents present: {}").format(retrain_self, contents))
    for epoch in epochs:
        start_time = time.time()
        print("Epoch", str(epoch), "out of", str(epochs[-1]), "Has Started")
        for batch in train_loader:
            
            X,Y = batch
            X,Y = X.to('cpu'), Y.to('cpu')
            yhat = clf(X)
            print(yhat)
            loss = lossfn(yhat, Y)
            
            optimizes.zero_grad() #resets all gradiants
            loss.backward() #applies backpropegation (ML Technique that passes through NN)
            optimizes.step() #Passes through layer and to output
        elapsed_time = time.time()-start_time
        elapsed_time_mins = elapsed_time/60
        est_until_completion = (math.floor(elapsed_time/60)+1)*(epochs[-1]-epoch+1)
        print("Epoch: {}; loss is: {}; Elapsed time this epoch: {} mins; ETA untill training completion is: {} Mins".format(epoch, loss, math.floor(elapsed_time_mins), est_until_completion, ))
    with open("fruits_model.pt", 'wb') as f:
            torch.save(clf.state_dict(), f)
    with open('logs.txt', 'w') as r:
            r.write("most recent training finshed on {}".format(date.today()))
    screen_val =0
if contents == True:
    print("Training Skipped, model already present")

    
