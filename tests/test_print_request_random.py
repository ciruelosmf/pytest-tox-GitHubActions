


from random_int_req.print_request_random import make_request_to_url
import pytest
import requests

@pytest.fixture
def url():
    return 'https://www.random.org/integers/?num=1&min=1&max=6&col=5&base=10&format=plain&rnd=new'

def test_make_request_to_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            if response.content.decode('utf-8').strip() == "1":
                return 1
            else:
                print("response.content.decode", response.content.decode('utf-8'))

                return 0
        else:
            print("Error: Unable to fetch data from the URL", response.content.decode('utf-8'))
            return 0
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return 0
# Example usage:


def main():
    assert test_make_request_to_url(url) is 1
    assert test_make_request_to_url(url) is 0


if __name__== '__main__':
    main()
    