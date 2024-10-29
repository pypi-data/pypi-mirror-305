import os
import yaml
import cv2
import random
import json
import shutil

def print_tabular(data):
    keys_to_print = ['dataset_name', 'id']
    print('\t '.join(keys_to_print))
    # Print rows
    for item in data['dataSets']:
        print('\t '.join(str(item[key]) for key in keys_to_print if key in item))

def format_time(seconds):
    time_str = ""
    hours, remainder = divmod(seconds, 3600)
    if hours:
        time_str += f"{int(hours)}h "
    minutes, seconds = divmod(remainder, 60)
    if minutes or time_str:
        time_str += f"{int(minutes)}m "
    if not time_str:  # if time_str is empty, it means the duration is less than a minute
        time_str = f"{seconds:.2f}s"
    return time_str.strip()

def load_label_map(label_map_path):

    if not label_map_path:
        print("No label map file provided.")
        return None, False

    # Get file extension
    _, ext = os.path.splitext(label_map_path)

    if ext == '.txt':
        if not os.path.exists(label_map_path):
            print(f"Label map file '{label_map_path}' not found.")
            return None, False

        try:
            with open(label_map_path, 'r') as label_file:
                labels = [line.strip() for line in label_file.readlines()]

            num_classes = len(labels)
            if num_classes == 0:
                print("Label map file is empty.")
                return None, False

            print(f"Label map loaded with {num_classes} classes from '{label_map_path}'.")
            return labels, num_classes

        except Exception as e:
            print(f"Error reading label map file: {e}")
            return None, False

    elif ext == '.yaml':
        if not os.path.exists(label_map_path):
            print(f"YAML config file '{label_map_path}' not found.")
            return None, False

        try:
            with open(label_map_path, 'r') as yaml_file:
                config_data = yaml.safe_load(yaml_file)

            if 'names' not in config_data:
                print("YAML config does not contain 'names' field.")
                return None, False

            labels = config_data['names']
            num_classes = len(labels)
            if num_classes == 0:
                print("YAML config file contains an empty 'names' field.")
                return None, False

            print(f"Label map loaded with {num_classes} classes from '{label_map_path}'.")
            return labels, num_classes

        except Exception as e:
            print(f"Error reading YAML config file: {e}")
            return None, False

    # Unsupported file type
    else:
        print(f"Unsupported file type '{ext}'. Please provide a .txt or .yaml file.")
        return None, False


def validate_coco_format(file_path):
        print('Validating coco format...')
        try:
            with open(file_path, 'r') as file:
                coco_data = json.load(file)

            # Check for the essential keys in COCO format
            essential_keys = ['images', 'annotations', 'categories']
            if not all(key in coco_data for key in essential_keys):
                print("Missing one or more essential COCO format keys.")
                return False

            # Validate the structure of 'images', 'annotations', and 'categories'
            for image in coco_data['images']:
                if not all(key in image for key in ['id', 'file_name']): #include width & height
                    print("Invalid structure in 'images'.")
                    return False

            for annotation in coco_data['annotations']:
                if not all(key in annotation for key in ['id', 'image_id', 'category_id']): #include for object detection bbox
                    print("Invalid structure in 'annotations'.")
                    return False

            for category in coco_data['categories']:
                if not all(key in category for key in ['id', 'name']):
                    print("Invalid structure in 'categories'.")
                    return False

            print("Metadata file is in valid COCO format.")
            return True

        except Exception as e:
            print(f"Error validating COCO format: {e}")
            return False

def validate_yolov8_format(annotations_dir, label_map_path):
    print("Validating YOLOv8 format and label map...")
    try:
        annotation_files = [f for f in os.listdir(annotations_dir) if f.endswith('.txt')]
        
        if not annotation_files:
            print(f"No annotation files found in directory '{annotations_dir}'.")
            return False

        random_file = random.choice(annotation_files)
        file_path = os.path.join(annotations_dir, random_file)

    except Exception as e:
        print(f"Error accessing annotation directory: {e}")
        return False

    try:
        labels, num_classes = load_label_map(label_map_path)
        
    except Exception as e:
        print(f"Error validating YOLOv8 labelmap: {e}")
        return False

    # Validate the annotation file
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        for line_num, line in enumerate(lines, start=1):
            components = line.strip().split()

            # Check if there are enough components to validate bounding box (expect exactly 5)
            if len(components) != 5:
                print(f"Line {line_num}: Incorrect number of components. Expected 5, got {len(components)}.")
                return False

            # Validate class_id is within the range of the label map
            class_id = components[0]
            if not class_id.isdigit() or not (0 <= int(class_id) < num_classes):
                print(f"Line {line_num}: Invalid class_id '{class_id}'. It must be between 0 and {num_classes - 1}.")
                return False

            # Validate that the bbox values (center_x, center_y, width, height) are floats between 0 and 1
            bbox_values = components[1:]
            for i, value in enumerate(bbox_values, start=1):
                try:
                    float_value = float(value)
                    if not (0.0 <= float_value <= 1.0):
                        print(f"Line {line_num}, Value {i + 1}: '{value}' is out of bounds. Expected a float between 0 and 1.")
                        return False
                except ValueError:
                    print(f"Line {line_num}, Value {i + 1}: '{value}' is not a valid float.")
                    return False

        print("YOLOv8 annotation file and label map are valid.")
        return True

    except Exception as e:
        print(f"Error validating YOLOv8 format: {e}")
        return False


