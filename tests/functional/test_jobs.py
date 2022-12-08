import json
from datetime import datetime


def test_index(client):
    """
    GIVEN a Flask application
    WHEN a get request is made to '/'
    THEN check that the index.html file has been rendered, and the status_code is 200 ok
    """

    res = client.get("/")

    assert res.status_code == 200
    assert b"JobStats" in res.data


def test_jobs_get(client):
    """
    GIVEN a flask application
    WHEN a request is made to '/jobs' (GET)
    THEN check that the response contains JSON relating to jobs
    """

    res = client.get("/jobs")
    # Verify status code
    assert res.status_code == 200
    # Verify the response contains JSON
    assert res.json != None
    # Verify the JSON is valid
    assert json.dumps(res.json)


def test_jobs_post(client):
    """
    GIVEN a flask application and a valid JSON representation of a job listing
    WHEN a POST request is made to '/jobs'
    THEN ccheck that the application accepts the JSON and returns it unchanged.
    """
    json_data = {
        "title": "Data Analyst",
        "company": "Ally Financial",
        "url": "https://www.indeed.com",
        "location": "Remote",
        "salary": 90000,
        "summary": "Lorem Ipsum",
        "posted": "2022-11-09",
        "entered": "2022-11-10 16:11:03.369562"
    }
    
    headers = {
        'Content-Type': 'application/json'
    }

    res = client.post("/jobs", headers=headers)

    assert res.status_code == 200
