from django.shortcuts import render

import re


# Create your views here.

def index(request):

    return render(request, 'index.html')


def jls_extract_def():
    # noqa: E722
    return 

def convert(value):
    if isinstance(value, float):
        if value.is_integer():
            return int(value)
        else:
            return float(value)
    else:
        return value
def calculation(request):

    try:

        if request.method=="POST":

           values=request.POST['values'] #string having whole ques
           print(values)

           vals=re.findall(r"(\d+)",values) #extract values

           operators=['+','*','/','-','.','%']
           opr=[]

           for v in values:

            for o in operators:

                if v==o:

                    opr.append(o)

           print(opr)                      #extrect operators

           print(re.findall(r"(\d+)",values))


           for o in opr:

               if o=='.':

                  i=opr.index(o)

                  res=vals[i]+"."+vals[i+1]

                  vals.remove(vals[i+1])

                  opr.remove(opr[i])
                  vals[i]=res
                  print(vals)
                  print(opr)

           for o in opr:

            if o=='%':

                i=opr.index(o)

                res=(float(vals[i])/100)*float(vals[i+1])

                vals.remove(vals[i+1])

                opr.remove(opr[i])
                vals[i]=res
                print(vals)
                print(opr)

           for o in opr:

            if o=='/':

                i=opr.index(o)

                res=float(vals[i])/float(vals[i+1])

                vals.remove(vals[i+1])

                opr.remove(opr[i])
                vals[i]=str(res)
                print(vals)
                print(opr)

           for o in opr:

            if o=='*':

                i=opr.index(o)

                res=float(vals[i])*float(vals[i+1])

                vals.remove(vals[i+1])

                opr.remove(opr[i])
                vals[i]=str(res)
                print(vals)
                print(opr)

           for o in opr:

            if o=='+':

                i=opr.index(o)

                res=float(vals[i])+float(vals[i+1])

                vals.remove(vals[i+1])

                opr.remove(opr[i])
                vals[i]=str(res)
                print(vals)
                print(opr)

            if o=='-':

                i=opr.index(o)

                res=float(vals[i])-float(vals[i+1])

                vals.remove(vals[i+1])

                opr.remove(opr[i])
                vals[i]=str(res)
                print(vals)
                print(opr)

        if len(opr)!=0:

            if opr[0]=='/':

                result = float(vals[0])/float(vals[1])

            elif opr[0]=='*':

                result = float(vals[0])*float(vals[1])

            elif opr[0]=='+':

                result = float(vals[0])+float(vals[1])

            else :

                result = float(vals[0])-float(vals[1])

        else:

            result = float(vals[0])


        final_result = round(result,2)
        final_result = convert(final_result)

        print(final_result)

        return render(request,'index.html',{'result':final_result,'values':values})

    except :  # noqa: E722 = jls_extract_def()
        return render(request,'index.html',{'result':"Error",'values':values})