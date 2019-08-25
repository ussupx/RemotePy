import sys
import cv2
import numpy as np 
import pyautogui
if sys.platform == 'linux':
    import pyscreenshot as ImageGrab
else:
    from PIL import ImageGrab
from PIL import ImageDraw,Image
from base_camera import BaseCamera

import mss
sct=mss.mss()
import win32gui
import pygetwindow as gw
import win32con
class Camera(BaseCamera):

    @staticmethod
    def frames():
        while True:
            # capture computer screen

            # draw mouse pointer

            k = gw.getWindowsWithTitle('Mozilla Firefox')
            HWND = k[0]._hWnd
            if not k[0].isActive:

                win32gui.ShowWindow(HWND, win32con.SW_RESTORE)
                win32gui.SetWindowPos(HWND, win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)
                win32gui.SetWindowPos(HWND, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)
                win32gui.SetWindowPos(HWND, win32con.HWND_NOTOPMOST, 0, 0, 0, 0,
                                      win32con.SWP_SHOWWINDOW + win32con.SWP_NOMOVE + win32con.SWP_NOSIZE)

            monitor = {"top": k[0].top, "left": k[0].left, "width": k[0].width, "height": k[0].height}

            img = sct.grab(monitor)
            img = Image.frombytes("RGB", img.size, img.rgb)

            #img = Camera.draw_mouse(img)

            # convert image to numpy array
            #img_np = np.array(img)
            # convert color space from BGR to RGB
            #frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
            # convert image to jpg format
            ret, jpeg = cv2.imencode('.jpg', img)
            yield jpeg.tobytes()


    @staticmethod
    def draw_mouse(img):
        """
        utility function to draw mouse pointer
        """
        # generate Draw object for PIL image
        draw = ImageDraw.Draw(img)
        # find current position of mouse pointer
        pos = pyautogui.position()
        # coordinates of ellipse
        ax, ay, bx, by = pos[0], pos[1], pos[0]+10, pos[1]+10
        # draw ellipse on image
        draw.ellipse((ax,ay,bx,by), fill="yellow")
        return img
