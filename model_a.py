import heapq

class PriorityStream:
    def __init__(self, file_path):
        self.file_path = file_path
        self.priority_queue = []
        self._load_file()

    def _load_file(self):
        """Load lines from the file into the priority queue."""
        with open(self.file_path, 'r') as file:
            for line in file:
                # Strip the newline character and any leading/trailing whitespace
                stripped_line = line.strip()
                # Push the line into the priority queue with its length as the priority
                heapq.heappush(self.priority_queue, (len(stripped_line), stripped_line))

    def get_next_line(self):
        """Get the next line with the highest priority (shortest length)."""
        if self.priority_queue:
            # Pop the line with the highest priority (shortest length)
            _, line = heapq.heappop(self.priority_queue)
            return line
        else:
            return None

    def is_empty(self):
        """Check if the priority queue is empty."""
        return len(self.priority_queue) == 0

# Example usage:
# Assuming 'example.txt' is a file with multiple lines of text
priority_stream = PriorityStream('example.txt')
while not priority_stream.is_empty():
    print(priority_stream.get_next_line())
