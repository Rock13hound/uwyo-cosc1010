# Elijah Gertsch
# Lab Section 11
# Submission Date 11/12/2024
# Sources, help given to/received from

with open("prompt.txt", "r") as infile, open("out.txt", "w") as outfile:
    for line in infile:
        pairs = line.strip().split("\t")
        output_line = ""
        for pair in pairs:
            if ':' in pair:
                key, value = pair.split(":")
                count = int(value)
                if key == 'w':
                    output_line += " " * count
                elif key == '*':
                    output_line += "*" * count
        outfile.write(output_line + "\n")
