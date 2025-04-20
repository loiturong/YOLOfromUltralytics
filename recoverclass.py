import os

# Replace 'input.txt' with your file name
input_file = r'C:\Users\loitr\OneDrive\PARAmeter\Project\MachineVision\project-5-at-2025-03-01-12-19-f9e929f6\labels_old'
output_file = r'C:\Users\loitr\OneDrive\PARAmeter\Project\MachineVision\project-5-at-2025-03-01-12-19-f9e929f6\labels'
old_class = '1'
new_class = '4'



def convert_class(in_: str, out_: str):
    with open(in_, 'r') as f:
        lines = f.readlines()

    with open(out_, 'w') as f:
        for line in lines:
            parts = line.strip().split()
            if parts[0] == old_class:
                parts[0] = new_class
            f.write(' '.join(parts) + '\n')

    print(f"Fixed labels saved to {output_file}")

file_names = [f for f in os.listdir(input_file) if os.path.isfile(os.path.join(input_file, f))]

for idx, file_name in enumerate(file_names):
    convert_class(input_file + "/" + file_name, output_file + "/" + file_name)

    print(f"Converted {file_name} to 640x640, saved as {f'image_{idx + 1}.jpg'}")