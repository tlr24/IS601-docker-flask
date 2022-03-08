"""Tests for the html pages"""

def test_request_main_menu_links(client):
    """Tests the main menu links in the nav bar"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a class="nav-link" href="/git">Git</a>' in response.data
    assert b'<a class="nav-link" href="/docker">Docker</a>' in response.data
    assert b'<a class="nav-link" href="/flask">Flask</a>' in response.data
    assert b'<a class="nav-link" href="/cicd">CI/CD</a>' in response.data

def test_request_index(client):
    """Tests the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome!" in response.data

def test_request_git_page(client):
    """Tests the git page"""
    response = client.get("/git")
    assert response.status_code == 200
    assert b"Git" in response.data

def test_request_docker_page(client):
    """Tests the docker page"""
    response = client.get("/docker")
    assert response.status_code == 200
    assert b"Docker" in response.data

def test_request_flask_page(client):
    """Tests the flask page"""
    response = client.get("/flask")
    assert response.status_code == 200
    assert b"Flask" in response.data

def test_request_cicd_page(client):
    """Tests the CI/CD page"""
    response = client.get("/cicd")
    assert response.status_code == 200
    assert b"CI/CD" in response.data

def test_request_page_not_found(client):
    """Tests trying to reach non-existing page"""
    response = client.get("/page5")
    assert response.status_code == 404
