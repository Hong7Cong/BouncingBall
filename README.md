# BouncingBall
This code generates and save a video of a ball bouncing across the screen. 

## How to run the code

**Step 1: Generate generates and saves a video (.avi file) of a ball bouncing across the screen**
```
python generate_ball.py [-h] [--color COLOR] [--length LENGTH] [--acceleration ACCELERATION] [--height HEIGHT] [--width WIDTH] 
```
Examples:
To use the default setting, run:
```
python generate_ball.py
```
To customize, run:
```
python generate_ball.py -c 255 0 0 -l 25 -a 1 -t 680 -w 1040
```

**Step 2: Detect ball in video**
```
python detect_ball.py
```

## Physics Assumptions/simplifications made:
The ball will be drop or throw to a box, it will bouncing until it will stop because of gravity. Moreover, I assuming that there is no friction force, which mean, when the ball stay on ground and not is bouncing anymore, it will continue move left and right with velocity vx.
![This is an image](equation_of_motion.png)
## Some notes and expected failures:

BUGs in platform of VScode-Windown Sub-System for Linux (WSL): Un-consistent key pressing. Because of this bugs, this code will not implement the feature "press q to quit while program on running". The only to quit is press Ctrl + C dirrectly to terminal.
https://stackoverflow.com/questions/46968099/cv2-waitkey-returns-255-for-all-keys