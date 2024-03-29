import cv2
from base_camera import BaseCamera


class Camera(BaseCamera):
    video_source = 2

    @staticmethod
    def set_video_source(source):
        Camera.video_source = source

    @staticmethod
    def frames():
        camera = cv2.VideoCapture(Camera.video_source)
        if not camera.isOpened():
            raise RuntimeError('Could not start camera.')

        while True:
            # read current frame
            _, img = camera.read()
            img = cv2.resize(img, (4096, 2048))

            # encode as a jpeg image and return it
            yield cv2.imencode('.jpg', img)[1].tobytes()
