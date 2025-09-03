import os
import cv2

DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_classes = 3
dataset_size = 100

cap = cv2.VideoCapture(0)  
for j in range(number_of_classes):
    class_dir = os.path.join(DATA_DIR, str(j))
    if not os.path.exists(class_dir):
        os.makedirs(class_dir)

    print('Collecting data for class {}'.format(j))

    input("Ready? Press Enter to start...")  

    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        
        # Save frame if 's' is pressed
        if cv2.waitKey(25) == ord('s'):
            cv2.imwrite(os.path.join(class_dir, '{}.jpg'.format(counter)), frame)
            counter += 1
            print(f"Saved image {counter}/{dataset_size}")

        # Exit loop if 'q' is pressed
        if cv2.waitKey(25) == ord('q'):
            break

    if counter == dataset_size:
        print(f"Data collection for class {j} complete!")
    else:
        print(f"Data collection for class {j} interrupted.")

cap.release()
cv2.destroyAllWindows()
