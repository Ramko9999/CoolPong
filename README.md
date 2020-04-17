# CoolPong

# What is it
Pong, but you can control the paddles with your hands. 

# How does it work?
I utilized OpenCV for Computer Vision purposes. In order to detect the hand, there are several asumptions and events that must take place. First, the game must be calibrated to the background in order to take the difference between frames. Furthermore, greater pixel contrast between the hand and background will improve the performance for detecting the hand. Essentially, I am putting a threshold on the frame difference (I assume that the hand would be what is moving majority of the time). Then I find the largest contour of the tresholded frame, and then the convex hull. The convex hull, if all goes right, is the outer frame of the hand. Finally, I find center of the hand by taking average of the convex hull points and using the center relative to the game to move the paddle.
