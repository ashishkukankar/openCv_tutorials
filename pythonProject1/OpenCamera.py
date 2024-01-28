import cv2

''' 
this method open camera. here you can give 
0/-1/1 - camera or filepath 
'''
cam = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter.fourcc(*'XVID')
output = cv2.VideoWriter('output.avi', fourcc, 20, (640, 480))  # saving video in output file
print("camera", cam.isOpened())

'''Run the loop while camera is open'''
while cam.isOpened():
    '''cam.read()- it will return boolean and frame value.'''
    ret, frame = cam.read()
    if ret:
        output.write(frame)
        '''
        cv2.cvtColor - convert color original frame to different color format. 
        It takes parameter as source frame and color formate 
        '''
        grey = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        '''cv2.imshow- show the camera '''
        cv2.imshow("frame", grey)
        '''condition for stop showing video'''
        if cv2.waitKey(1) & 0XFF == ord('q'):
            break
    else:
        break
'''release resources'''
cv2.destroyAllWindows()
cam.release()
output.release()
