from picamera2 import Picamera2, Preview
import time
import datetime

def main():
    try:
        picam2 = Picamera2()
        camera_config = picam2.create_still_configuration(main={"size": (1280, 720)}, lores={"size": (640, 480)}, display="lores")
        picam2.configure(camera_config)
        picam2.start()
        print("Starting Camera...")
        time.sleep(2)
        picam2.capture_file("./image/mannualImage.jpg")
        print("Image Captured Successfully !!")
        picam2.stop_preview()
        picam2.stop()
        print("Stopping Camera...")
        current_time = datetime.datetime.now()
        time_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
        with open('./time.txt', 'w') as f:
            f.write(time_str)
        return True
    except:
        print("Camera not found or could not be initialized.")
        return False
