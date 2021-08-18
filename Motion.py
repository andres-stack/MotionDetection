import cv2
import numpy as np
from twilio.rest import Client



account_sid = #account_sid
auth_token = #auth_toekn

myPhone = #myPhone
TwilioNumber = #TwiloNumber

client = Client(account_sid, auth_token)


vidCapture = cv2.VideoCapture(0)

fgbg = cv2.createBackgroundSubtractorMOG2(100, 200, True)

frameCount = 0

while(1):
    ret, frame = vidCapture.read()

    if not ret:
        break

    frameCount += 1

    resizedFrame = cv2.resize(frame, (0, 0), fx=.6, fy= .6)

    fgmask = fgbg.apply(resizedFrame)

    count = np.count_nonzero(fgmask)

    if(frameCount > 1 and count > 1000):
        client.messages.create(
            to=myPhone,
            from_=TwilioNumber,
            body='I am moving ' + u'\U0001f680')

        cv2.imshow('frame', resizedFrame)
        cv2.imshow('Mask', fgmask)

        key = cv2.waitKey(1) & 0xff

        if key == 27:
            break
vidCapture.release()
cv2.destroyAllWindows()
