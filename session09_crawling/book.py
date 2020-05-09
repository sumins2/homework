def extract_info(book_list):

    result = []

    for book in book_list:

        title = book.find("a", {"class" : "N=a:bta.title"}).string
        image = book.find("img")["src"]
        link = book.find("div", {"class" : "thumb_type thumb_type2"}).find("a")["href"]        
        author = book.find("a",{"class" : "txt_name N=a:bta.author"}).string
        publisher = book.find("a", {"class" : "N=a:bta.publisher"}).text
        # price_box = book.find("em",{"class" : "price"}).text.strip()
        #     if price != None:
        #         pirce = price_box.string
        #     else:
        #         price = '없음'
        
        
        book_info = {
            'title' : title,
            'image' : image,
            'link' : link,
            'author' : author,
            'publisher' : publisher,
            # 'price_box' : price_box,
                   
        }
        result.append(book_info)
    return result
    print(result)