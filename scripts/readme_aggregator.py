"""
Aggregate all problem-specific README files into one for better searching 
"""


import os


if __name__ == "__main__":
    root_dir = ".."
    output_dir = root_dir
    output_filename = "README_all.md"
    output_content = ""
    

    readme_dict = dict()
    for fn in os.listdir(root_dir):
        if "problem" in fn:
            problem_number = int(fn.replace('problem_', ''))
            readme_path = root_dir + "/" + fn + '/README.md'
            readme_content = ""
            with open(readme_path, 'r') as f:
                for line in f:
                    if ("# " in line) and ("## " not in line):   # title line
                        line = line.replace("# ", "# Problem %d: " % problem_number)
                    readme_content += line
            readme_dict[problem_number] = readme_content
        
    with open("%s/%s" % (output_dir, output_filename), 'w') as f:
        for k in readme_dict:
            f.write(readme_dict[k])
            f.write('\n\n')

    #print readme_dict
            

