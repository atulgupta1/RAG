import os
import matplotlib.pyplot as plt

def get_folder_size(folder_path, extensions):
    """Calculates the total size of files with specified extensions in a folder and its subfolders."""
    total_size = 0
    for root, _, files in os.walk(folder_path):
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                file_path = os.path.join(root, file)
                total_size += os.path.getsize(file_path)
    return total_size

def plot_folder_sizes(root_directory):
    """Plots the total size of .md and .docx files in each Rel folder."""

    rel_folders = ["Rel-8", "Rel-9", "Rel-10", "Rel-11", "Rel-12", "Rel-13", "Rel-14", "Rel-15", "Rel-16", "Rel-17", "Rel-18", "Rel-19"]
    md_sizes = []
    docx_sizes = []

    for rel_folder in rel_folders:
        folder_path = os.path.join(root_directory, rel_folder)
        md_sizes.append(get_folder_size(folder_path, [".md"]))  # Calculate size of .md files
        docx_sizes.append(get_folder_size(folder_path, [".docx"]))  # Calculate size of .docx files

    # Print a tabular summary
    print("Release\tMD Size (MB)\tDOCX Size (MB)")
    for rel_folder, md_size, docx_size in zip(rel_folders, md_sizes, docx_sizes):
        print(f"{rel_folder}\t{md_size / (1024 * 1024):.2f}\t{docx_size / (1024 * 1024):.2f}")

    plt.figure(figsize=(10, 6))
    width = 0.35  # Adjust bar width for better visualization of two datasets

    # Plot bar graphs for .md and .docx sizes
    p1 = plt.bar(rel_folders, md_sizes, width, label='.md Files', color='skyblue')
    p2 = plt.bar([x + width for x in rel_folders], docx_sizes, width, label='.docx Files', color='coral')
    plt.xlabel("Release", fontsize=12)
    plt.ylabel("Size (MB)", fontsize=12)
    plt.title("Size of .md and .docx Files in Each Release", fontsize=14)
    plt.xticks([x + width / 2 for x in rel_folders], rel_folders, rotation=45, ha='right')  # Rotate x-axis labels

    # Add legend
    plt.legend(handles=[p1[0], p2[0]], loc='upper left')

    plt.grid(axis='y', linestyle='--')
    plt.tight_layout()
    plt.show()

# Replace 'D:\\TSpec-LLM\\3GPP-clean' with your actual root directory
root_directory = "D:\\TSpec-LLM\\3GPP-clean"
plot_folder_sizes(root_directory)