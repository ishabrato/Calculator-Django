from django.shortcuts import render


# Create your views here.

def index(request):

    return render(request, 'index.html')
def convert(value):
    if isinstance(value, float):
        if value.is_integer():
            return int(value)
        else:
            return value
    else:
        return value
def calculation(request):

    try:
        if request.method=="POST":
            values=request.POST['values'] 
            print(values)
            final_result = convert(eval(values))
            print(final_result)
            return render(request,'index.html',{'result':final_result,'values':values})
    except :    # noqa: E722
        return render(request,'index.html',{'result':"Error",'values':values})