import os
import time

from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

from commands import *


def start_test(governor):
    connect()
    os.system(cmd_gov_set(0, governor))
    os.system(cmd_gov_set(7, governor))

    os.system(cmd_gfxinfo_reset())
    os.system(cmd_reset(0))
    os.system(cmd_reset(7))
    os.system(cmd_battery_stats_reset())
    return MonkeyRunner.waitForConnection()


def test_flappy(device, time_limit):
    # device.installPackage("apk/com-dotgears-flappybird.apk")

    package = "com.dotgears.flappybird"

    activity = "com.dotgears.flappy.SplashScreen"

    runComponent = package + "/" + activity

    w = int(device.getProperty("display.width"))
    h = int(device.getProperty("display.height"))

    MonkeyRunner.sleep(4)

    device.startActivity(component=runComponent)
    device.touch(w / 4, h / 1.48039, "DOWN_AND_UP")

    start_sec = time.time()
    current_sec = time.time()

    while current_sec - start_sec < time_limit:
        device.touch(w / 4, h / 1.48039, "DOWN_AND_UP")
        MonkeyRunner.sleep(0.6)
        current_sec = time.time()

    device.press('KEYCODE_HOME', MonkeyDevice.DOWN_AND_UP)
    kill_command = 'am force-stop %s' % package
    device.shell(kill_command)


def test_camera(device, time_limit):
    w = int(device.getProperty("display.width"))
    h = int(device.getProperty("display.height"))

    # device.installPackage("apk/Open_Camera_v1.48.1_apkpure.com.apk")

    package = "net.sourceforge.opencamera"

    activity = "net.sourceforge.opencamera.MainActivity"

    runComponent = package + "/" + activity

    device.startActivity(component=runComponent)
    MonkeyRunner.sleep(5)
    device.touch(2050, 550, "DOWN_AND_UP")
    MonkeyRunner.sleep(time_limit)
    device.touch(2050, 550, "DOWN_AND_UP")

    device.press('KEYCODE_HOME', MonkeyDevice.DOWN_AND_UP)
    kill_command = 'am force-stop %s' % package
    device.shell(kill_command)


def test_trial_xtreme(device, time_limit):
    # device.installPackage("apk/trial_xtreme_3_-1469689232-www.androeed.ru___.apk")

    package = "com.x3m.tx3"

    activity = "com.prime31.UnityPlayerProxyActivity"

    runComponent = package + "/" + activity

    device.startActivity(component=runComponent)
    MonkeyRunner.sleep(3)
    start_sec = time.time()
    current_sec = time.time()

    # play button
    device.touch(2000, 900, "DOWN_AND_UP")
    MonkeyRunner.sleep(3)
    # select location
    device.touch(700, 300, "DOWN_AND_UP")
    MonkeyRunner.sleep(3)
    # select bike
    device.touch(2000, 975, "DOWN_AND_UP")
    MonkeyRunner.sleep(3)
    # select level
    device.touch(1550, 350, "DOWN_AND_UP")
    MonkeyRunner.sleep(1.5)
    # start
    # device.touch(h/1.1325, w/1.18681, "DOWN_AND_UP")
    # MonkeyRunner.sleep(5)
    # play
    while current_sec - start_sec < time_limit:
        device.touch(1600, 900, "DOWN_AND_UP")
        device.touch(1935, 910, MonkeyDevice.DOWN)
        MonkeyRunner.sleep(10)
        device.touch(1600, 900, "DOWN_AND_UP")
        device.touch(1935, 910, MonkeyDevice.UP)
        # restart
        device.touch(1600, 900, "DOWN_AND_UP")
        MonkeyRunner.sleep(3)
        current_sec = time.time()

    device.press('KEYCODE_HOME', MonkeyDevice.DOWN_AND_UP)
    kill_command = 'am force-stop %s' % package
    device.shell(kill_command)


def test_pdf(device, time_limit):
    # device.installPackage("/home/user/dvfs_testing/mrScripts/apk/com.adobe.reader.apk")

    package = "com.adobe.reader"

    activity = "com.adobe.reader.AdobeReader"

    runComponent = package + "/" + activity

    device.startActivity(component=runComponent)
    MonkeyRunner.sleep(3)

    start_sec = time.time()
    current_sec = time.time()

    MonkeyRunner.sleep(5)

    device.touch(965, 210, "DOWN_AND_UP")

    device.touch(510, 1100, "DOWN_AND_UP")

    while current_sec - start_sec < time_limit:
        device.touch(1030, 1778, "DOWN_AND_UP")
        MonkeyRunner.sleep(3)
        current_sec = time.time()

    device.press('KEYCODE_HOME', MonkeyDevice.DOWN_AND_UP)
    kill_command = 'am force-stop %s' % package
    device.shell(kill_command)


