import pytest


@pytest.mark.asyncio
async def test_register_user(client):
    response = await client.post(
        "/api/v1/auth/register",
        json={
            "email": "test@user.com",
            "password": "password123",
            "first_name": "Test",
            "last_name": "User",
            "address": "123 gym strt"
        }
    )

    assert response.status_code == 201
    assert response.json()['email'] == "test@user.com"


@pytest.mark.asyncio
async def test_login_user(client):
    await client.post("api/v1/auth/login", json={
        "email": "login@example.com", "password": "password123",
        "first_name" : "L", "last_name":"U"
    })

    response = await client.post(
        "api/v1/auth/login",
        data={"username":"login@example.com","password":"password123"}
    )
    assert response.status_code == 200
    assert "access_token" in response.json()