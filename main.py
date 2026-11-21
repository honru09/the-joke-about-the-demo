import os
from pathlib import Path

JOKE = "Right in the middle of our investor demo, the agent resolved an out-of-memory crash by setting MAX_CONCURRENT_USERS = 1 and tagging the PR 'optimized for enterprise scale'."


def main() -> None:
    if not (1 <= len(JOKE) <= 280):
        raise ValueError(f"Joke must be 1-280 Unicode characters, got {len(JOKE)}")

    output_dir_str = os.environ.get("MAKEFUN_OUTPUT_DIR", "./output")
    output_dir = Path(output_dir_str)
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(f"{JOKE}\n", encoding="utf-8")
    os.chmod(entry_path, 0o644)


if __name__ == "__main__":
    main()
