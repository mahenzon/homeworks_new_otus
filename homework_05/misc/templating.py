__all__ = (
    "templates",
    "TemplateResponse",
)

from pathlib import Path
from starlette.templating import Jinja2Templates

parent_dir = Path(__file__).parent.parent
templates_dir = parent_dir / "templates"

templates = Jinja2Templates(directory=str(templates_dir))
TemplateResponse = templates.TemplateResponse
