from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import UrlForm
from app.helpers import generate_shortlink, is_valid_url
from app.models import ShortUrl

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = UrlForm()
    # Does all of the form processing work.
    # Returns true if nothing went wrong retrieving the data.
    if form.validate_on_submit(): 
        if is_valid_url(form.url.data):
            shortlink = generate_shortlink()
            shorturl = ShortUrl(shortlink=shortlink, link=form.url.data)
            db.session.add(shorturl)
            db.session.commit()
       
            flash('Request to shorten URL {}'.format(form.url.data))
            flash('At extension {}'.format(shortlink))
            return redirect(url_for('results', link=shortlink))
        else:
            flash('Request to shorten URL {} failed'.format(form.url.data))
            return redirect(url_for('results'))

    return render_template('index.html', form=form)

@app.route('/results')
def results():
    shortlink = None
    if "link" in request.args:
        shortlink = request.args["link"]
    return render_template('success.html', shortlink=shortlink)

@app.route('/<shortlink>')
def redirect_view(shortlink):
    shorturl = ShortUrl.query.filter_by(shortlink=shortlink).first()
    if shorturl is not None:
        return redirect(shorturl.link)
    else:
        return render_template('404.html')
