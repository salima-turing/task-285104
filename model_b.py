import heapq

class priority_stream:
    def __init__(self, filename):
        """
        Initialize the priority_stream with the given filename.
        The lines from the file will be sorted based on their priority (length).
        """
        self.filename = filename
        self.priority_queue = []

    def readline(self):
        """
        Read the next line from the file and add it to the priority queue.
        Return the sorted line with the highest priority (shortest length).
        """
        if not self.priority_queue:
            with open(self.filename, 'r') as file:
                for line in file:
                    heapq.heappush(self.priority_queue, (len(line), line))

        if self.priority_queue:
            _, line = heapq.heappop(self.priority_queue)
            return line
        return None

# Example usage:
if __name__ == "__main__":
    import os

    filename = 'example.txt'  # Replace this with your actual file name

    if os.path.exists(filename):
        ps = priority_stream(filename)
        line = ps.readline()
        while line:
            print(line.rstrip())
            line = ps.readline()
    else:
        print(f"Error: File {filename} not found.")
