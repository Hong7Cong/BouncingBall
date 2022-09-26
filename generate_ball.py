import cv2
import numpy as np
import argparse
import time


class BouncingBall():
    def __init__(self, vx=2, vy=4, gravity=1):
        # Coordinates of the ball
        self.x = 200
        self.y = 200
        # Direction of the ball
        self.dx = 1 # (>0:go down, <0:go up)
        self.dy = 1 # (>0:go right, <0:go left)
        # Velocity of the ball
        self.vx = vx 
        self.vy = vy
        self.gravity = gravity
        self.bg_height = 680
        self.bg_width  = 1040
        
    def get_xy(self):
        return (self.x, self.y)
    
    def update_xy(self):
        self.vy = self.vy + self.dy * self.gravity
        if(self.vy == 0):
            self.dy *= -1
        self.x = self.x + self.dx * self.vx
        self.y = self.y + self.dy * int(abs(self.vy))

    
    def CheckifInsideScreen(self):
        if self.y >= self.bg_height-20:
            self.y = self.bg_height-20
            self.dy = -1*self.dy
        elif self.y <= 0+20:
            self.y = 0+20
            self.dy = -1*self.dy

        if self.x >= self.bg_width-20:
            self.x = self.bg_width-20
            self.dx = -1*self.dx
        elif self.x <= 0+20:
            self.x = 0+20
            self.dx = -1*self.dx
            
    def CheckStop(self):
        if(self.y == self.bg_height-20 and self.vy == 0):
            self.dy = 0
            
            # if(self.vx > 0):
            #     self.vx -= 1 
    

def main(args):
    # Init paramters
    print(args)
    gravity         = args.acceleration
    video_length    = args.length
    bg_height       = args.height
    bg_width        = args.width
    bg_shape        = (bg_height, bg_width, 3)
    color           = (args.color[0], args.color[1], args.color[2])
    ball1           = BouncingBall(args.vx, args.vy, gravity)
    background_img  = np.zeros(bg_shape, dtype='uint8')
    fourcc          = cv2.VideoWriter_fourcc('M','J','P','G')
    fps             = 30
    video_filename  = 'output.avi'
    out             = cv2.VideoWriter(video_filename, fourcc, fps, (bg_width, bg_height))
    start_time      = time.time()
    
    while (time.time() - start_time < video_length):
        # Display the image
        cv2.imshow('Display and Refresh the background image', background_img)
        key = cv2.waitKey(20) & 0xFF # Wait for 20 ms
        background_img = np.zeros(bg_shape, dtype='uint8') 
        ball1.update_xy()
        # print("y = ", ball1.y, " vy = ", ball1.vy, " dy = ", ball1.dy)
        # create a ball shape
        # cv2.ellipse(background_img, ball1.get_xy(), (20, 15), 0, 0, 360, (100,100,0), -1)
        cv2.circle(background_img, ball1.get_xy(), 20, color, -1)
        # print(key)
        ball1.CheckifInsideScreen()
        ball1.CheckStop()
        out.write(background_img)
        # key = cv2.waitKey(1) & 0xFF
        # if the 'q' key is pressed, stop the loop
        # if key == ord("d"):
        #     break
    out.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-c', '--color', nargs='+', help='<Required> Set flag', required=False, type=int, default=[100, 100, 0])
    parser.add_argument('--vx', default=3, type=int, help='Length of video in seconds')
    parser.add_argument('--vy', default=4, type=int, help='Length of video in seconds')
    parser.add_argument('-l', '--length', action='store', default=30, type=int, help='Length of video in seconds')
    parser.add_argument('-a', '--acceleration', action='store', default=1, type=int, help='Acceleration due to gravity with operational range 1 to 10')
    parser.add_argument('-t','--height', action='store', default=680, type=int, help='Resolution of video: height')
    parser.add_argument('-w','--width', action='store', default=1049, type=int, help='Resolution of video: width')                   
    args = parser.parse_args()
    
    main(args)


