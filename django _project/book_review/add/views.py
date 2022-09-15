from django.shortcuts import render
from .models import Comment, Book
from account.models import User
from django.contrib import messages
from .form import AddBookForm, AddCommentForm

def add_book(request):
    if request.method == "POST":
        add_book = AddBookForm(request.POST, request.FILES)
        if add_book.is_valid():
            new_book = add_book.cleaned_data
            Book.objects.create(name = new_book['name'], author = new_book['author'], translator = new_book['translator'], year = new_book['year'], genre = new_book['genre'], summary = new_book['summary'], cover =new_book['cover'])
            messages.success(request, 'done', 'done')   
    else:
        add_book = AddBookForm()
    return render(request, 'add_book.html')

def add_comment(request, get_book_id):
    if request.method == "POST":
        add_comment = AddCommentForm(request.POST)
        if add_comment.is_valid():
            new_comment = add_comment.cleaned_data 
            if User.objects.filter(name = new_comment['user_name']).exists():
                user_info = User.objects.filter(name = new_comment['user_name'], email = new_comment['user_email']).values('id', 'comment_count')
                if user_info.exists():
                    Comment.objects.create(comment = new_comment['comment'], book_id = get_book_id, user_id = user_info[0]['id']) 
                    User.objects.filter(id = user_info[0]['id']).update(comment_count = user_info[0]['comment_count'] + 1 )
                else:
                    messages.error(request, 'wrong email', 'email_message')
            else:
                messages.error(request, 'name does\'t exist', 'name_message')     
    else:
        add_comment = AddCommentForm()
        
    book_info = Book.objects.filter(id = get_book_id) 
    comment = Comment.objects.filter(book_id = get_book_id).values('comment', 'date', 'user_id')
    comments = []
    for i in comment:
        user_name = User.objects.filter(id = i['user_id']).values('name')
        for j in user_name:
            comments.append(i | j)

    return render(request, 'add_comment.html', {'book_info':book_info, 'comments':comments})
