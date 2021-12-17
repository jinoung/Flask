from flask import Blueprint, render_template, request, url_for, g, flash

from ..forms import NoticeForm
from werkzeug.utils import redirect
from datetime import datetime
from .. import db
from bbs.models import Notice
from bbs.views.auth_views import login_required

bp = Blueprint('notice', __name__, url_prefix='/notice')


@bp.route('/list/')
def _list():
    page = request.args.get('page', type=int, default=1)
    notice = Notice.query.order_by(Notice.create_date.desc())
    notice = notice.paginate(page, per_page=10)
    return render_template('notice/notice_list.html', data=notice)

@bp.route('/detail/<int:notice_id>/')
def detail(notice_id):
    notice = Notice.query.get_or_404(notice_id)
    return render_template('notice/notice_detail.html', data=notice)

@bp.route('/create/', methods=('GET', 'POST'))
@login_required
def create():
    form = NoticeForm()
    if request.method == 'POST' and form.validate_on_submit():
        notice = Notice(subject=form.subject.data, content=form.content.data, create_date=datetime.now(), user=g.user)
        db.session.add(notice)
        db.session.commit()
        return redirect(url_for('main.index'))
    else:
        return render_template('notice/notice_create.html', form=form)

@bp.route('/update/<int:notice_id>/', methods=('GET', 'POST'))
def update(notice_id):
    notice = Notice.query.get_or_404(notice_id)
    if g.user != notice.user:
        flash('수정권한이 없어요')
        return redirect(url_for('notice.detail', notice_id=notice_id))
    if request.method == 'POST':
        form = NoticeForm()
        if form.validate_on_submit():
            form.populate_obj(notice)
            notice.edit_date = datetime.now()
            db.session.commit()
            return redirect(url_for('notice.detail', notice_id=notice_id))
    else:
        form = NoticeForm(obj=notice)
    return render_template('notice/notice_create.html', form=form)

@bp.route('/delete/<int:notice_id>')
@login_required
def delete(notice_id):
    notice = Notice.query.get_or_404(notice_id)
    if g.user != notice.user:
        flash('삭제권한이 없습니다')
        return redirect(url_for('notice.detail', notice_id=notice_id))
    db.session.delete(notice)
    db.session.commit()
    return redirect(url_for('notice._list'))