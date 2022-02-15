import cv2
import numpy as np
from pyzbar.pyzbar import decode
from time import strftime

# set up the webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# this will count if a qr code was detected
qr_code = 0

# get the info in qr code
while qr_code < 1: # once the value of qr_code is greater than 1, it will break the while loop 
    _, qr = cap.read()
    for info in decode(qr):
        contact_details = info.data.decode("utf-8")
        qr_code = qr_code+1 # the value will be incremented by 1 once a qr code is detected
    cv2.imshow('QR CODE SCANNER', qr)
    cv2.waitKey(1)

# get the current date/time    
current_date_time = strftime("%m/%d/%Y %I:%M:%S %p")

# create a text file to store the info from qr code and  its access date/time
txt_file = open('CONTACT TRACE.txt', 'w')
txt_file.write("    Date and Time Access: "+current_date_time+"\n")
txt_file.write(contact_details)
