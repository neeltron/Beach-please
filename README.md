# Beach, please

When we picture ourselves at the seaside on vacation, we imagine a clean seashore with clear water. But, in reality, this is never the case, as marine pollution has become one of humanity's biggest concerns. Thanks to human negligence, most of the beaches on our planet are littered with plastic and non-biodegradable trash, which eventually reach the sea and damage the marine ecosystem. As fellow stewards of this Earth, we were inspired to build something that can help restore beaches and protect sea life. 

The automated smart rover built by us moves around the beach to identify and pick up trash. The wheels of the rover are potent enough to move across dry as well as wet sand. The camera of the Raspberry pi 4 used in this rover takes an image of the material, and then it sends that image to Google Cloud. With the help of Google's CloudVision API, it identifies what is there in the image and returns it to my client. Depending upon the type of that object, the program classifies it as either trash or not. If the object gets identified as trash, then the rover picks it up, moves, and gathers them to a specific corner away from the seashore, making it easy for the garbage collector to collect the whole trash of the site at once. And the rover keeps repeating the process of picking up trash and moving it near a trashcan until the entire area (in this case, the beach shore) is clean and free of plastic.

## Requirements
+ Raspberry Pi 4B
+ Camera (5 MP or Higher)
+ L293D Module
+ Servomechanism Motor
+ Lithium Ion Battery
+ BO Motors
+ Chassis
+ Google Cloud Account


## Installation
Check out <a href = "https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up">this guide</a> to set up your Raspberry Pi.<br>
Raspberry Pi GPIO Library:
```
pip3 install RPi.GPIO
```
Raspberry Pi Camera Module:
```
pip3 install picamera
```
Google Cloud Libraries:
```
pip3 install google-cloud
```
```
pip3 install google
```
```
pip3 install google-cloud-vision`
```

## Future Scope

In the future, we are planning to upgrade our rover with a trash bin detection capability which will allow the garbage to be gathered near a dustbin/trashcan or put the trash inside that. We will also add a web portal to our project, which will allow us to control the rover in a semi-autonomous configuration. In the web portal, there will be buttons to allow the user to communicate with the rover. Further, we will be improving the architecture of the rover as well, so that it can pick up multiple trash at once, which will reduce the number of turns it has to take to reach the dustbin/trashcan, hence improving the rover's efficiency.

## Citations
https://cloud.google.com/vision/automl/object-detection/docs<br>
https://devpost.com/software/smartbin-qkcliw
