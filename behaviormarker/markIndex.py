import numpy as np
from pathlib import Path
import json
import pandas as pd


def mark_index(video_path, individual, behavior, from_frame_number, to_frame_number):
    """
    Mark the index for the behavior
    :param video_path: path to the video file
    :param individual: the individual being marked
    :param behavior: the behavior being marked
    :param from_frame_number: the frame number to start from for the sequence to mark
    :param to_frame_number: the frame number to end for the sequence to mark
    :return:
    """

    filepath = Path(video_path)
    destination_file = filepath.parent / f'{filepath.stem}_{individual}.json'
    new_range = [from_frame_number, to_frame_number]

    if not destination_file.exists():
        data = {individual: {behavior: [new_range]}}
    else:
        data = pd.read_json(destination_file).to_dict()
        if behavior in data[individual].keys():
            old_ranges = data[individual][behavior]
            old_ranges.append(new_range)
            data[individual][behavior] = old_ranges
        else:
            data[individual][behavior] = [new_range]
    destination_file = str(destination_file.absolute())
    with open(destination_file, 'w') as outfile:
        json.dump(data, outfile)
