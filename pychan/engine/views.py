# -*- coding: utf-8 -*-

# Create your views here.

from django.shortcuts import render_to_response
import sys
from engine.models import Post, Reply, GlobalId
from engine.forms import PostForm, ReplyForm
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.db.models import Max
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def GetLastGet():
    global_id = GlobalId.objects.all().aggregate(Max('global_id'))
    if global_id['global_id__max'] is None:
        return 0
    else:
        return global_id['global_id__max']


def ShowPostForm(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            g_id = GetLastGet()
            g_id += 1
            author_name = form.cleaned_data['author_name']
            author_email = form.cleaned_data['author_email']
            post_subject = form.cleaned_data['post_subject']
            post_body = form.cleaned_data['post_body']
            image = form.cleaned_data['image']
            p = Post(post_id=g_id, author_name=author_name, author_email=author_email, post_subject=post_subject,
                     post_body=post_body, image=image)
            p.save()
            gid = GlobalId(global_id=g_id)
            gid.save()
            return HttpResponseRedirect('')
    else:
        form = PostForm()
    post_list = Post.objects.all()
    paginator = Paginator(post_list.reverse(), 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render_to_response('b.html', {
        'form': form,
        'post_list': post_list,
        'posts': posts,
    }, context_instance=RequestContext(request))


def ShowReplyForm(request):
    if request.method == 'POST':
        form = ReplyForm(request.POST, request.FILES)
        param = request.GET.get('to', '')
        if form.is_valid():
            g_id = GetLastGet()
            if g_id == 1:
                pass
            else:
                g_id += 1
            reply_name = form.cleaned_data['reply_name']
            reply_email = form.cleaned_data['reply_email']
            reply_body = form.cleaned_data['reply_body']
            image = form.cleaned_data['image']
            p = Reply(reply_id=g_id, op_post_id=param, reply_name=reply_name, reply_email=reply_email,
                      reply_body=reply_body, image=image)
            p.save()
            gid = GlobalId(global_id=g_id)
            gid.save()
            return HttpResponseRedirect('')

    if request.method == 'GET':
        form = ReplyForm
        param = request.GET.get('to', '')
        p = Post.objects.get(post_id=param)
        r = Reply.objects.filter(op_post_id=param)
        return render_to_response('reply.html', {
            'param' : param,
            'form' : form,
            'p' : p,
            'r' : r,
        }, context_instance=RequestContext(request))