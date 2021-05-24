from time import timezone
from django.shortcuts import render, redirect
from .models import CellImage
from django.shortcuts import render, get_object_or_404
import cell.cell_predict as cell_predict

def index(request):
    # return HttpResponse("BITS")
    return render(request,'index.html')


def image_upload(request):
    cellImage = CellImage()
    cellImage.title = request.POST['title']
    cellImage.images = request.FILES['images']
    cellImage.predicted_image = str(request.FILES['images'])[:-4]+'_predicted.jpg'
    cellImage.save()

    cell_predict.predict(cellImage.images)

    return redirect('/cell/detail/' + str(cellImage.id))

def detail(request, cell_image_id):
    cell_detail = get_object_or_404(CellImage, pk=cell_image_id)
    return render(request, 'detail.html', {'cell': cell_detail})




# #
# # def detail(request):
# #     return render(request, 'detail.html')
#
# def update(request, cell_image_id):
#     cellImage = CellImage.objects.get(id=cell_image_id)
#
#     if request.method == "POST":
#         cellImage.title = request.POST['title']
#         # cellImage.body = request.POST['body']
#         cellImage.save()
#         return redirect('/cell/detail/' + str(cellImage.id))
#
#     else:
#         return render(request, 'index.html')
#
# def delete(request, cell_image_id):
#     cellImage = CellImage.objects.get(id=cell_image_id)
#     cellImage.delete()
#     return redirect('/')
#
# # def image_show(request):
# #
# #     return render(request,'detail.html')
