import os
from datetime import datetime

def save_output(raw_content, optimized_content):
    # Ensure outputs directory exists
    output_dir = os.path.join(os.getcwd(), "outputs")
    os.makedirs(output_dir, exist_ok=True)

    # Create timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # File paths
    raw_file = os.path.join(output_dir, f"raw_{timestamp}.txt")
    optimized_file = os.path.join(output_dir, f"optimized_{timestamp}.txt")

    # Save raw content
    with open(raw_file, "w", encoding="utf-8") as f:
        f.write(raw_content)

    # Save optimized content
    with open(optimized_file, "w", encoding="utf-8") as f:
        f.write(optimized_content)

    return raw_file, optimized_file
