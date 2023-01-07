from django.shortcuts import render
from phyMath.phyMath import phyMath

m1 = phyMath()


# Create your views here.
def hellWorld(request):
    if request.method == 'GET':
        return render(request, 'helloworld.html')

def example(request):
    if request.method == 'GET':
        return render(request, 'exampleCal.html')
    if request.method == 'POST':
        x1 = request.POST.get('x1')
        x2 = request.POST.get('x2')
        x1, x2 = int(x1), int(x2)
        result = m1.simpleAdd(x1, x2)
        return render(request, 'exampleCalResult.html', {'result': result})
