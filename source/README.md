# Prototype Submission for Video Analytics - by Team Trinity

## Steps to Run the code:

1. Clone this github repository using "git clone <name_of_the_repo.git>".

2. After cloning, get inside the main folder of the code repository. Download the weights from the links provided below and store them in the main working directory. Links:
  - https://github.com/swghosh/DeepFace/releases
  - https://github.com/patrick013/Object-Detection---Yolov3/blob/master/model/yolov3.weights

3. There are different files for each component (python files are named accordingly). With running these files using the command "python <filename.py>", one can see the output of the desired component.

4. We also have one python file named "sql_connect.py" which will be used to connect the SQL database and will also enter all the scanned activities through cctv camera feed inside the database with their necessary columns.
  
5. This data will be then visible to the Security Personnel and raise the alarm to alert everyone near the premises.


## Algorithms used and their applications in the prototype:

1. <ins>Anomaly Detection</ins>: A deep learning model based on the YOLOv3 algorithm that processes a video frame-by-frame to detect such anomalies in real-time and generate an alert for the concerned authorities.

2. <ins>Object Detection</ins>: A video based fire detection system using the YOLOv3 object detection model. The model was trained on a dataset of approximately 3000 images of fire in various contexts and additional augmented data. YOLOv3 achieved an AP of 89.5% on a test set consisting of fire in high risk and emergency situations and a 97% AP on a test set consisting of single flame images.

3. <ins>Face Detection</ins>: Face recognition is used to track down and identify known facilitators.  A facilitator detects miscreants, works on alarms triggered, and takes action on them.

4. <ins>Scene Detection</ins>: A module to detect any kind of tampering with the camera like focus settings,  alteration of video content, or concealing an object. The output of the module will provide the timestamp of the tampering.

5. <ins>Keypoint Detection</ins>: This module provides the count of people present in the frame at the moment. It also assigns an ID to each individual present in the frame.

6. <ins>Optical Character Recognition (OCR)</ins>: Time taken for activity on-premises can be calculated by extracting the timestamp present in the frame using OCR.

7. <ins>MySQL Database</ins>: Used for storing all the information obtained from different modules.
