from __future__ import absolute_import
from celery import shared_task
from engine.models import Post, GlobalId, Reply

@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def add_post(g_id, author_name, author_email, post_subject, post_body, image):
    p = Post(post_id=g_id, author_name=author_name, author_email=author_email, post_subject=post_subject,
             post_body=post_body, image=image)
    p.save()
    gid = GlobalId(global_id=g_id)
    gid.save()
    return 0


@shared_task
def add_reply(g_id, param, reply_name, reply_email, reply_body, image):
    p = Reply(reply_id=g_id, op_post_id=param, reply_name=reply_name, reply_email=reply_email,
              reply_body=reply_body, image=image)
    p.save()
    gid = GlobalId(global_id=g_id)
    gid.save()
    return 0

