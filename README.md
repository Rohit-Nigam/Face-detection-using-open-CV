# Face-detection-using-open-CV

This Python script performs **real-time face detection** using your webcam. It utilizes OpenCV’s built-in **Haar Cascade Classifier** to detect human faces and draw rectangles around them in a video stream.

---

## 📷 Features

- ✅ Real-time face detection from webcam
- 🧠 Uses Haarcascade XML for frontal face detection
- 🔲 Draws bounding boxes around detected faces
- 💻 Press **'d'** to exit the live feed

---

## 🛠️ Technologies Used

- **Python 3**
- **OpenCV (cv2)**
- Haar Cascade XML Classifier

---

## ▶️ How to Run

1. Make sure OpenCV is installed:
    ```bash
    pip install opencv-python
    ```

2. Download the Haar Cascade file:
    - Get `haarcascade_frontalface_default.xml` from [OpenCV GitHub](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml)
    - Place it in the same directory as your script.

3. Save the code to a file, e.g., `face_detection.py`.

4. Run the script:
    ```bash
    python face_detection.py
    ```

---

## 🧠 How It Works

- Captures video from the system’s default webcam (`cv2.VideoCapture(0)`)
- Converts each frame to grayscale
- Detects faces using Haar Cascades
- Draws rectangles around detected faces
- Closes the window when you press **"d"**

---

## 📌 Future Enhancements

- [ ] Add smile or eye detection
- [ ] Improve performance using DNN face detectors
- [ ] Record or save detected face images
- [ ] Integrate with GUI using PyQt5 or Tkinter

---

