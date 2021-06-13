# Beach, please

#Inspiration

When we picture ourselves at the seaside on vacation, we imagine a clean seashore with clear water. But in reality, it is never the case because marine pollution has become one of the biggest concerns of humankind at present. Thanks to the negligence of our fellow human beings, most beaches of Earth are littered with plastic, and non-biodegradable trash, which eventually reaches the sea/ocean water and adversely affects the marine ecosystem as well. This inspired us to build something that can help in restoring the beaches to their original clean and beautiful form.

#What it does

The automated smart rover built by us moves around the beach to identify and pick up trash. The wheels of the rover are potent enough to move across dry as well as wet sand. The camera of the Raspberry pi 4 used in this rover takes an image of the material, and then it sends that image to Google Cloud. With the help of Google's CloudVision API, it identifies what is there in the image and returns it to my client. Depending upon the type of that object, the program classifies it as either trash or not. If the object gets identified as trash, then the rover picks it up, moves, and gathers them to a specific corner away from the seashore, making it easy for the garbage collector to collect the whole trash of the site at once. And the rover keeps repeating the process of picking up trash and moving it near a trashcan until the entire area (in this case, the beach shore) is clean and free of plastic.

#How we built it

The heart of the rover is the Raspberry pi 4, and along with it, we are using the RPI cam. We have used two motors for the movement, and for the picking mechanism, we used a micro servo motor. We needed a Motor Driver to drive the motors, and we used an l293d for that. With the help of Google Cloud Vision Object Detection API and some python code for driving the motor driver, we merged both the API code for the object detection and the robot's movement. Next, we calibrated the rover with threshold values, say for the movement or tuning the triggering of the servo.

#Challenges we ran into

One of the mentionable challenges faced while building the project was that it was our first time interfacing the l293d motor driver with the Raspberry pi. Then configuring the servo with the R-pi and making it work correctly was another hurdle we had to overcome. Merging the API code with the main code was a bit tricky. And finally, some troubleshooting and bug fixing was also nerve-wracking for sure.

#Accomplishment we are proud of

Driving the l293d Motor Driver and the Servo Motor with the Raspberry pi was an accomplishment in itself. Being able to make the object detection API work correctly so that it could identify trash was something that we are very proud of doing. One of the most celebratory moments for us was watching the bot working correctly upon merging the Object Detection API with the main Driver Code. 

#What's next for Beach, please

In the future, we are planning to upgrade our rover with a trash bin detection capability which will allow the garbage to be gathered near a dustbin/trashcan or put the trash inside that. We will also improve the architecture of the rover so that it can pick up multiple trash at once, which will reduce the number of turns it has to take to reach the dustbin/trashcan, and hence it will improve the rover's efficiency. 
