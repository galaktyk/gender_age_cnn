## Overview
Gender & Age classification with VGG19

## Usage 
[Download model.h5](https://drive.google.com/open?id=1bQ9vfeNqGrWJ1NctqVdaR_CvDNOr8cL5)  
Train, Val : use the nootbook file  
Webcam test : use run_webcam.py

## Dataset
[Adiencedb Face](https://talhassner.github.io/home/projects/Adience/Adience-data.html)  
Gender : Male, Female  
Age groups : (0-2, 4-6, 8-13, 15-20, 25-32, 38-43, 48-53, 60-100)
## Network Architecture
It just VGG19 with modified output head

![](https://github.com/galaktyk/gender_age_cnn/blob/master/doc/model16.png)
## Validation accuracy
Gender : 0.95  
Age : 0.73  
![](https://github.com/galaktyk/gender_age_cnn/blob/master/doc/val1.png)
![](https://github.com/galaktyk/gender_age_cnn/blob/master/doc/val2.png)
