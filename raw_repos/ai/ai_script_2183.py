def find_path(start, end):
    # Create an empty list to store the path
    path = []

    # Create a dictionary to store visited nodes
    visited = {start: None}

    # Create a queue and add the initial space to it
    queue = [start]

    # Keep looping until the queue is empty
    while len(queue) > 0:
        # Get the first element in the queue
        curr = queue.pop(0)

        # Add the current node to the path
        path.append(curr)

        # Check if we reached the end of the path
        if curr == end:
            return path

        # Explore all neighbours of the current node
        for neighbour in get_neighbours(curr):
            # Check if the neighbour is not visited previously
            if neighbour not in visited:
                # Add the neighbour to the queue and mark it as visited
                queue.append(neighbour)
                visited[neighbour] = curr
    # If the queue is empty, there is no path
    return None