from flask import Flask, render_template, request

# Globala definicja zmiennych

app = Flask(__name__)

poll_data = {
    'question': 'Pies czy Kot?',
    'fields': ['Pies', 'Kot']
}

# Ponizej funkcje dodatkowe

def add_to_file(content, file_name="data.txt"):
    with open(file_name, "a") as f:
        f.write("{}\n".format(content))


def read_file(file_name="data.txt"):
    with open(file_name, "r") as f:
        data = f.read()
    data = data.split("\n")
    data = clean_data(data)
    return data

def clean_data(data, sign=''):
    for i in range(data.count(sign)):
        data.remove(sign)
    return data

# Ponizej funkcje dla flaska z dekoratorami

@app.route('/')
def root():
    return render_template('poll.html', data=poll_data)


@app.route('/poll')
def poll():
    # Zlap wynik glosowania uzytkownika i zapisz do zmiennej vote
    vote = request.args.get('field')
    # Zapisz wynik do pliku
    add_to_file(vote)

    # Wczytaj wyniki wszystkich uzytkownikow
    votes_data = read_file()

    # Zainicjuj slownik z 0 liczba glosow dla kazdego pola
    votes = {}

    # Zlicz wyniki dla danego wyboru [pies,kot] i wrzuc je do votes
    for field in poll_data['fields']:
        votes[field] = votes_data.count(field)

    return render_template('results.html', data=poll_data, votes=votes)

if __name__ == "__main__":
    app.run(debug=True)
