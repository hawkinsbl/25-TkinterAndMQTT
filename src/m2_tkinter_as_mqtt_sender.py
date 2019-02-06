"""
Using a fake robot as the receiver of messages.
"""

# Done: 1. In mqtt_remote_method_calls, set LEGO_NUMBER at line 131
# to YOUR robot's number.

# Done: 2. Copy your Tkinter/ttk ROBOT gui code from the previous session (m6).
# Then modify it so that pressing a button sends a message to a teammate
# of the form:
#   (for Forward)
#        ["forward", X, y]
#   where X and Y are from the entry box.
#
# Implement and test.

import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com
import time


def main():
    name1 = input("Enter one name (subscriber): ")
    name2 = input("Enter another name (publisher): ")

    mqtt_client = com.MqttClient()
    mqtt_client.connect(name1, name2)
    time.sleep(1)  # Time to allow the MQTT setup.
    print()

    root = tkinter.Tk()
    root.title("MQTT Remote")

    main_frame = ttk.Frame(root, padding=20)
    main_frame.grid()  # only grid call that does NOT need a row and column

    left_speed_label = ttk.Label(main_frame, text="Left")
    left_speed_label.grid()
    left_speed_entry = ttk.Entry(main_frame, width=8)
    left_speed_entry.insert(0, "600")
    left_speed_entry.grid(row=1, column=0)

    right_speed_label = ttk.Label(main_frame, text="Right")
    right_speed_label.grid(row=0, column=2)
    right_speed_entry = ttk.Entry(main_frame, width=8, justify=tkinter.RIGHT)
    right_speed_entry.insert(0, "600")
    right_speed_entry.grid(row=1, column=2)

    forward_button = ttk.Button(main_frame, text="Forward")
    forward_button.grid(row=2, column=1)
    forward_button['command'] = lambda: mqtt_client.send_message('forward', getspeeds(left_speed_entry, right_speed_entry))
    root.bind('<Up>', lambda event: print("Forward key"))

    left_button = ttk.Button(main_frame, text="Left")
    left_button.grid(row=5, column=0)
    left_button['command'] = lambda: print("Left button")
    root.bind('<Left>', lambda event: print("Left key"))

    stop_button = ttk.Button(main_frame, text="Stop")
    stop_button.grid(row=5, column=1)
    stop_button['command'] = lambda: print("Stop button")
    root.bind('<space>', lambda event: print("Stop key"))

    right_button = ttk.Button(main_frame, text="Right")
    right_button.grid(row=5, column=2)
    right_button['command'] = lambda: print("Right button")
    root.bind('<Right>', lambda event: print("Right key"))

    back_button = ttk.Button(main_frame, text="Back")
    back_button.grid(row=7, column=0)
    back_button['command'] = lambda: print("Back button")
    root.bind('<Down>', lambda event: print("Back key"))

    up_button = ttk.Button(main_frame, text="Up")
    up_button.grid(row=4, column=1)
    up_button['command'] = lambda: print("Up button")
    root.bind('<u>', lambda event: print("Up key"))

    down_button = ttk.Button(main_frame, text="Down")
    down_button.grid(row=6, column=1)
    down_button['command'] = lambda: print("Down button")
    root.bind('<j>', lambda event: print("Down key"))

    # Buttons for quit and exit
    q_button = ttk.Button(main_frame, text="Quit")
    q_button.grid(row=7, column=2)
    q_button['command'] = lambda: print("Quit button")

    e_button = ttk.Button(main_frame, text="Exit")
    e_button.grid(row=8, column=1)
    e_button['command'] = lambda: exit()

    root.mainloop()


def getspeeds(entry1, entry2):
    lspeed = entry1.get()
    rspeed = entry2.get()
    speeds = [lspeed, rspeed]
    return speeds


def sendforward(lentry, rentry):
    lspeed = getspeeds(lentry)
    rspeed = getspeeds(rentry)

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
