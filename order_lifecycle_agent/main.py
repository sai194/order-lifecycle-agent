import os
import uvicorn
from google.adk.cli.fast_api import get_fast_api_app

app = get_fast_api_app(
    agents_dir=os.path.dirname(os.path.abspath(__file__)),
    web=True,
)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8001, reload=True)
