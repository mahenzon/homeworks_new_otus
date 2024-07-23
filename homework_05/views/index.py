from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from misc.templating import TemplateResponse

router = APIRouter()


@router.get(
    "/",
    name="main:index",
    response_class=HTMLResponse,
)
def index(request: Request):
    return TemplateResponse(
        request=request,
        name="index.html",
    )


@router.get(
    "/about/",
    name="main:about",
    response_class=HTMLResponse,
)
def index(request: Request):
    return TemplateResponse(
        request=request,
        name="about.html",
    )
