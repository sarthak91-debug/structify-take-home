def count_intersections(radians, identifiers):
    # Initialize intersection count
    intersections = 0

    # Create a list of chords with their start and end points
    chords = []
    for radian, identifier in zip(radians, identifiers):
        if 's' in identifier:
            chords.append([radian, None])
        else:
            for chord in chords:
                if chord[1] is None:
                    chord[1] = radian
                    break

    # Sort the chords by their start point
    chords.sort(key=lambda x: x[0])

    # Check each pair of chords to see if they intersect
    for i in range(len(chords)):
        for j in range(i + 1, len(chords)):
            start_i, end_i = chords[i]
            start_j, end_j = chords[j]

            # Check for intersection
            inter1 = (start_i < start_j < end_i) if start_i < end_i else (start_j < end_i or start_i < start_j)
            inter2 = (start_j < end_i < end_j) if start_j < end_j else (end_i < end_j or start_j < end_i)
            inter3 = (start_i < end_j < end_i) if start_i < end_i else (end_j < end_i or start_i < end_j)
            inter4 = (start_j < start_i < end_j) if start_j < end_j else (start_i < end_j or start_j < start_i)

            if (inter1 != inter3) and (inter2 != inter4):
                intersections += 1

    return intersections

# Test the function with the examples provided
radians_1 = [0.78, 1.47, 1.77, 3.92]
identifiers_1 = ['s1', 's2', 'e1', 'e2']
intersections_1 = count_intersections(radians_1, identifiers_1)

radians_2 = [0.9, 1.3, 1.70, 2.92]
identifiers_2 = ['s1', 'e1', 's2', 'e2']
intersections_2 = count_intersections(radians_2, identifiers_2)

(intersections_1, intersections_2)
