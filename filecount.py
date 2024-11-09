import os

def count_words_in_markdown(file_path):
    """Counts the number of words in a Markdown file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        words = file.read().strip().split()
        return len(words)

def get_folder_word_count(folder_path):
    """Calculates the total word count of .md files in a folder and its subfolders."""
    total_word_count = 0
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                word_count = count_words_in_markdown(file_path)
                total_word_count += word_count
    return total_word_count

def plot_folder_word_counts(root_directory):
    """Plots the word count of .md files in each Rel folder."""

    rel_folders = ["Rel-8", "Rel-9", "Rel-10", "Rel-11", "Rel-12", "Rel-13", "Rel-14", "Rel-15", "Rel-16", "Rel-17", "Rel-18", "Rel-19"]
    folder_word_counts = []

    for rel_folder in rel_folders:
        folder_path = os.path.join(root_directory, rel_folder)
        word_count = get_folder_word_count(folder_path)
        folder_word_counts.append(word_count)

    # Print a tabular summary
    print("Release\tWord Count")
    for rel_folder, word_count in zip(rel_folders, folder_word_counts):
        print(f"{rel_folder}\t{word_count}")

    # You can comment out the plotting section if you don't need a bar chart
    # plt.figure(figsize=(10, 6))
    # plt.bar(rel_folders, folder_word_counts, color='skyblue')
    # plt.xlabel("Release", fontsize=12)
    # plt.ylabel("Word Count", fontsize=12)
    # plt.title("Word Count of .md Files in Each Release", fontsize=14)
    # plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
    # plt.grid(axis='y', linestyle='--')
    # plt.tight_layout()
    # plt.show()

# Replace 'D:\\Spec\\3GPP-clean' with your actual root directory
root_directory = "D:\\Spec\\3GPP-clean"
plot_folder_word_counts(root_directory)
