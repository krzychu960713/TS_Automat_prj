from commands.moves import move_j
import numpy as np

def addPoint(robot, path, start, stop):

    middle = [stop[0], start[1], start[2],
              start[3], start[4], start[5]]
    # middle = [stop[0], start[1], 0., 0., 0., 0.]
    path1 = move_j(robot, start, middle)
    path2 = move_j(robot, middle, stop)

    path = np.concatenate((path, path1, path2), axis=0)

    return path

def moveA(robot, path, start):

    stop = [180.0, 90.0, 0.0, 0.0, 0.0, start[5]]
    path = addPoint(robot, path, start, stop)
    return stop, path

def takeA(robot, path, start):

    stop = [180.0, 120.0, 30.0, 0.0, 0.0, 90.0]
    path = addPoint(robot, path, start, stop)
    return stop, path

def moveB(robot, path, start):

    stop = [240.0, 90.0, 0.0, 0.0, 0.0, start[5]]
    path = addPoint(robot, path, start, stop)
    return stop, path

def takeB(robot, path, start):

    stop = [240.0, 120.0, 30.0, 0.0, 0.0, 90.0]
    path = addPoint(robot, path, start, stop)
    return stop, path


def init(robot, path):
    start = [90.0, 90.0, 0.0, 0.0, 0.0, 0.0]
    path1 = move_j(robot, start, start)
    path = np.concatenate((path1), axis=0)
    return start, path

def moveSt(robot, path, start):

    stop = [90.0, 90.0, 0.0, 0.0, 0.0, start[5]]
    path = addPoint(robot, path, start, stop)
    return stop, path

def getSt(robot, path, start):

    stop = [90.0, 120.0, 30.0, 0.0, 0.0, 0.0]
    path = addPoint(robot, path, start, stop)
    return stop, path

def moveAr(robot, path, start):

    stop = [00.0, 90.0, 0.0, 0.0, 0.0, 0.0]
    path = addPoint(robot, path, start, stop)
    return stop, path

def takeAr(robot, path, start):

    stop = [00.0, 180.0, -90.0, 0.0, 90.0, 7200.0]
    path = addPoint(robot, path, start, stop)
    return stop, path

