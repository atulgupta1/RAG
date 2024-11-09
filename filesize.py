import os
import matplotlib.pyplot as plt

def get_folder_size(folder_path):
    """Calculates the total size of .md files in a folder and its subfolders."""
    total_size = 0
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".md"):
                total_size += os.path.getsize(os.path.join(root, file))
    return total_size

def plot_folder_sizes(root_directory):
    """Plots the size of .md files in each Rel folder."""

    rel_folders = ["Rel-8", "Rel-9", "Rel-10", "Rel-11", "Rel-12", "Rel-13", "Rel-14", "Rel-15", "Rel-16", "Rel-17", "Rel-18", "Rel-19"]
    folder_sizes = []

    for rel_folder in rel_folders:
        folder_path = os.path.join(root_directory, rel_folder)
        folder_size = get_folder_size(folder_path)
        folder_sizes.append(folder_size / (1024 * 1024))  # Convert to MB

    # Print a tabular summary
    print("Release\tSize (MB)")
    for rel_folder, size in zip(rel_folders, folder_sizes):
        print(f"{rel_folder}\t{size:.2f}")

    plt.figure(figsize=(10, 6))
    plt.bar(rel_folders, folder_sizes, color='skyblue')
    plt.xlabel("Release", fontsize=12)
    plt.ylabel("Size (MB)", fontsize=12)
    plt.title("Size of .md Files in Each Release", fontsize=14)
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability

    # Add labels to each bar
    for i, v in enumerate(folder_sizes):
        plt.text(i, v, str(round(v, 2)) + ' MB', ha='center', va='bottom')

    plt.grid(axis='y', linestyle='--')
    plt.tight_layout()
    plt.show()

# Replace 'D:\\TSpec-LLM\\3GPP-clean' with your actual root directory
root_directory = "D:\\TSpec-LLM\\3GPP-clean"
plot_folder_sizes(root_directory)