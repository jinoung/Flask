from flask import Blueprint, render_template, request, url_for
from ..forms import QuestionForm
from werkzeug.utils import redirect
from datetime import datetime
from .. import db
from bbs.models import Notice

bp = Blueprint('notice', __name__, url_prefix='/notice')


@bp.route('/list/')
def _list():
    page = request.args.get('page', type=int, default=1)
    notice = Notice.query.order_by(Notice.create_date.desc())
    notice = notice.paginate(page, per_page=20)
    return render_template('notice/notice_list.html', data=notice)

@bp.route('/detail/<int:notice_id>/')
def detail(notice_id):
    notice = Notice.query.get_or_404(notice_id)
    return render_template('notice/notice_detail.html', data=notice)

@bp.route('/create/', methods=('GET', 'POST'))
def create():
    form = QuestionForm()
    if request.method == 'POST' and form.validate_on_submit():
        notice = Notice(subject=form.subject.data, content=form.content.data, create_date=datetime.now())
        db.session.add(notice)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('notice/notice_create.html', form=form)

@bp.route('/update/<int:notice_id>/', methods=('GET', 'POST'))
def update(notice_id):
    notice = Notice.query.get_or_404(notice_id)
    #form = QuestionForm()
    if request.method == 'POST':
        form = QuestionForm()
        if form.validate_on_submit():
            form.populate_obj(notice)
            notice.edit_date = datetime.now()
            db.session.commit()
            return redirect(url_for('notice.detail', notice_id=notice_id))
    else:
        form = QuestionForm(obj=notice)
    return render_template('notice/notice_update.html', form=form)
