"""Tests for the html pages"""

def test_request_main_menu_links(client):
    """Tests the main menu links in the nav bar"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a class="nav-link" href="/oop_terms">OOP Terms</a>' in response.data
    assert b'<a class="nav-link" href="/aaa">AAA Testing</a>' in response.data
    assert b'<a class="nav-link" href="/oop_principles">OOP Principles</a>' in response.data
    assert b'<a class="nav-link" href="/solid">SOLID</a>' in response.data
    assert b'<a class="dropdown-item" href="/git">Git</a>' in response.data
    assert b'<a class="dropdown-item" href="/docker">Docker</a>' in response.data
    assert b'<a class="dropdown-item" href="/flask">Flask</a>' in response.data
    assert b'<a class="dropdown-item" href="/cicd">CI/CD</a>' in response.data

def test_request_index(client):
    """Tests the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome!" in response.data

def test_request_oop_terms_page(client):
    """Tests the OOP terms page"""
    response = client.get("/oop_terms")
    assert response.status_code == 200
    assert b"OOP Terms" in response.data

def test_request_aaa_testing_page(client):
    """Tests the AAA Testing page"""
    response = client.get("/aaa")
    assert response.status_code == 200
    assert b"AAA Testing" in response.data

def test_request_oop_principles_page(client):
    """Tests the OOP principles page"""
    response = client.get("/oop_principles")
    assert response.status_code == 200
    assert b"OOP Principles" in response.data

def test_request_solid_page(client):
    """Tests the SOLID page"""
    response = client.get("/solid")
    assert response.status_code == 200
    assert b"SOLID" in response.data

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
