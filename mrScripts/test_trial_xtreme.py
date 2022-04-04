from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import time
import os
import sys
from commands import *

curr_governor = sys.argv[2]
os.system(cmd_gov_set(0, curr_governor))
os.system(cmd_gov_set(7, curr_governor))

device = MonkeyRunner.waitForConnection()

device.installPackage("apk/trial_xtreme_3_-1469689232-www.androeed.ru___.apk")

package = "com.x3m.tx3"

activity = "com.prime31.UnityPlayerProxyActivity"

runComponent = package + "/" + activity

w = int(device.getProperty("display.width"))
h = int(device.getProperty("display.height"))

folder_name =  "spsa2/test_trial_xtreme"

test_count = int(sys.argv[1])

time_limit = 150  # 300

connect()

for test_i in range(test_count):

    MonkeyRunner.sleep(4)
    os.system(cmd_gfxinfo_reset())

    os.system(cmd_reset(0))
    os.system(cmd_reset(7))
    os.system(cmd_battery_stats_reset())

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

    os.system(cmd_dump_time(0, test_i, folder_name))
    os.system(cmd_dump_time(7, test_i, folder_name))
    os.system(cmd_dump_trans(0, test_i, folder_name))
    os.system(cmd_dump_trans(7, test_i, folder_name))
    os.system(cmd_gfxinfo_dump(package, test_i, folder_name))

    os.system(cmd_battery_stats_dump(package, test_i, folder_name))

    device.press('KEYCODE_HOME', MonkeyDevice.DOWN_AND_UP)
    kill_command = 'am force-stop %s' % package
    device.shell(kill_command)
