# -*- coding: utf-8 -*-
# utils/cam_detect.py
# Detect available cameras on the system
# and take a snapshot of all available cameras
import cv2
from PIL import Image

"""
Callable: opencv_to_pil
Arg: image (numpy.ndarray)
Return: Image (PIL.Image)

Converts an OpenCV image to a PIL image
"""
opencv_to_pil = lambda image: Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))


def take_snapshot(camera_id):
    cap = cv2.VideoCapture(camera_id)
    _, frame = cap.read()
    cap.release()
    return frame


def list_available_cameras(max_cameras=10):
    """
    Return a list of available cameras on the system
    """
    available_cameras = []
    for index in range(max_cameras):
        cap = cv2.VideoCapture(index)
        if cap.isOpened():
            available_cameras.append(index)
            cap.release()
    return available_cameras


def main():
    cameras = list_available_cameras()
    print("[INFO] Available cameras:", cameras)
    for camera in cameras:
        # Traverse and take a snapshot of all available cameras
        snapshot = take_snapshot(camera)
        pil_img = opencv_to_pil(snapshot)
        pil_img.show()


if __name__ == "__main__":
    main()
