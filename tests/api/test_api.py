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

    assert response.status_code == 201


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

    assert response.status_code == 201


def test_create_add_fail_one(client):
    response = client.post(
        "/api/add",
        json={
            "title": 25,
            "company": 200,
            "location": {"string": "text"},
            "salary": "Notanumber",
            "summary": "This is not a real job listing. Delete this later. DELETE",
            "url": "http://Dontforgettochangethiseachtime",
            "posted": "2022-12-13T00:05:10.442112",
            "scraped": "2022-12-13",
        },
    )

    ve = response.json["ValidationError"]

    assert response.status_code == 400
    assert "ValidationError" in response.json
    assert "title" in ve
    assert "company" in ve
    assert "location" in ve
    assert "salary" in ve
    assert "url" in ve
    assert "posted" in ve
    assert "scraped" in ve


def test_integrity_errors(client):
    response = client.post(
        "/api/add",
        json={
            "company": "Not a real company",
            "location": "Anywhere",
            "salary": 400000,
            "summary": "This is not a real job listing. Delete this later. DELETE",
            "url": "http://Dontforgettochangethiseachtime.com",
            "posted": "2022-12-13",
            "scraped": "2022-12-13T00:05:10.442112",
        },
    )

    # This is a 400 because this can only happen if the request was missing fields.
    assert response.status_code == 400
    assert "IntegrityError" in response.json
