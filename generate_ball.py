'''
This file generates and saves a video (.avi file) of a ball bouncing across the screen.

usage: 
    generate_ball.py [-h] [-c COLOR [COLOR ...]] [--vx VX] [--vy VY] [-l LENGTH] [-a ACCELERATION] [-t HEIGHT] [-w WIDTH]

options:
  -h, --help            show this help message and exit
  -c COLOR [COLOR ...], --color COLOR [COLOR ...]
                        <Required> Set flag
  --vx VX               Length of video in seconds
  --vy VY               Length of video in seconds
  -l LENGTH, --length LENGTH
                        Length of video in seconds
  -a ACCELERATION, --acceleration ACCELERATION
                        Acceleration due to gravity with operational range 1 to 10
  -t HEIGHT, --height HEIGHT
                        Resolution of video: height
  -w WIDTH, --width WIDTH
                        Resolution of video: width
'''

import cv2
import numpy as np
import argparse
import time


class BouncingBall():
    """An Bouncing Ball Object.

    Attributes:
        vx (int):           Initial Velocity of horizontal direction.
        vy (int):           Initial Velocity of vertical direction.
        gravity (int):      Accelarator by gravity.
        bg_height (int):    Height of screen in pixels.
        bg_width (int):     Width of screen in pixels

    """
    def __init__(self, vx=2, vy=4, gravity=1, bg_height=680, bg_width=1040):
        # Coordinates of the ball
        self.x = 200
        self.y = 200
        # Direction of the ball
        self.dx = 1 
        self.dy = 1 
        # Velocity of the ball
        self.vx = vx 
        self.vy = vy
        self.gravity = gravity
        self.bg_height = bg_height
        self.bg_width  = bg_width
        
    def get_xy(self):
        """Get the current cordination of the ball.

        Args: None

        Returns: (x, y)

        """
        return (self.x, self.y)
    
    def update_xy(self):
        """Update the cordination of the ball after 20ms.
        
        Args: None
        
        Returns: None
        
        """
        self.vy = self.vy + self.dy * self.gravity
        if(self.vy == 0):
            self.dy *= -1
        self.x = self.x + self.dx * self.vx
        self.y = self.y + self.dy * int(abs(self.vy))

    
    def CheckifInsideScreen(self):
        """Check border conditions.
        
        If the ball out of screen border then change the moving direction back the the screen
        
        Args: None
        
        Returns: None
        
        """
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
        """Check if the vertical velocity is zero (whether the ball moving up and down anymore)
        
        Args: None
        
        Returns: True if the ball is stop moving up and down
        
        """
        if(self.y == self.bg_height-20 and self.vy == 0):
            self.dy = 0
            return True
        return False

def main(args):
    # Init paramtters
    print(args)
    gravity         = args.acceleration
    video_length    = args.length
    bg_height       = args.height # Background height
    bg_width        = args.width  # Background width
    bg_shape        = (bg_height, bg_width, 3)
    color           = (args.color[0], args.color[1], args.color[2]) 
    ball1           = BouncingBall(args.vx, args.vy, gravity)
    background_img  = np.zeros(bg_shape, dtype='uint8')
    start_time      = time.time()
    
    # Create video-reading object
    fourcc          = cv2.VideoWriter_fourcc('M','J','P','G')
    fps             = 30
    video_filename  = 'output.avi'
    out             = cv2.VideoWriter(video_filename, fourcc, fps, (bg_width, bg_height))

    # Display the video frame by frame
    while (time.time() - start_time < video_length):
        # Display frames
        cv2.imshow('Display and Refresh the background image', background_img)
        key = cv2.waitKey(20) & 0xFF # Wait for 20 ms
        background_img = np.zeros(bg_shape, dtype='uint8') 
        ball1.update_xy()

        # Draw a ball on the background image
        cv2.circle(background_img, ball1.get_xy(), 20, color, -1)
        
        # Check falling conditions
        ball1.CheckifInsideScreen()
        ball1.CheckStop()
        out.write(background_img)
    
    # Save .avi video   
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


