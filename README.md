# Capstone-Project-UPTP-1
**Cable Insertion
Project Overview**
This capstone project focuses on enhancing industrial robot self-awareness through computer vision, motion monitoring

The proposed system aims to monitor repetitive industrial robotic operations, learn normal motion patterns, identify abnormal behavior, and explore potential corrective strategies to improve manufacturing reliability, precision, and autonomy.
The experimental platform is based on an ABB IRB 1090 industrial robot at the National Taiwan University of Science and Technology (NTUST).

**Main Objectives**
-Develop a vision-based industrial robot motion monitoring system.
-Extract relevant spatial and temporal features from RGB images.
-Create a structured dataset of normal and abnormal robotic operations.
-Implement and compare statistical and machine learning anomaly detection methods.
-Evaluate robot positioning accuracy and motion repeatability.
-Explore real-time anomaly detection through Edge AI deployment.
-Investigate feedback mechanisms for potential robotic self-correction.

**System Architecture**
The proposed system integrates three main components:

1. Industrial Robot and Control
-ABB IRB 1090 industrial robot.
-ABB RobotStudio and RAPID programming.
-Robot calibration and coordinate system definition.
-TCP, tooldata, loaddata, and workobject configuration.
-Motion execution and communication with external systems.

2. RGB Computer Vision
-Cognex industrial vision cameras.
-Camera calibration and image acquisition.
-Region of interest (ROI) definition.
-Object and robot motion tracking.
-Position and orientation estimation.
-OpenCV-based image processing.
-Visual feature extraction and dataset generation.

3. Edge AI and Anomaly Detection
-Normal motion pattern learning.
-Statistical anomaly detection.
-Machine learning-based anomaly classification.
-Temporal motion analysis.
-Edge computing implementation.
-Real-time performance evaluation.
-Communication of detected anomalies to the robotic control system.

**Proposed Workflow**
-Robot motion execution.
-RGB image acquisition.
-Image preprocessing and feature extraction.
-Motion dataset generation.
-Normal behavior modeling.
-Anomaly detection.
-Decision-making and potential corrective feedback.
