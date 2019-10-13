## Pitch

Lite Box is a solution developed to target the issue of hygiene within the Food & Beverage (F&B) industry with the help of digital making and data analytics to classify the status of plates (dirty/clean).

Inspiration:
During the soft launch for a cafe commandeered by visually impaired chefs in conjunction with Etch Empathy, the staff and manager reflected that hygiene is a hurdle towards obtaining proper license in running the cafe. Harbouring poor vision, the chefs and kitchen helpers are unable to identify small stains and bits of food wastes left on their cookery after wash-up. For instance, leftover scrambled eggs were spotted on one of the “clean” dishes meant to serve customers. This problem is evident of a deeper issue in society, one that is potentially deterring numerous visually impaired individuals from being hired and productive.

However, this issue with hygiene is not a problem solely for the visually impaired, but one that plagues the F&B industry as a whole. In addition to the spade of recent food poisoning incidents, an article from Straits Times (https://www.straitstimes.com/forum/letters-on-the-web/dishes-at-hawker-centres-must-be-washed-more-thoroughly) described how hawker centers need to wash their dishes more thoroughly despite the use of dishwashing technology. 

Taking the above into account, we believe that there is great potential for our product in empowering the visually impaired, and in the regulation of hygiene in the F&B industry.

## Some snippets

![Clean_plate](https://user-images.githubusercontent.com/44086084/66710931-aa62ab00-edb4-11e9-8762-05ccedb802ab.jpeg)
![Dirty_plate](https://user-images.githubusercontent.com/44086084/66710932-aa62ab00-edb4-11e9-82f2-199933931fbf.jpeg)


## Overview

LiteBox consist of 3 parts:
1. Light Box
2. Machine vision
3. Mobile application
The light box provides a stable platform and environment where the machine vision can take place, endowed with electronic components to make it smart. An ultrasonic sensor is positioned within to determine the presence of cookery, and consequentially switch on the LED lighting within to provide a well lit environment to reflect the state of the cookery placed within.

For machine visioning, a pre-trained MobileNet image classifier was fine-tuned on an open sourced dataset from Kaggle containing dirty and clean dishes. This was then complimented by a set of images trained within our light box, to improve classification accuracy and precision. The model was then converted into Tensorflowlite to be incorporated into the Android app. 

Coded with Android Studio(Java), the mobile application provides a platform that aggregates the above 2 parts of LiteBox in providing real time feedback on whether the cookery being inspected is clean or not. The results of the analysis from machine vision is displayed in prominent red and green, providing ease of identification to the visually impaired.

## Accomplishments

This is the 1st time for everyone on the team in participating in a 24h Hackathon, and we are glad that each of us were able to apply our skills in finishing the product, as well as learning from one another.

## Difficulties faced

The lack of large scale open source data set limited the accuracy and precision of the model, and required us to further update the training set with our own data. 
As we have never done cross platform integration for the above functions, it required us to read up extensive on the documentations online in addition to tutorial videos.

## Future work

In the future, we intend on improving the model accuracy and robustness through object detection on top of image classification.
The light box could be refurbished to better serve its purpose with higher power LEDs positioned on all sides.
We also intend on collaborating with the company mentioned above in obtaining a wider data set and in implementation of the above solution into their kitchen.
