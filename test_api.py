import requests
import uuid

ENDPOINT = "https://jsonplaceholder.typicode.com/"


def test_create_post():
    # Generate the payload
    payload = new_post_payload()

    # Send the POST request and capture the response object
    create_post_response = create_post(payload)

    # Now you can assert that the status code is 201 (which means the resource was created)
    assert create_post_response.status_code == 201


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


def new_post_payload():
    body = f'test_body_{uuid.uuid4().hex}'
    title = f'test_title_{uuid.uuid4().hex}'
    return {
        "title": title,
        "body": body,
        "userId": "1"
    }
