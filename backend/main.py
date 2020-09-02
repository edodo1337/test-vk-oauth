from flask import Blueprint, render_template, session, redirect
from . import create_app
from .oauth import VKSignIn
import os

main = Blueprint('main', __name__)


@main.route('/')
def index():
    vk = VKSignIn.get_instance('vk')
    context = {}
    if "vk_access_token" in session:
        response = vk.get_info(access_token=session["vk_access_token"])
        if response is None:
            return redirect("/")
        data = response
        context.update({'id': data['id'], 'first_name': data['first_name'], 'last_name': data['last_name'],
                        'is_authenticated': True,
                        'avatar': data['photo_200'], 'friends': data['friends']})

    return render_template('index.html', context=context)


@main.route('/profile')
def profile():
    return render_template('profile.html')

