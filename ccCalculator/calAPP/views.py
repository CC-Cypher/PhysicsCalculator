from django.shortcuts import render
from phyMath.phyMath import Bin2CSV

m1 = Bin2CSV('./Resources/test.bin')


# Create your views here.
def hellWorld(request):
    if request.method == 'GET':
        m1.transform('./Result/test.txt')
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

def cal1(request):
    if request.method == 'GET':
        return render(request, 'cal1-put.html')
    if request.method == 'POST':
        filePath = request.POST.get('filepath')
        pnumber = int(request.POST.get('pnumber'))
        print(request.FILES)
        fileObject = request.FILES.get('filename')
        print(fileObject)
        dataset = open('./localData/' + fileObject.name, 'wb')
        for chunk in fileObject.chunks():
            dataset.write(chunk)
        dataset.close()
        # result = edfs.put('./localData/' + fileObject.name, filePath, pnumber)
        # print(result)
        # files = edfs.ls(filePath)['data']
        # return render(request, 'edfs2-ls.html', {'msg': result[0], 'path': filePath, 'queryset': files})
        #
        # ###############################
        # # edfs = EDFSURL()
        # requestPath = request.POST.get('filepath')
        # # requestPath = requestPath if requestPath else '/'
        # pnumber = request.POST.get('pnumber')
        #
        # ans = edfs.readPartition(requestPath, int(pnumber))
        # msg = ans['success']
        # result = ans['data']
        # if msg[0] == 'Read Partition Success':
        #     # pd.set_option('colheader_justify', 'center')
        #     return render(request, 'edfs2-readpart-result.html', \
        #                   {'msg': msg[0], 'table': result.to_html(classes="table table-bordered table-hover")})
        # else:
        #     return render(request, 'edfs2-cat-result.html', \
        #                   {'msg': msg[0], 'table': 'Incorrect input'})
