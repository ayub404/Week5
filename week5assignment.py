books = ["Moby Dick", "1984", "Dune", "War and Peace"]
counts = [15, 130, 95, 25]
update_info = ["Moby Dick", 20]
unpopular_min = 22
popular_min = 100
new_count = 0


def update_checkout_count(books, counts, book_title, new_count):
    for i in range(len(books)):
        if books[i] == book_title:
            counts[i] = new_count
            return True
    return False

def remove_unpopular_books(books, counts, min_checkouts):
    popular_books = []
    popular_counts = []
    for i in range(len(counts)):
        if counts[i] >= min_checkouts:
            popular_books.append(books[i])
            popular_counts.append(counts[i])
        
    return popular_books, popular_counts
    
    
# print(remove_unpopular_books(books, counts,70))

def categorize_by_popularity(books, counts, popular_threshold):
    popular = []
    regular = []
    
    
    for i in range(len(counts)):
        if counts[i] >= popular_threshold:
            popular.append(books[i])
        else:
            regular.append(books[i])
   
    return popular, regular
    


# print( categorize_by_popularity(books, counts, 120))

def analyze_library_stock(initial_books, initial_counts, book_to_update, unpopular_threshold, popular_threshold):
    books_copy = initial_books[:]
    counts_copy = initial_counts[:]
   
   
    book_title, new_count = book_to_update
    

    if not update_checkout_count(books_copy, counts_copy, book_title, new_count):
        print(f"Warning: Book '{book_title}' not found in the library.")
    

    cleaned_books, cleaned_counts = remove_unpopular_books(books_copy, counts_copy, unpopular_threshold)

    popular_books, regular_books = categorize_by_popularity(cleaned_books, cleaned_counts, popular_threshold)



    return popular_books, regular_books
    
popular, regular = analyze_library_stock(books, counts, update_info, unpopular_min, popular_min)

print(f"popular: {popular}")
print(f"regular: {regular}")