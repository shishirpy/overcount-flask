from flask import render_template, flash, url_for, request
from .. import db
from ..models import Count
from . import bp
from .forms import CounterForm


@bp.route("/", methods=['GET', 'POST'])
def index():
    form = CounterForm()
    if request.args.get('locale') == 'hi':
        return render_template("index_hn.html", form = form)
    else:
        if form.validate_on_submit():
            data = form.data
            count = Count(author_id=1,
                    fat_count=data.get('fatality_count'),
                    inf_count=data.get('infection_count'),
                    lat=data.get('lat'),
                    long=data.get('long'))

            db.session.add(count)
            db.session.commit()
            print(count)

            return render_template("index.html", form=form)
        return render_template("index.html", form=form)

