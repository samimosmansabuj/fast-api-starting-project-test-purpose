import uvicorn
from pathlib import Path

async def app(scope, receive, send):
    assert scope["type"] == "http"
    
    template_path = Path("index.html")
    html_content = template_path.read_text(encoding="utf-8")
    
    try:
        await send(
            {
                "type": "http.response.start",
                "status": 200,
                "headers": [
                    [b"content-type", b"text/html"]
                ]
            }
        )
        
        await send(
            {
                "type": "http.response.body",
                # "body": b"Samim Osman Sabuj"
                "body": html_content.encode("utf-8"),
                "more_body": False,
            }
        )
    except:
        print("Failed to start!")


if __name__ == "__main__":
    config = uvicorn.Config("app:app", port=5000, log_level="info", reload=True)
    server = uvicorn.Server(config)
    server.run()

# if __name__ == "__main__":
#     uvicorn.run("app:app", port=5000, log_level="info")

# async def main(scope, receive, send):
#     assert scope["type"] == "http"
    
#     try:
#         await send(
#             {
#                 "type": "http.response.start",
#                 "status": 200,
#                 "headers": [
#                     [b"content-type", b"text/plain"]
#                 ]
#             }
#         )
#         await send(
#             {
#                 "type": "http.response.body",
#                 "body": "Samim Osman Sabuj",
#             }
#         )
#     except:
#         print("Failed to start server!")



