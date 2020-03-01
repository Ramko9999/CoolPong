import cv2
from hand import Hand, compute_center
import numpy as np
from game import Pong
import pygame
import sys
import math
from constants import *

MIN_AREA = 10
CALIBRATION_LIMIT = 30
CAMERA_HEIGHT = 480
CAMERA_WIDTH = 640
MIN_REACH = 175
MAX_REACH = 400
SCALE = 1

def main():

    # start video stream
    vid = cv2.VideoCapture(0)
    hand = Hand()
    game = Pong()
    cam_paddle = game.paddles[1]
    ai_paddle = game.paddles[0]
    SCALE = GAME_HEIGHT/(MAX_REACH - MIN_REACH)

    # variables used to figure out the static background for background subtraction
    aggregation_counter = 0
    background = np.zeros((CAMERA_HEIGHT,CAMERA_WIDTH))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    ai_paddle.move_up(15)
                if event.key == pygame.K_DOWN:
                    ai_paddle.move_down(15)

        ret, frame = vid.read()
        grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # aggregate background for some frames
        if aggregation_counter < CALIBRATION_LIMIT:
            background += grey_frame
            aggregation_counter += 1
        elif aggregation_counter == CALIBRATION_LIMIT:
            background = np.divide(background, CALIBRATION_LIMIT)
            aggregation_counter += 1
            print("Calibrated")
        else:
            # compute the absolute difference between our static background frame and our current frame
            delta_frame = cv2.absdiff(background.astype("uint8"), grey_frame)
            ret, df = cv2.threshold(delta_frame, 105, 255,cv2.THRESH_BINARY)

            # median blur for smoothness
            smooth_mask = cv2.medianBlur(df, 5)

            # finding contours
            contours, hierarchy = cv2.findContours(smooth_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            area = 0
            max_con = None
            for contour in contours:
                if cv2.contourArea(contour) > area:
                    max_con = contour
                    area = cv2.contourArea(contour)

            # find the convex hull of the largest contour
            if max_con is not None:
                hull = cv2.convexHull(max_con)

                # fetch new position and draw line in frame
                new_pos = compute_center(hull)
                new_pos[1] = math.floor((new_pos[1] - MIN_REACH) * SCALE)
                cam_paddle.set_position(new_pos)
                ai_paddle.set_position(new_pos)
                cv2.line(frame, tuple(hand.center_pos), tuple(new_pos), (0,255,0), 5)
                hand.set_hull(hull)

                # draw it in the normal frame
                cv2.drawContours(frame, [max_con], 0, (255, 0, 0))
                cv2.drawContours(frame, [hull],0, (0,0,255))

            cv2.imshow("Regular Frame", frame)
            hand.set_frame(grey_frame)
            game.update()
            if cv2.waitKey(1) == ord("r"):
                break

    vid.release()
    vid.destroyAllWindows()

main()