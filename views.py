from flask import Blueprint, render_template
from website.modules.supabase import SupaBase

import pprint

views = Blueprint('views', __name__)

@views.route('/')
def home():
	return render_template("home.html")

@views.route('/see_players')
def see_players():
    return render_template("see_players.html")


@views.route('/see_player_data<number>')
def see_player_data(number):
    db = SupaBase()
    pic= "./static/images/{}.png".format(number)
    
    player_data = db.read_table('User_Data')
    for i in player_data:
        if i['player_number'] == number:
            pprint.pprint(i)
            email = i['email']
            twitter = i['twitter']
            telegram = i['telegram']
            facebook = i['facebook']
            wallet_address = i['wallet_address']

            return render_template("see_player_data.html", number=number, pic=pic, email=email, twitter=twitter, telegram=telegram, facebook=facebook, wallet_address=wallet_address)
    
    return render_template("see_players.html")





@views.route('/prize')
def prize():
  return render_template("prize.html")

@views.route('/games')
def games():
  return render_template("games.html")