def test_youtube_480(device, time_limit):
    package = "org.mozilla.firefox"

    activity = "org.mozilla.firefox.App"

    runComponent = package + "/" + activity

    device.startActivity(component=runComponent)
    MonkeyRunner.sleep(3)

    device.touch(500, 2150, "DOWN_AND_UP")

    MonkeyRunner.sleep(3)

    device.type("youtube.com")

    device.touch(1000, 2100, "DOWN_AND_UP")

    MonkeyRunner.sleep(3)

    device.touch(865, 173, "DOWN_AND_UP")

    MonkeyRunner.sleep(3)

    device.type("wild")

    MonkeyRunner.sleep(3)

    device.press('KEYCODE_SPACE', MonkeyDevice.DOWN_AND_UP)

    MonkeyRunner.sleep(3)

    device.type("animals")

    MonkeyRunner.sleep(3)

    device.press('KEYCODE_SPACE', MonkeyDevice.DOWN_AND_UP)

    MonkeyRunner.sleep(3)

    device.type("collection")

    MonkeyRunner.sleep(3)

    device.touch(1000, 2100, "DOWN_AND_UP")

    MonkeyRunner.sleep(2)

    device.touch(500, 500, "DOWN_AND_UP")

    MonkeyRunner.sleep(3)

    device.touch(1000, 288, "DOWN_AND_UP")

    MonkeyRunner.sleep(0.5)

    device.touch(1000, 288, "DOWN_AND_UP")

    MonkeyRunner.sleep(3)

    device.touch(300, 850, "DOWN_AND_UP")

    MonkeyRunner.sleep(3)

    device.touch(200, 1000, "DOWN_AND_UP")  # 200 730 for 1080

    MonkeyRunner.sleep(3)

    device.touch(840, 1500, "DOWN_AND_UP")

    MonkeyRunner.sleep(time_limit)

    MonkeyRunner.sleep(10)
    device.press('KEYCODE_HOME', MonkeyDevice.DOWN_AND_UP)
    kill_command = 'am force-stop %s' % package
    device.shell(kill_command)


def test_youtube_1080(device, time_limit):
    package = "org.mozilla.firefox"

    activity = "org.mozilla.firefox.App"

    runComponent = package + "/" + activity

    device.startActivity(component=runComponent)
    MonkeyRunner.sleep(3)

    device.touch(500, 2150, "DOWN_AND_UP")

    MonkeyRunner.sleep(3)

    device.type("youtube.com")

    device.touch(1000, 2100, "DOWN_AND_UP")

    MonkeyRunner.sleep(3)

    device.touch(865, 173, "DOWN_AND_UP")

    MonkeyRunner.sleep(3)

    device.type("wild")

    MonkeyRunner.sleep(3)

    device.press('KEYCODE_SPACE', MonkeyDevice.DOWN_AND_UP)

    MonkeyRunner.sleep(3)

    device.type("animals")

    MonkeyRunner.sleep(3)

    device.press('KEYCODE_SPACE', MonkeyDevice.DOWN_AND_UP)

    MonkeyRunner.sleep(3)

    device.type("collection")

    MonkeyRunner.sleep(3)

    device.touch(1000, 2100, "DOWN_AND_UP")

    MonkeyRunner.sleep(2)

    device.touch(500, 500, "DOWN_AND_UP")

    MonkeyRunner.sleep(3)

    device.touch(1000, 288, "DOWN_AND_UP")

    MonkeyRunner.sleep(0.5)

    device.touch(1000, 288, "DOWN_AND_UP")

    MonkeyRunner.sleep(3)

    device.touch(300, 850, "DOWN_AND_UP")

    MonkeyRunner.sleep(3)

    device.touch(200, 730, "DOWN_AND_UP")  # 200 730 for 1080

    MonkeyRunner.sleep(3)

    device.touch(840, 1500, "DOWN_AND_UP")

    MonkeyRunner.sleep(time_limit)

    MonkeyRunner.sleep(10)
    device.press('KEYCODE_HOME', MonkeyDevice.DOWN_AND_UP)
    kill_command = 'am force-stop %s' % package
    device.shell(kill_command)


def test_video(device, time_limit):
    os.system(cmd_video_playing())

    package = "org.videolan.vlc"

    MonkeyRunner.sleep(time_limit)

    device.press('KEYCODE_HOME', MonkeyDevice.DOWN_AND_UP)
    kill_command = 'am force-stop %s' % package
    device.shell(kill_command)


def test_typing(device, time_limit):
    package = "com.ogden.memo"

    activity = "com.ogden.memo.ui.MemoMain"

    runComponent = package + "/" + activity

    device.startActivity(component=runComponent)

    MonkeyRunner.sleep(3)
    device.touch(1047, 155, "DOWN_AND_UP")

    start_sec = time.time()
    current_sec = time.time()
    while current_sec - start_sec < time_limit:
        device.type("UTvjfEMLXa")
        current_sec = time.time()

    device.press('KEYCODE_HOME', MonkeyDevice.DOWN_AND_UP)
    kill_command = 'am force-stop %s' % package
    device.shell(kill_command)


def end_test():
    folder_name = "spsa2/test_trial_xtreme"

    os.system(cmd_dump_time(0, 0, folder_name))
    os.system(cmd_dump_time(7, 0, folder_name))


d = start_test("spsa2")
# test_flappy(d, 180)
# test_camera(d, 180)
# test_trial_xtreme(d,180)
# test_pdf(d, 180)
# test_typing(d, 180)
# end_test()
# os.system("adb shell \"su -c \'dmesg\'\" > log.txt")
