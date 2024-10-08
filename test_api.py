import requests
import uuid

ENDPOINT = "https://jsonplaceholder.typicode.com/"


def test_create_post():
    payload = new_post_payload()
    create_post_response = create_post(payload)
    assert create_post_response.status_code == 201
    created_post = create_post_response.json()
    assert created_post['title'] == payload['title']
    assert created_post['body'] == payload['body']
    assert created_post['userId'] == payload['userId']


def test_update_post():
    id = "1"
    updated_payload = {
        'title': 'Updated Title',
        'body': 'Updated body content',
        'userId': id
    }

    update_response = put_post_by_id(id, updated_payload)
    assert update_response.status_code == 200

    updated_post = update_response.json()
    assert updated_post['title'] == updated_payload['title']
    assert updated_post['body'] == updated_payload['body']
    assert updated_post['userId'] == updated_payload['userId']


def test_patch_post():
    id = "1"
    updated_payload = {
        'title': 'patched Title'
    }

    update_response = patch_post_by_id(id, updated_payload)
    assert update_response.status_code == 200

    updated_post = update_response.json()
    assert updated_post['title'] == updated_payload['title']


def test_get_all_posts():
    get_response = get_posts()
    assert get_response.status_code == 200

    posts = get_response.json()
    assert isinstance(posts, list)

    assert len(posts) > 0
    first_post = posts[0]
    assert 'title' in first_post
    assert 'body' in first_post
    assert 'userId' in first_post


def create_post(payload):
    headers = {
        'Content-type': 'application/json; charset=UTF-8'
    }
    response = requests.post(
        f'{ENDPOINT}/posts', json=payload, headers=headers)
    return response


def get_posts():
    return requests.get(ENDPOINT + "/posts")


def get_post_by_id(id):
    return requests.get(ENDPOINT + f"/posts/{id}")


def get_comments_by_post_id(postId):
    return requests.get(ENDPOINT + f"/posts/{postId}/comments")


def put_post_by_id(id, updated_data):
    headers = {'Content-type': 'application/json; charset=UTF-8'}
    response = requests.put(
        ENDPOINT + f"/posts/{id}", json=updated_data, headers=headers)
    return response


def patch_post_by_id(id, updated_data):
    headers = {'Content-type': 'application/json; charset=UTF-8'}
    response = requests.patch(
        ENDPOINT + f"/posts/{id}", json=updated_data, headers=headers)
    return response


def new_post_payload():
    body = f'test_body_{uuid.uuid4().hex}'
    title = f'test_title_{uuid.uuid4().hex}'
    return {
        "title": title,
        "body": body,
        "userId": "1"
    }
