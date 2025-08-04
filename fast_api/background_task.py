from fastapi import BackgroundTasks,FastAPI 
import time

app = FastAPI()

def write_notification(email: str, message: str = ""):
    time.sleep(5)  
    with open("log.txt",mode = "a") as email_file:
        content = f"Notification for {email}: {message}\n"
        email_file.write(content)

@app.post("/send-notification/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks):
   
    background_tasks.add_task(write_notification, email, message="your report is ready.")
    return {"message": "Notification sent in the background"}