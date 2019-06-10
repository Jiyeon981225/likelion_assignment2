from django.shortcuts import render

def home(request):
    return render(request, 'wordcount/home.html')
#template receives a as 'a'
    
def list(request):
    return render(request, 'wordcount/list.html')
    
def result(request):
    text = request.GET['fulltext']
    words = text.split()
    word_dic={}
    for x in words:
        if x in word_dic:
            word_dic[x] += 1
        else:
            word_dic[x]=1
    
    return render(request, 'wordcount/result.html', {'total':text, 'dic': word_dic.items()})