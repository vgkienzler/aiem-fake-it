from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv

from src.config import assistant_detail
from src.models import assistant_completion, client

load_dotenv()

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Mount the static files directory
app.mount("/static", StaticFiles(directory="../static"), name="static")

# Create a thread
thread = client.beta.threads.create()

messages = client.beta.threads.messages.list(
            thread_id=thread.id
        )

assistant_id = assistant_detail["id_fakeit"]


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html",
                                      {"request": request, "conversation": messages.data})


@app.post("/", response_class=HTMLResponse)
async def chat(request: Request, message: str = Form(...)):
    print("Message received from api: ", message)

    messages = await assistant_completion(
        message=message,
        assistant_id=assistant_id,
        thread=thread,
    )

    return templates.TemplateResponse("index.html",
                                      {"request": request, "conversation": messages.data})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
