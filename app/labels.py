from enum import Enum

class Labels(Enum):
    NULL = (0, "null")
    STILL = (1, 'still')
    WALKING = (2, 'walking')
    RUN = (3, 'run')
    BIKE = (4, 'bike')
    CAR = (5, 'car')
    BUS = (6, 'bus')
    TRAIN = (7, 'train')
    SUBWAY = (8, 'subway')


for label in Labels:
    print(f"{label.name} = {label.value}")