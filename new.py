import cv2 
# Replace 'your_camera_ip_address' with the actual IP address of your camera
# Replace 'your_username' and 'your_password' with the actual username and password of your camera if required
url = 'http://193.168.0.101'
 
# Create a VideoCapture object with the URL of the IP camera stream
cap = cv2.VideoCapture(url)
 
# Check if the camera stream is opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()
 
# Read frames from the camera stream
while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame.")
        break
 
    # Display the frame
    cv2.imshow('IP Camera', frame)
 
    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
# Release the VideoCapture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
