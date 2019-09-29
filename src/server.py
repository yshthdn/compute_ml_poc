from flask import render_template
import connexion

application=app = connexion.App(__name__, specification_dir="./")

# app.add_api('swagger.yml')
app.add_api('compute_forcast.yml')

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
