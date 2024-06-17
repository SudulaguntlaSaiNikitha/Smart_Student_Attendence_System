# import cv2
#
# cam_port = 0
# cam = cv2.VideoCapture(cam_port)
#
# inp = input('Enter person name: ')
#
# while True:
#     result, image = cam.read()
#     if result:
#         cv2.imshow(inp, image)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             cv2.imwrite(inp + ".png", image)
#             print("Image taken")
#             break
#     else:
#         print("No image detected. Please try again.")
#
# cam.release()
# cv2.destroyAllWindows()
# import cv2
# import os
#
# # Set up the camera
# cam_port = 0
# cam = cv2.VideoCapture(cam_port)
#
# if not cam.isOpened():
#     print("Error: Could not open camera.")
#     exit()
#
# inp = input('Enter person name: ')
#
# while True:
#     result, image = cam.read()
#     if result:
#         cv2.imshow(inp, image)
#
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             # Save the image to the current directory
#             file_name = inp + ".png"
#             try:
#                 if cv2.imwrite(file_name, image):
#                     print(f"Image taken and saved as {file_name}")
#                 else:
#                     print(f"Error: Failed to save the image as {file_name}")
#             except Exception as e:
#                 print(f"Exception occurred while saving the image: {e}")
#             break
#     else:
#         print("No image detected. Please try again.")
#
# # Release the camera and close all OpenCV windows
# cam.release()
# cv2.destroyAllWindows()
#
import cv2
import os

# Set up the camera
cam_port = 0
cam = cv2.VideoCapture(cam_port)

if not cam.isOpened():
    print("Error: Could not open camera.")
    exit()

inp = input('Enter person name: ')

# Print the current working directory
current_directory = os.getcwd()
print(f"Images will be saved in: {current_directory}")

while True:
    result, image = cam.read()
    if result:
        cv2.imshow(inp, image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            # Save the image to the current directory
            file_name = inp + ".png"
            try:
                if cv2.imwrite(file_name, image):
                    print(f"Image taken and saved as {file_name} in {current_directory}")
                else:
                    print(f"Error: Failed to save the image as {file_name}")
            except Exception as e:
                print(f"Exception occurred while saving the image: {e}")
            break
    else:
        print("No image detected. Please try again.")

# Release the camera and close all OpenCV windows
cam.release()
cv2.destroyAllWindows()
