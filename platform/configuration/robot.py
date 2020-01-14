""" Конфигурация робота """
from edubot import EduBot, MotorMode
import smbus

servoPosLen = 255
middleServoPos = int(servoPosLen / 2)

bus = smbus.SMBus(1)
robot = EduBot(bus)


def move(speed):
    robot.setParrot0(int(-speed))
    robot.setParrot1(int(speed))


def rotate(speed):
    robot.setParrot0(int(speed))
    robot.setParrot1(int(speed))


def setCamera(scale):
    scale = min(max(-1, scale), 1)
    robot.beep()
    robot.setServo0(int(middleServoPos - scale*servoPosLen))


def initializeAll():
    robot.online = True
    robot.start()
    robot.setMotorMode(MotorMode.MOTOR_MODE_PID)
    robot.setParrot0(0)
    robot.setParrot1(0)
    robot.setServo0(int(middleServoPos))
    robot.setServo1(int(middleServoPos))


def release():
    robot.exit()
