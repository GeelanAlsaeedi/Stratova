"""UI configuration."""

from pathlib import Path

UI_DIR = Path(__file__).resolve().parent
LOGO_SVG_PATH = UI_DIR / "assets" / "logo.svg"

BRAND_BLUE = "#1d348a"
LIGHT_GREY = "#f1f1f1"

GTM_BRIEF_FIELDS = ["product", "audience", "market", "goals"]


def load_logo_svg() -> str:
    return LOGO_SVG_PATH.read_text(encoding="utf-8")
