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
    print("-------------------------------------------")
    print(str(request.POST['check_class']))
    print("-------------------------------------------")
    cellImage.title = request.POST['title']
    cellImage.images = request.FILES['images']
    img_name = str(request.FILES['images'])
    img_name = img_name[7:] if "images" in img_name else img_name
    cellImage.predicted_images = "/media/predicted_images/"+img_name
    # cellImage.save()
    # cellImage.predicted_images = cell_predict.predict(cellImage.images)
    cellImage.save()
    cell_result=cell_predict.predict(img_name,str(request.POST['check_class']))
    # return redirect('/cell/detail/' + str(cellImage.id))
    #cell_detail = get_object_or_404(CellImage)
    #return render(request, 'detail.html',{'cell':cell_detail})
    return render(request, 'detail.html',{'cell':cellImage,'cell_result':cell_result})

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
