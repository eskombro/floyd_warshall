class Parser():
    size = 0
    links = []

    def __init__(self, csv):
        csv_lines = csv.split('\n')
        if len(csv_lines) < 2:
            raise Exception("csv is not well formated")
        self.size = int(csv_lines[0])
        if self.size < 2:
            raise Exception("Graph size can't be smaller than 2")
        links_count = int(csv_lines[1])
        if len(csv_lines) != links_count + 2:
            raise Exception("Error in link count")
        for i in range(int(csv_lines[1])):
            self.parse_link(csv_lines[i + 2], i + 3)

    def parse_link(self, line, index):
        line_data = line.split(',')
        if len(line_data) != 3:
            raise Exception("Format error at line {}: {}".format(index, line))
        for i in range(3):
            try:
                line_data[i] = int(line_data[i])
            except Exception:
                raise Exception(
                    "Error in element at line {}: {}".format(index, line))
        self.links.append({
                'src': line_data[0]-1,
                'dst': line_data[1]-1,
                'weight': line_data[2],
            })
