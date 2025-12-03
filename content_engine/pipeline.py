from content_engine.generate_content import generate_marketing_content
from content_engine.optimizer import optimize_content
from content_engine.utils import save_output

def run_pipeline():
    topic = "AI in digital marketing"
    platform = "LinkedIn"

    print("\n🔥 Generating content...\n")
    raw_content = generate_marketing_content(topic, platform)

    print("\n🛠 Optimizing content...\n")
    optimized_content = optimize_content(raw_content)

    # Save to files
    raw_path, optimized_path = save_output(raw_content, optimized_content)

    print("\n✅ Final Optimized Content:\n")
    print(optimized_content)

    print("\n📁 Saved files:")
    print(f"Raw content saved at: {raw_path}")
    print(f"Optimized content saved at: {optimized_path}")

if __name__ == "__main__":
    run_pipeline()
