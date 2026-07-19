"""Generate the repository's deterministic terminal demo GIF."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


WIDTH, HEIGHT = 960, 540
BACKGROUND = "#0d1117"
PANEL = "#161b22"
TEXT = "#e6edf3"
MUTED = "#8b949e"
GREEN = "#3fb950"
BLUE = "#58a6ff"
YELLOW = "#d29922"


def load_font(size: int):
    candidates = [
        "/System/Library/Fonts/Menlo.ttc",
        "/System/Library/Fonts/Monaco.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
    ]
    for candidate in candidates:
        if Path(candidate).exists():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()


FONT = load_font(21)
SMALL = load_font(17)
TITLE = load_font(25)


SCENES = [
    ("1. Give a focused task", [
        ("$ codex", BLUE),
        ("> Fix the README typo.", TEXT),
        ("> Scope: README.md only.", TEXT),
        ("> Done when: links still work.", TEXT),
    ]),
    ("2. Read project guidance", [
        ("• Reading AGENTS.md", BLUE),
        ("  - keep the diff minimal", MUTED),
        ("  - check Markdown links", MUTED),
        ("  - report verification", MUTED),
    ]),
    ("3. Make the smallest change", [
        ("M README.md", YELLOW),
        ("- beginer-friendly", "#f85149"),
        ("+ beginner-friendly", GREEN),
    ]),
    ("4. Verify", [
        ("$ markdown-link-check README.md", BLUE),
        ("✓ All local links are valid", GREEN),
        ("$ git diff --check", BLUE),
        ("✓ No whitespace errors", GREEN),
    ]),
    ("5. Human reviews the diff", [
        ("Changed: README.md", TEXT),
        ("Tests: link check, diff check", TEXT),
        ("Unresolved: none", TEXT),
        ("✓ Ready for human approval", GREEN),
    ]),
]


def frame(title, lines, progress):
    image = Image.new("RGB", (WIDTH, HEIGHT), BACKGROUND)
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle((32, 32, WIDTH - 32, HEIGHT - 32), 16, fill=PANEL, outline="#30363d", width=2)
    draw.ellipse((56, 55, 70, 69), fill="#ff5f56")
    draw.ellipse((78, 55, 92, 69), fill="#ffbd2e")
    draw.ellipse((100, 55, 114, 69), fill="#27c93f")
    draw.text((136, 48), "hajimete-ai-agent-development", font=SMALL, fill=MUTED)
    draw.text((64, 104), title, font=TITLE, fill=TEXT)
    y = 166
    for text, color in lines:
        draw.text((72, y), text, font=FONT, fill=color)
        y += 44
    draw.rounded_rectangle((64, HEIGHT - 78, WIDTH - 64, HEIGHT - 60), 8, fill="#21262d")
    draw.rounded_rectangle((64, HEIGHT - 78, 64 + int((WIDTH - 128) * progress), HEIGHT - 60), 8, fill=BLUE)
    label = "safe • small • verified"
    label_box = draw.textbbox((0, 0), label, font=SMALL)
    label_width = label_box[2] - label_box[0]
    draw.text((WIDTH - 64 - label_width, HEIGHT - 112), label, font=SMALL, fill=MUTED)
    return image


def main():
    frames = []
    for index, (title, lines) in enumerate(SCENES, start=1):
        for visible in range(1, len(lines) + 1):
            frames.append(frame(title, lines[:visible], (index - 1 + visible / len(lines)) / len(SCENES)))
        frames.extend([frame(title, lines, index / len(SCENES))] * 3)
    output = Path(__file__).resolve().parents[1] / "assets" / "agent-development-demo.gif"
    output.parent.mkdir(parents=True, exist_ok=True)
    frames[0].save(output, save_all=True, append_images=frames[1:], duration=480, loop=0, optimize=True)
    print(output)


if __name__ == "__main__":
    main()
