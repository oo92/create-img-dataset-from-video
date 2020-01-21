import cv2
import os

def create_dataset(n):
    cam = cv2.VideoCapture('../Videos/training-videos/' + str(n) + '.mp4')

    try:
        if not os.path.exists('../Videos/training-videos/data' + str(n)):
            os.makedirs('../Videos/training-videos/data' + str(n))
    except OSError:
        print('Error: Creating directory of data' + str(n))

    current_frame = 0

    while (True):

        ret, frame = cam.read()

        if ret:
            name = '../Videos/training-videos/data' + str(n) + '/frame' + str(current_frame) + '.jpg'
            print('Creating...' + name)

            cv2.imwrite(name, frame)

            current_frame += 1
        else:
            break
    cam.release()
    cv2.destroyAllWindows()


for i in range(0, 6):
    create_dataset(i)