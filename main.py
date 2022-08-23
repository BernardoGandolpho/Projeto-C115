import uvicorn

from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    uvicorn.run("app.chatbot:app", host="0.0.0.0", port=7999, reload=True)
