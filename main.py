import os

from dotenv import load_dotenv
import requests

from fastapi import FastAPI
from models import Course, Discussion
#/courses/:course_id/discussion_topics


app = FastAPI()

load_dotenv()

access_token = os.getenv("ACCESS_TOKEN")


base_url = "https://dixietech.instructure.com/api/v1"

headers: dict[str, str] = {
    "Authorization": f"Bearer {access_token}"

}

response = requests.get(url=f"{base_url}/courses", headers=headers)
r_json = response.json()

course= Course(id=r_json[0]["id"], name=r_json[0]["name"])

print(course)

#/courses

@app.get("/courses")
async def get_courses() -> Course:
    response = requests.get(url=f"{base_url}/courses", headers=headers)
    r_json = response.json()

    courses: list[Course] = []

    for course_json in r_json:
        course= Course(id=r_json[0]["id"], name=r_json[0]["name"]) 
        courses.append(course)

    return course


@app.get("/discussions")
async def get_discussions(course_id: int) -> list[Discussion]:
    response = requests.get(url=f"{base_url}/courses/{course_id}/discussion_topics", headers=headers)
    r_json = response.json()

    discussions: list[Discussion] = []
    for discussion_json in r_json:
        discussion = Discussion(id=discussion_json["id"], title=discussion_json["title"])
        discussions.append(discussion)

    return discussions