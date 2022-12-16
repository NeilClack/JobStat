import pytest


def test_get(client):
    """
    GIVEN a request to /api/get
    WHEN no query strings are supplied
    THEN the response should be a JSON list
    AND the JSON list should contain many jobs
    AND status code should be 200
    """

    res = client.get("/api/get")

    assert type(res.json) == list
    assert len(res.json) > 1
    assert res.status_code == 200


def test_get_filter_title(client):
    """
    GIVEN a request to /api/get
    WHEN a query string is provided for title without 'exact' keyword
    THEN the response JSON should only contain jobs with the title query string in the title.
    AND status code should be 200
    """

    res = client.get("/api/get?title=Data")

    for i in res.json:
        assert "Data" in i["title"]

    assert res.status_code == 200


def test_get_filter_title_exact(client):
    """
    GIVEN a request to /api/get
    WHEN a query string is provided for title and the exact keyword is present
    THEN only return results whose title matches the phrase exactly
    AND status code should be 200
    """

    res = client.get("/api/get?title=Data Analyst&exact=true")

    for i in res.json:
        assert i["title"] == "Data Analyst"

    assert res.status_code == 200


@pytest.mark.skip(reason="Company search is currently not working.")
def test_get_company(client):
    """
    GIVEN a request to /api/get
    WHEN a query string is provided for company and the exact keyword is not present
    THEN the results whose company should contain the company name provided
    AND status code should be 200
    """

    res = client.get("/api/get?company=Black")

    for i in res.json:
        assert "Black" in i["company"]

    assert res.status_code == 200


@pytest.mark.skip(reason="Company search is currently not working.")
def test_get_company_exact(client):
    """
    GIVEN a request to /api/get
    WHEN a query string is provided for company and the exact keyword is present
    THEN the results whose company should match the company name provided
    AND status code should be 200
    """

    company = "Black Rifle Coffee"

    res = client.get(f"/api/get?company={company}")

    for i in res.json:
        assert i["company"] == company

    assert res.status_code == 200


def test_get_salary(client):
    """
    GIVEN
    WHEN
    THEN
    """
    pass


def test_get_location(client):
    """
    GIVEN
    WHEN
    THEN
    """
    pass


def test_get_location_exact(client):
    """
    GIVEN
    WHEN
    THEN
    """
    pass


def test_get_summary(client):
    """
    GIVEN
    WHEN
    THEN
    """
    pass


def test_get_posted(client):
    """
    GIVEN
    WHEN
    THEN
    """
    pass


def test_get_posted_range(client):
    """
    GIVEN
    WHEN
    THEN
    """
    pass
