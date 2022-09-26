# BouncingBall

## How to run the code

**Step 1: Generate ball video**

```
python generate_ball.py [-h] [--color COLOR] [--length LENGTH] [--acceleration ACCELERATION] [--height HEIGHT] [--width WIDTH] 
```
Example:
```
python generate_ball.py
or
python generate_ball.py -c 255 0 0 -l 25 -a 1 -t 680 -w 1040
```

**Step 2: Detect ball in video**


## Some notes and expected failures:

BUGs in platform of VScode-Windown Sub-System for Linux (WSL): Un-consistent key pressing. Because of this bugs, this code will not implement the feature "press q to quit while program on running". The only to quit is press Ctrl + C dirrectly to terminal.
https://stackoverflow.com/questions/46968099/cv2-waitkey-returns-255-for-all-keys