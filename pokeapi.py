from flask import render_template
import pokebase as pb

from flask import Flask
app = Flask(__name__)


@app.route('/pokemon/page/<int:page>')
def get_pokemon(page):
    pokemons = []
    page_size = 6
    start = (page - 1) * page_size
    end = start + page_size
    total_pokemons = 300
    total_pages = total_pokemons // page_size + 1
    for i in range(start + 1, end + 1):
        pokemons.append(pb.pokemon(i))
    return render_template('index.html', pokemons=pokemons, total_pages=total_pages, current_page=page, page_size=page_size)


if __name__ == '__main__':
    app.run(debug=True)