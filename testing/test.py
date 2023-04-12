import os
import re

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_name = f"{project_dir}/testing/results_summary.txt"
temp_out = f"{project_dir}/testing/temp.out"

f = open(file_name, "w")

REF_STR_SIZES = (12, 164, 344, 524, 704, 884, 1064)
FRAME_SIZES = (2, 5, 7)

def parse_out_file(n_pages):
    results = []
    with open(temp_out, "r") as f:
        for line in f:
            # find n page faults
            page_faults = re.findall(r"(\d+) page faults", line)
            if page_faults:
                results.append(round(int(page_faults[0])/n_pages, 2))
    
    return results

for ref_str_size in REF_STR_SIZES:
    f.write(f"REFERENCE STRING SIZE: {ref_str_size}\n")

    for frame_size in FRAME_SIZES:
        f.write(' ' * 2)
        f.write(f"FRAME SIZE: {frame_size}\n")

        f.write(' ' * 3)
        f.write(f"Fault ratio\n".rjust(7))
        os.system(f'python paging.py {frame_size} {ref_str_size} > {temp_out}\n')

        results = parse_out_file(ref_str_size)
        
        f.write(' ' * 4)
        f.write(f"FIFO: {results[0]}\n")
        f.write(' ' * 4)
        f.write(f"LRU: {results[1]}\n")
        f.write(' ' * 4)
        f.write(f"OPT: {results[2]}\n")
        