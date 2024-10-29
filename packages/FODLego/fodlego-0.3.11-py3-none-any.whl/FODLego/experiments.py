#!/usr/bin/env python3

import numpy as np



def readXYZ(input_file):
    """
    Create a relaxed position in which the FODs have a minum of energy,
    based off an electrostatic potential.
    """
    with open(input_file, 'r') as infile:
        lines = infile.readlines()

        # Process the remaining lines
        for line in lines[3:]:
            parts = line.split()
            coords = np.array(parts[1:4])  # First three are the coordinates
            coords = coords.astype(float)
            print(coords)
            print(np.linalg.norm(coords, axis=0))

    # Create the shells



readXYZ("test2shellsxyz.xyz")
    # Load the shells
    #Shell1, Shell2 = 0,2
