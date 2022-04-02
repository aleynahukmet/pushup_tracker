# pushup_tracker

<p align="center"> 
   <img width="1000" height="400" alt="Ekran Resmi 2021-06-28 01 15 28" src="https://user-images.githubusercontent.com/87663976/161401522-9abfc07f-27d0-4755-ab44-eccce86465af.png">
</p>
In this project I will be doing pushup tracker using MediaPipe and OpenCV. I calculated the angle and wrote code to count the number of pushups. And I showed them on the screen to give the person a convenient feedback. 

# MediaPipe
Google open-source MediaPipe was first introduced in June, 2019. It aims to make our life easy by providing some integrated computer vision and machine learning features. Media Pipe is a framework for building multimodal(e.g video,audio or any time series data) applied ML pipelines.MediaPipe offers customizable Python solutions as a prebuilt Python package on PyPI, which can be installed simply with *pip install mediapipe*.  

# Pose Estimation Problem
Human pose estimation from video plays a critical role in various applications such as quantifying physical exercises, sign language recognition, and full-body gesture control. For example, it can form the basis for yoga, dance, and fitness applications. It can also enable the overlay of digital content and information on top of the physical world in augmented reality. 
MediaPipe Pose is a high-fidelity body pose tracking solution that renders 33 3D landmarks and a background segmentation mask on the whole body from RGB frames (Note RGB image frame).

<p align="center"> 
   <img width="1000" height="400" alt="Ekran Resmi 2021-06-28 01 15 28" src="https://user-images.githubusercontent.com/87663976/161401605-47774d04-4050-49c1-b6ff-cca552651950.png">
</p>

# Requirements
After we installed mediapipe and opencv we are importing our required libraries.

*import cv2*

*import mediapipe*

*import numpy*

