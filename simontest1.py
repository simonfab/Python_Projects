# print("hello world")

#from fastapi import FastAPI

#app = FastAPI()

#@app.get("/")
#async def root():
#    return {"message": "Hello World"}






response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[],
  temperature=0.5,
  max_tokens=64,
  top_p=1
)
