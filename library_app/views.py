from django.shortcuts import render
from .models import User, Book, Borrow
from datetime import datetime

def Home(request):
    return render(request, 'home.html')

def Write(request):
    users = User.objects.all()
    books = Book.objects.all()
    if request.method == 'POST':
        if 'user_submit' in request.POST:
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            User.objects.create(name=name, email=email, phone=phone)

        elif 'book_submit' in request.POST:
            title = request.POST.get('title')
            author = request.POST.get('author')
            isbn = request.POST.get('isbn')
            Book.objects.create(title=title, author=author, isbn=isbn)

        elif 'borrow_submit' in request.POST:
            user_id = request.POST.get('user_id')
            book_id = request.POST.get('book_id')
            return_date_str = request.POST.get('return_date')  
            if(return_date_str):
                return_date = datetime.strptime(return_date_str, "%Y-%m-%d").date()
            else:
                return_date = None
            # Convert IDs into actual objects from the database
            user = User.objects.get(user_id=user_id)
            book = Book.objects.get(book_id=book_id)
            
            # Create a Borrow entry
            Borrow.objects.create(user_id=user, book_id=book, return_date=return_date)

        elif 'return_submit' in request.POST:
            user_id = request.POST.get('user_id')
            book_id = request.POST.get('book_id')
            return_date_str = request.POST.get('return_date')  

            return_date = datetime.strptime(return_date_str, "%Y-%m-%d").date() if return_date_str else None

            # Get the actual objects
            user = User.objects.get(user_id=user_id)
            book = Book.objects.get(book_id=book_id)

            # Find the active borrow (return_date is None) for this user + book
            try:
                borrow = Borrow.objects.filter(user_id=user, book_id=book, return_date__isnull=True).latest('borrow_id')
                # Update return date
                borrow.return_date = return_date
                borrow.save()
            except Borrow.DoesNotExist:
                # No active borrow exists → optional: show error or create a new record
                pass  # or Borrow.objects.create(user_id=user, book_id=book, return_date=return_date)

    return render(request, 'Write.html', {'users': users, 'books': books})



def Read(request):
    user = User.objects.all()
    book = Book.objects.all()
    borrow = Borrow.objects.all()
    return render(request, 'Read.html', {
        'users': user,
        'books': book,
        'borrows': borrow,
})

def Delete(request):
    users = User.objects.all()
    books = Book.objects.all()

    if request.method == 'POST':
        if 'user_submit' in request.POST:
            user_id = request.POST.get('user_id')
            if user_id:
                User.objects.filter(user_id=user_id).delete()
        if 'book_submit' in request.POST:
            book_id = request.POST.get('book_id')
            if book_id:
                Book.objects.filter(book_id=book_id).delete()
        
    return render(request, 'Delete.html', {'users': users, 'books': books})
