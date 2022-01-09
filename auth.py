from flask import Blueprint, render_template, request, flash
from website.modules.supabase import SupaBase
from website.modules.helpers import is_in_database

import datetime


auth = Blueprint('auth', __name__)

@auth.route('/connect', methods=["GET", "POST"])
def connect():
    if request.method == 'GET':
        return render_template("connect.html")
    
    if request.method == 'POST':
        global wallet_address
        wallet_address = request.form['walletaddress']
        
        result = is_in_database(wallet_address)
        if result:
            return render_template("./shorts/wallet_already_connected.html")
        
        if not result:
            return render_template("pick_player.html")
    

@auth.route('/pick_player', methods=["GET", "POST"])
def pick_player():
    return render_template("pick_player.html")


@auth.route('/collect_user_data<player_number>', methods=["GET", "POST"])
def collect_user_data(player_number='x'):
    pic= "./static/images/{}.png".format(player_number)

    imagemas = ['./static/img/0.png', './static/img/1.png', './static/img/2.png', './static/img/3.png', './static/img/4.png',
        './static/img/5.png', './static/img/6.png', './static/img/7.png', './static/img/8.png', './static/img/9.png']

    image1 = ['./static/img/2.png']
    image2 = ['./static/img/0.png']
    image3 = ['./static/img/0.png']
    image4 = ['./static/img/0.png']

    count1 = 2
    count2 = 0
    count3 = 0
    count4 = 0

    image1[0] = imagemas[count1]
    image2[0] = imagemas[count2]
    image3[0] = imagemas[count3]
    image4[0] = imagemas[count4]


    if request.method == "GET":        
        return render_template("collect_user_data.html", number=player_number, pic=pic, wallet_address=wallet_address)
        
    if request.method == "POST":
        
        email = request.form.get('email')
        twitter = request.form.get('twitter')
        telegram = request.form.get('telegram')
        facebook = request.form.get('facebook')
        
        if len(email) == 0 and len(twitter) == 0 and len(telegram) == 0 and len(facebook) == 0:
            flash('at least 1 contact needed', category='error')
            return render_template("collect_user_data.html", number=player_number, pic=pic, wallet_address=wallet_address)
        
        else:
            flash("You are now connected Await further instructions", category='success')
                
            database = SupaBase()
            data = {
                'player_number': player_number,
                'created_at': str(datetime.datetime.now()),
                'twitter': request.form.get('twitter'),
                'telegram': request.form.get('telegram'),
                'facebook': request.form.get('facebook'),
                'email': request.form.get('email'),
                'wallet_address': wallet_address
                }
                

            if count4 == 0:
                    if count1 == 0:
                        if count2 == 0:
                            if count3 == 0:
                                return render_template("base.html", image1=image1[0], image2=image2[0], image3=image3[0], image4=image4[0])
                            else:
                                count3 = count3 - 1
                                count4 = 9
                                image3[0] = imagemas[count3]
                                image4[0] = imagemas[count4]
                        else:
                            if count3 == 0:
                                count2 = count2 - 1
                                count3 = 9
                                count4 = 9
                                image2[0] = imagemas[count2]
                                image3[0] = imagemas[count3]
                                image4[0] = imagemas[count4]
                            else:
                                count3 = count3 - 1
                                count4 = 9
                                image3[0] = imagemas[count3]
                                image4[0] = imagemas[count4]
                    else:
                        if count2 == 0:
                            if count3 == 0:
                                count1 = count1 - 1
                                count2 = 9
                                count3 = 9
                                count4 = 9
                                image1[0] = imagemas[count1]
                                image2[0] = imagemas[count2]
                                image3[0] = imagemas[count3]
                                image4[0] = imagemas[count4]
                            else:
                                count3 = count3 - 1
                                count4 = 9
                                image3[0] = imagemas[count3]
                                image4[0] = imagemas[count4]
                        else:
                            if count3 == 0:
                                count2 = count2 - 1
                                count3 = 9
                                count4 = 9
                                image2[0] = imagemas[count2]
                                image3[0] = imagemas[count3]
                                image4[0] = imagemas[count4]
                            else:
                                count3 = count3 - 1
                                count4 = 9
                                image3[0] = imagemas[count3]
                                image4[0] = imagemas[count4]
            else:
                                    count4 = count4 - 1
                                    image4[0] = imagemas[count4]
                            
            res = database.add_to_table('User_Data', data)

            return render_template("base.html", image1 = image1[0], image2 = image2[0], image3 = image3[0], image4 = image4[0])

        return render_template("home.html")