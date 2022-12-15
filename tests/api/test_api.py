import pytest


def test_create_add_one(client):
    response = client.post(
        "/api/add",
        json={
            "title": "Delete",
            "company": "Not a real company",
            "location": "Anywhere",
            "salary": 400000,
            "summary": "This is not a real job listing. Delete this later. DELETE",
            "url": "http://Dontforgettochangethiseachtime.com",
            "posted": "2022-12-13",
            "scraped": "2022-12-13T00:05:10.442112",
        },
    )

    assert response.status_code == 200


def test_create_add_many(client):
    response = client.post(
        "/api/add",
        json=[
            {
                "title": "Delete",
                "company": "Not a real company",
                "location": "Anywhere",
                "salary": 400000,
                "summary": "This is not a real job listing. Delete this later. DELETE",
                "url": "http://Dontforgettochangethiseachtime.com",
                "posted": "2022-12-13",
                "scraped": "2022-12-13T00:05:10.442112",
            },
            {
                "title": "Delete",
                "company": "Not a real company",
                "location": "Anywhere",
                "salary": 400000,
                "summary": "This is not a real job listing. Delete this later. DELETE",
                "url": "http://Dontforgettochangethiseachtime.com",
                "posted": "2022-12-13",
                "scraped": "2022-12-13T00:05:10.442112",
            },
        ],
    )

    assert response.status_code == 200


def test_create_add_fail_one(client):
    response = client.post(
        "/api/add",
        json={
            "title": 25,
            "company": "Not a real company",
            "location": "anywhere",
            "salary": 400000,
            "summary": "This is not a real job listing. Delete this later. DELETE",
            "url": "http://Dontforgettochangethiseachtime.com",
            "posted": "2022-12-13",
            "scraped": "2022-12-13T00:05:10.442112",
        },
    )

    assert response.status_code == 200
