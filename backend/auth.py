from flask import Blueprint, session, redirect, request, flash
from .oauth import VKSignIn
import json

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    vk = VKSignIn.get_instance('vk')
    data = vk.authorize()
    return redirect(data.geturl())


@auth.route('/authorize')
def authorize():
    code = request.args['code']
    vk = VKSignIn.get_instance('vk')

    response = vk.authorize_access_token(code)
    data = json.loads(response.data.decode('utf8'))
    if "error" in data:
        flash(data.get("error"))
        flash(data.get("error_description"))
        return redirect('/')

    session['vk_access_token'] = data['access_token']
    session.permanent = True
    return redirect('/')


@auth.route('/logout')
def logout():
    session.clear()
    return redirect('/')
