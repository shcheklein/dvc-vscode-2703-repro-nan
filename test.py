from pathlib import Path

Path("out.json").write_text(Path("in.json").read_text())
