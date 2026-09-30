def library_books_view(request):
 books = Book.objects.all()
 context = {'books': books}
 return render(request, 'library/books.html', context)