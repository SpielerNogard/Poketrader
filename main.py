########################################################################################
######################          Import packages      ###################################
########################################################################################
from Poketrader import Poketrader
from flask import Blueprint, render_template, flash ,url_for
from flask_login import login_required, current_user
from __init__ import create_app, db, BOB

########################################################################################

# our main blueprint
main = Blueprint('main', __name__)

@main.route('/') # home page that return 'index'
def index():
    randoms = BOB.give_random_searchs_and_offers()
    searches = randoms[0]
    offers = randoms[1]
    #return render_template('index.html')
    return(render_template('index.html',suchen = searches, angebote = offers)) 
    
@main.route('/profile') # profile page that return 'profile'
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/trades') # The trade page for the User'
@login_required
def trades():
    return render_template('profile.html', name=current_user.name)

app = create_app() # we initialize our flask app using the __init__.py function
if __name__ == '__main__':
    db.create_all(app=create_app()) # create the SQLite database
    app.run(debug=True) # run the flask app on debug mode