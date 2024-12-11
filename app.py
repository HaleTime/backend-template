import uvicorn

if __name__ == '__main__':
    uvicorn.run("app.server:app", host="0.0.0.0", port=9999, workers=0)
