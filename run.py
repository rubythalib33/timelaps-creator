import cv2

def create_timelapse(input_video_path, frames_to_skip, output_video_path):
    # Open the input video
    cap = cv2.VideoCapture(input_video_path)

    if not cap.isOpened():
        print(f"Error: Could not open video {input_video_path}")
        return

    # Get the properties of the input video
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    # Define the codec and create VideoWriter object for the output video
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video_path, fourcc, fps , (frame_width, frame_height))

    frame_count = 0
    while True:
        ret, frame = cap.read()
        
        if not ret:
            break
        
        if frame_count % (frames_to_skip + 1) == 0:
            print(frame_count)
            out.write(frame)
        
        frame_count += 1

    # Release everything when done
    cap.release()
    out.release()
    print(f"Timelapse video saved as {output_video_path}")

# Example usage
input_video = '../z.mp4'
frames_to_skip = 60
output_video = 'output_timelapse.mp4'

create_timelapse(input_video, frames_to_skip, output_video)
