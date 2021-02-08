from reprint import output
import time
import random

if __name__ == "__main__":
    with output(output_type='dict', sort_key=lambda x:x[1]) as output_lines:
        for i in range(10):
            for idx in range(10):
                output_lines[str(idx)] = random.randint(0, 100)
            output_lines.append("epoch {} max: {}".format(i+1, max(output_lines.values())))
            
            time.sleep(1)

        output_lines.append("finished")
