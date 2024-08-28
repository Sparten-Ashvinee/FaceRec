# Face recognition and detection

### Introduction
This project focuses on implementing advanced face recognition and detection techniques. For face detection, we utilize YOLO, an optimized version of YOLO designed for high-performance inference on edge devices. For face recognition, we employ FaceNet, a robust model renowned for generating high-quality face embeddings, which enables precise identification and verification.

### Rquirement
  * python
  * keras
  * sklearn
  * azureml
  * keras_vggface

### Dataset
The dataset consists of Indian face images collected from IEEE, ensuring diversity in terms of age, gender, ethnicity, and lighting conditions. The LFW dataset are added among this to increase the amount of the dataset.

### Preprocessing
Face Detection Preprocessing: Resize and normalize images to meet the input requirements of the YOLO model.
Face Recognition Preprocessing: Align and crop faces detected by YOLO, then resize and normalize them for embedding extraction by FaceNet. Images are meticulously pre-processed for alignment and resizing using MXNet to ensure consistency and accuracy.

### Training and evaluation 
Face Detection:
Train the YOLO model using labeled face images to achieve accurate face detection.
Evaluate detection performance with metrics such as precision, recall, and mean average precision (mAP).
Face Recognition:
Train the FaceNet model using embeddings generated from the detected faces.
Assess recognition performance using metrics such as accuracy, precision, recall, and F1-score.

Triplet Loss is a commonly used loss function in face recognition tasks to improve the model's ability to differentiate between similar and dissimilar faces. Below is an explanation and illustration of how Triplet Loss functions in the context of person identification.
<a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"></a>
<img src="https://github.com/user-attachments/assets/3b479405-90bf-43ff-8498-5dce10b4e1d4" align="left" width="300">
<img src="https://github.com/user-attachments/assets/91a4eb12-7829-4bc7-8a63-b0bb151d0c67" align="left" width="300">
<a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"><img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif"></a>
### Optimization
Conducted model optimization to improve performance and efficiency, ensuring enhanced accuracy and faster inference times. Quantized the model generating a perfectly optimized model for deployment on the Nvidia Jetson Nano edge devices. This model is deployed industrially for facial recognition-based attendance and safety compliance monitoring.

### Deployment
We are developing a web inference system for testing, available at [Ashvinee.xyz](https://www.ashvinee.xyz/coming-soon-02). Also deployment industrially on the Nvidia Jetson Nano edge devices for facial recognition-based attendance and safety compliance monitoring.

### Resources
  * [FaceNet](https://github.com/davidsandberg/facenet)
  * [arcface-pytorch](https://github.com/ronghuaiyang/arcface-pytorch)
  * [SphereFace](https://github.com/wy1iu/sphereface)
  * [Insightface](https://github.com/deepinsight/insightface)
