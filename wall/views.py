from django.shortcuts import render
from django.views.generic import ListView, FormView, View
from django.core.paginator import Paginator
from wall.models import Message, Comment
from wall.forms import MessageForm, CommentForm, MessageChangeForm, CommentChangeForm



class Wall(ListView):
    template_name = 'wall/message_list.html'
    queryset = Message.objects.all().order_by('created')
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        queryset = []
        messages = Message.objects.all().order_by('-created')
        paginator = Paginator(messages, self.paginate_by)
        page = paginator.page(self.request.GET.get('page', 1))
        for message in page:
            msg_dict = dict()
            msg_dict['message'] = message
            comment = Comment.objects.filter(message=message)
            msg_dict['comment'] = comment
            queryset.append(msg_dict)

        context['messages'] = queryset
        context['page'] = page
        context['page_name'] = 'wall'
        return context


class MessageCreate(FormView):
    form_class = MessageForm
    success_url = '/'
    template_name = 'wall/message_list.html'

    def form_valid(self, form):
        if form.is_valid():
            form.save(commit=True)
        return super().form_valid(form)


class MessageChange(FormView):
    form_class = MessageChangeForm
    success_url = '/'
    template_name = 'wall/message_list.html'

    def form_valid(self, form):
        if form.is_valid():
            form.save(commit=True)
        return super().form_valid(form)


class CommentCreate(FormView):
    form_class = CommentForm
    success_url = '/'
    template_name = 'wall/message_list.html'

    def form_valid(self, form):
        if form.is_valid():
            form.save(commit=True)
        return super().form_valid(form)


class CommentChange(FormView):
    form_class = CommentChangeForm
    success_url = '/'
    template_name = 'wall/message_list.html'

    def form_valid(self, form):
        if form.is_valid():
            form.save(commit=True)
        return super().form_valid(form)


class NextPage(View):
    paginate_by = 3

    def post(self, request):
        num_page = request.POST.get('page', 1)
        queryset = []

        if num_page == 'all':
            page = Message.objects.all().order_by('-created')
        else:
            messages = Message.objects.all().order_by('-created')
            paginator = Paginator(messages, self.paginate_by)
            page = paginator.page(int(num_page))

        for message in page:
            msg_dict = dict()
            msg_dict['message'] = message
            comment = Comment.objects.filter(message=message)
            msg_dict['comment'] = comment
            queryset.append(msg_dict)

        context = dict()
        context['messages'] = queryset
        context['page'] = page
        return render(request, 'wall/message_block.html', context)
