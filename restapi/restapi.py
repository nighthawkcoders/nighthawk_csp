from flask import Blueprint, render_template
import requests

restapi_bp = Blueprint('restapi', __name__,
                       url_prefix='/restapi',
                       template_folder='templates',
                       static_folder='static', static_url_path='assets')


@restapi_bp.route('/joke', methods=['GET', 'POST'])
def joke():
    # call to random joke web api
    url = 'https://official-joke-api.appspot.com/jokes/programming/random'
    response = requests.get(url)
    # formatting variables from return
    setup = response.json()[0]['setup']
    punchline = response.json()[0]['punchline']
    return render_template("restapi/joke.html", setup=setup, punchline=punchline)


@restapi_bp.route('/covid19', methods=['GET', 'POST'])
def covid19():
    url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api"

    headers = {
        'x-rapidapi-key': "dec069b877msh0d9d0827664078cp1a18fajsn2afac35ae063",
        'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)
    world = response.json().get('world_total')
    countries = response.json().get('countries_stat')
    """
    print(world['total_cases'])
    for country in countries:
        print(country["country_name"])
    #return countries
    """
    return render_template("restapi/covid19.html", world=world, countries=countries)