def flatten_directory(directory_path):
    """
    Copy all files from subdirectories to the main directory
    """
    try:
        # First, copy all files from subdirectories to the main directory
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                # Skip the main directory itself
                if root == directory_path:
                    continue
                # Copy file to the main directory
                source = os.path.join(root, file)
                destination = os.path.join(directory_path, file)
                shutil.move(source, destination)
    except Exception as e:
        print(e)

def yolo_to_coco(images_dir, annotations_dir, label_map_path, output_json_path):
    """
    Converting annotations to coco json
    """
    print('Converting annotations to coco json')

    if images_dir is None or not os.path.isdir(images_dir):
        raise TypeError("images_dir must be a valid directory path.")

    coco_output = {
        "info": {
            "year": "2024",
            "version": "2",
            "description": "Exported from cortalinsight",
            "contributor": "",
            "date_created": "2024-09-27T16:40:52+00:00"
        },
        "licenses": [
            {
                "id": 1,
                "url": "",
                "name": "Unknown"
            }
        ],
        "images": [],
        "annotations": [],
        "categories": []
    }


    class_names, num_classes = load_label_map(label_map_path)
    
    # Create the categories part in COCO format
    for idx, class_name in enumerate(class_names):
        coco_output["categories"].append({
            "id": idx,
            "name": class_name,
            "supercategory": "none"
        })

    annotation_id = 1
    image_id = 1

    # Iterate through all YOLO annotation files
    for filename in os.listdir(annotations_dir):
        if filename.endswith(".txt"):
            annotation_file = os.path.join(annotations_dir, filename)

            image_base_name = os.path.splitext(filename)[0]
            image_file = os.path.join(images_dir, image_base_name + ".jpg")

            # Open the image using cv2 to get width and height
            if not os.path.exists(image_file):
                print(f"Image file '{image_file}' not found for annotation '{filename}'. Skipping...")
                continue

            image = cv2.imread(image_file)
            if image is None:
                print(f"Could not open image '{image_file}'. Skipping...")
                continue
            
            image_height, image_width = image.shape[:2]

            # Add the image entry to the COCO output
            coco_output["images"].append({
                "id": image_id,
                "file_name": os.path.basename(image_file),
                "width": image_width,
                "height": image_height
            })

            # Parse the YOLO annotation file
            with open(annotation_file, 'r') as f:
                lines = f.readlines()

            for line in lines:
                parts = line.strip().split()
                class_id = int(parts[0])
                center_x = float(parts[1])
                center_y = float(parts[2])
                bbox_width = float(parts[3])
                bbox_height = float(parts[4])

                # Convert YOLO format to COCO format (absolute values)
                x_min = int((center_x - bbox_width / 2) * image_width)
                y_min = int((center_y - bbox_height / 2) * image_height)
                abs_width = int(bbox_width * image_width)
                abs_height = int(bbox_height * image_height)

                # Add the annotation entry to the COCO output
                coco_output["annotations"].append({
                    "id": annotation_id,
                    "image_id": image_id,
                    "category_id": class_id,
                    "bbox": [x_min, y_min, abs_width, abs_height],
                    "area": abs_width * abs_height,
                    "iscrowd": 0
                })

                annotation_id += 1
            image_id += 1

    # Save the COCO format output to a JSON file
    with open(output_json_path, 'w') as json_file:
        json.dump(coco_output, json_file, indent=4)

    print(f"COCO format JSON file created at: {output_json_path}")
    return output_json_path


def subsample_video_to_frames(input_video, output_folder='video_output', sub_sample_rate=15, image_format='png'):

    output_folder = os.path.abspath(output_folder)

    # Ensure the output directory exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the video file
    cap = cv2.VideoCapture(input_video)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    frame_idx = 0
    saved_frame_idx = 0

    # Read through the video frame by frame
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Save the frame if it's at the subsample rate
        if frame_idx % sub_sample_rate == 0:
            filename = os.path.join(output_folder, f"frame_{saved_frame_idx:04d}.{image_format}")
            cv2.imwrite(filename, frame)
            saved_frame_idx += 1

        frame_idx += 1

    cap.release()
    print(f'Successfully extracted {frame_idx} frames to {output_folder}')
