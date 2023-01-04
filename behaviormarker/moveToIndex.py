import numpy as np
from pathlib import Path


def move_to_index(video_path, individual, behavior, current_frame_number):
    """
    Move to the next index based on the file loaded
    :param video_path: path to the video file
    :param individual: the individual being marked
    :param behavior: the behavior being marked
    :param current_frame_number: the current frame number is GUI is on
    :return:
    """

    filepath = Path(video_path)
    destination_file = filepath.parent / f'Training_Data/{behavior}_{filepath.stem}_{individual}.npy'

    data = np.load(destination_file)

    for i, dt in enumerate(data):
        if dt > current_frame_number:
            percentage = np.round((i / data.shape[0]) * 100, 2)
            return dt, percentage
