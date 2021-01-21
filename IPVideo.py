'''                            _____________                   ____              ____
        /\        /\          /             |                 |    |            |    |
       /  \      /  \        |     ____     |                 |    |____________|    |
      /    \    /    \       |    |    |    |               __|   __            __   |__ 
     /      \  /      \      |    |____|    |            __|     |  |          |  |     |__
    /    /\  \/  /\    \     |           ___/           |        |__|          |__|        |
   /    /  \    /  \    \    |    |\    \               |__     __                __     __|
  /    /    \  /    \    \   |    | \    \      ____       |__ |_ |______________| _| __|
 /    /      \/      \    \  |    |  \    \    |    |         |  |________________|  |
/____/                \____\ |____|   \____\   |____|         |______________________|
Created By Adrian Thaddeus Smith
'''
# CANNOT RUN UNTIL OPENCV IS INSTALLED


import cv2, time, numpy, threading

class CameraStream:
    def __init__(self, src=0, resolution=(640,360)):
        self.stream = cv2.VideoCapture(src)
        self.stream.set(3,resolution[0])
        self.stream.set(4,resolution[1])
        (self.grabbed, self.frame) = self.stream.read()
        self.stopped = False
        self.start()
        time.sleep(1.0)

    def start(self):
        self.updateFrameThread = threading.Thread(target=self.updateFrame)
        self.updateFrameThread.daemon = True
        self.updateFrameThread.start()
        return self

    def updateFrame(self):
        while True:
            if self.stopped: return
            (self.grabbed, self.frame) = self.stream.read()

    def read(self):	return self.frame
    def stop(self): self.stopped = True

if __name__ == '__main__':
    cam = CameraStream()
    while True:
        img = cam.frame
        cv2.imshow('Yeet', img)
        cv2.waitKey(10)
