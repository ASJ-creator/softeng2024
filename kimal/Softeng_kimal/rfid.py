#!/usr/bin/env python3
# -*- coding: utf8 -*-

import MFRC522
import signal
import time

# Flag to control the reading loop
continue_reading = True

# Capture SIGINT signal to allow graceful exit when the script is interrupted
def end_read(signal, frame):
    global continue_reading
    print("\nCtrl+C captured, ending read operation.")
    continue_reading = False

def get_uid():
    '''
    blue tag: F2EA4403
    white card: B5972902
    '''
    # Bind the SIGINT signal handler to the `end_read` function
    signal.signal(signal.SIGINT, end_read)

    # Create an instance of the MFRC522 class
    rfid_reader = MFRC522.MFRC522()

    # Welcome message
    print("Please place your RFID card on the reader...")

    # Continuously check for RFID cards
    while continue_reading:
        # Scan for RFID cards
        (status, TagType) = rfid_reader.MFRC522_Request(rfid_reader.PICC_REQIDL)

        # If a card is detected
        if status == rfid_reader.MI_OK:
            print("RFID card detected!")

            # Get the UID of the card
            (status, uid) = rfid_reader.MFRC522_SelectTagSN()

            # If UID was successfully retrieved, proceed
            if status == rfid_reader.MI_OK:
                # Convert UID list to a hexadecimal string
                uid_str = ''.join(['%02X' % i for i in uid])
                return uid_str
                
            else:
                print("Unable to get card UID")
        else:
            # If no card is detected, wait for a short period before retrying
            time.sleep(0.5)


def main():
    uid = get_uid()
    print(uid)

if __name__ == "__main__":
    main()