from flask import Blueprint, request
from requests import get
from function_jwt import validate_token

users_github = Blueprint("users_github", __name__)

# primer paso de verificacion de token


@users_github.before_request
def verify_token_middleware():
    token = request.headers['Authorization'].split(" ")[1]
    validate_token(token, output=False)

# una vez verificado viene a esta funcion


@users_github.route("/github/users", methods=['POST'])
def github():
    data = request.get_json()
    country = data['country']
    return get(f'https://api.github.com/search/users?q=location:"{country}"&page=1').json()
