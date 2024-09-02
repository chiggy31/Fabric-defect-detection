import os
import cv2

# Define the paths to the folders containing images
project_path = r"D:\minor 2\datasets\New folder"
holes_folder = os.path.join(project_path, "holes")
lines_folder = os.path.join(project_path, "lines")

# Define the rotation angles
rotation_angles = [20, 40, 60, 75, 90]

def rotate_and_save_images(folder_path, angles):
    # Iterate through each image in the folder
    for image_name in os.listdir(folder_path):
        image_path = os.path.join(folder_path, image_name)
        image = cv2.imread(image_path)
        
        if image is None:
            continue
        
        # Get the image dimensions
        (h, w) = image.shape[:2]
        center = (w // 2, h // 2)
        
        # Apply each rotation and save the augmented image
        for angle in angles:
            # Perform the rotation
            M = cv2.getRotationMatrix2D(center, angle, 1.0)
            rotated_image = cv2.warpAffine(image, M, (w, h))
            
            # Save the rotated image
            rotated_image_name = f"aug_rot_{angle}_{image_name}"
            rotated_image_path = os.path.join(folder_path, rotated_image_name)
            cv2.imwrite(rotated_image_path, rotated_image)

# Perform rotation on images in both folders
rotate_and_save_images(holes_folder, rotation_angles)
rotate_and_save_images(lines_folder, rotation_angles)