from django.shortcuts import render


# Create your views here.
def count(request):
    return render(request, 'count.html')

def result(request):
    text = request.POST['text']
    total_len = len(text)
    no_blank_len = len(text.replace(" ",""))
    word_num = text.split(" ")
    number_of_words = len(word_num)
    return render(request,'result.html', {
        'total_len' : total_len,
        'text' : text,
        'no_blank_len' : no_blank_len,
        'word_num' : word_num,
        'number_of_words' : number_of_words
    })