import json
import pytest
from utils import make_request, verify


@pytest.mark.smoke
@pytest.mark.parametrize("endpoint, expected_response_code", [("posts", 200),
                                                              ("/posts/1", 200),
                                                              ("/posts/1/comments", 200),
                                                              ("/comments?postId=1", 200),
                                                              ("comments", 200),
                                                              ("albums", 200),
                                                              ("photos", 200),
                                                              ("todos", 200),
                                                              ("users", 200)])
def test_get_apis(api, endpoint, expected_response_code):
    verify.assert_status_code("GET {}{}".format(api, endpoint), expected_response_code,
                              make_request.make_request("GET", api + endpoint).status_code)


@pytest.mark.regression
def test_post_call(api, posts, header):
    response = make_request.make_request("POST", url=api + "posts", data=json.dumps(posts), header=header)
    assert response.status_code == 201
    assert response.json()['id'] == 101
    assert response.json()['userId'] == posts.get('userId')


@pytest.mark.regression
def test_put_call(api, posts, header):
    posts['title'] = 'PMI'
    response = make_request.make_request("PUT", url=api + "posts/1", data=json.dumps(posts), header=header)
    assert response.status_code == 200
    assert response.json()['id'] == 1
    assert response.json()['title'] == 'PMI'


@pytest.mark.regression
def test_patch_call(api, header):
    data = {'title': 'foo3'}
    response = make_request.make_request("PATCH", url=api + "posts/1", data=json.dumps(data), header=header)
    assert response.status_code == 200
    assert response.json()['id'] == 1
    assert response.json()['title'] == 'foo3'


@pytest.mark.regression
def test_delete_call(api):
    response = make_request.make_request("DELETE", url=api + "posts/1")
    assert response.status_code == 200


@pytest.mark.negative
def test_invalid_url(api):
    response = make_request.make_request("GET", url=api + "/poster")
    assert response.status_code == 404


@pytest.mark.negative
def test_invalid_data(api, header):
    response = make_request.make_request("POST", url=api + "posts", data="abc", header=header)
    assert response.status_code == 400


@pytest.mark.regression
def test_jph_user():
    endpoint = "https://jsonplaceholder.typicode.com/users/1"
    response = make_request.make_request("GET", url=endpoint)
    assert response.status_code == 200


@pytest.mark.regression
def test_jph_user_2():
    endpoint = "https://jsonplaceholder.typicode.com/users/2"
    response = make_request.make_request("GET", url=endpoint)
    assert response.status_code == 200