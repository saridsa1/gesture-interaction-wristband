import sys
import os.path
sys.path.append(os.path.abspath(__file__ + "/../.."))
from input.processor import Processor
from input.reader import AsyncReader
from scanner.Gestures import Gestures
from scanner.GestureScanner import GestureScanner
import time

def process_input(in_stream):
    if not dataProcessor.put_raw(in_stream):
        return

    gesture_id = gestureScanner.check_for_gesture(dataProcessor.get_flat_buffer())
    print str(gestureScanner.gestureProba(dataProcessor.get_flat_buffer()))

    # todo pass gesture to dashboard
    # todo track when last gesture was done and only pass this one on if there is enough time in between (~1sec)
    if gesture_id == Gestures.SWIPE_LEFT:
        print "Left swipe recognized"
        pass
    elif gesture_id == Gestures.SWIPE_RIGHT:
        print "Right swipe recognized"
        pass

# init gesture scanning
gestureScanner = GestureScanner("../input/raw/sensor_data.csv")

# handle data input of the sensor
dataProcessor = Processor.DataProcessor()
ar = AsyncReader.StdinReader(0, "reader", process_input)
ar.start()

# keep this process alive until ctrl-d is pressed. This can be removed when we add the tkinter dashboard
while(True):
    time.sleep(1)
