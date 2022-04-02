def pageCount(n, p):
    page_in_book=p//2
    total_pages=n//2
    front_pages=page_in_book
    from_back=total_pages - page_in_book
    return min(front_pages,from_back)
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()