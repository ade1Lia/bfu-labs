import cv2
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('movie')
cap = cv2.VideoCapture(parser.parse_args().movie)
while (True):
    ret, frame = cap.read()
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,str(cap.get(cv2.CAP_PROP_FPS)),(50, 50),font, 1,(0, 255, 255),2, cv2.LINE_4)
    cv2.putText(frame, parser.parse_args().movie, (150, 50), font, 1, (0, 255, 255), 2, cv2.LINE_4)
    cv2.imshow('video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()