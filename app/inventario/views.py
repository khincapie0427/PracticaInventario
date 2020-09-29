from django.shortcuts import render, redirect
from .models import Producto

def index(request):

#Es la página principal, si sen envía un método POST, se obtiene los datos de la petición, se crea un objeto de Produto y se guarda en la base de datos
    if request.method == 'POST':

        #Si no encontramos el nombre en la request entonces le asignamos -1, lo que significa que posttearon un CSV
        nombre = request.POST.get('nombre', '-1')
        cantidad = request.POST.get('cantidad')
        precio = request.POST.get('precio')
        comentario = request.POST.get('comentario')  
        if nombre != '-1':     
            #Se crea el objeto de la base de datos y se guarda con los datos que nos llegan en la request
            Producto(nombre=nombre,cantidad=cantidad,precio=precio,comentario=comentario).save()
        else:

            #Postearon un CSV, se lee el archivo y se guarda en la base de datos
            csv = request.FILES['csv'].read().decode('utf-8')
            
            #Recorremos el csv
            for i in csv.split('\n'):
                row = i.split(',')
                try:
                    #Se guarda el producto
                    Producto(nombre=row[0],cantidad=row[1],precio=row[2],comentario=row[3]).save()
                except:
                    pass



    #Si recibe un get, se obtienen todos los productos y se renderiza el archivo index.html
    context = {'productos':Producto.objects.all()}
    return render(request,'index.html', context=context)



def delete(request,id):
    #Se busca el objeto por id desde la base de datos
    obj = Producto.objects.get(id=id)
    #Elimina el objeto
    obj.delete()
    #Se redirige al index
    return redirect('index')


def edit(request,id):

    #Si la petición es POST, busca los datos de la petición y los edita en el objeto correspondiente

    if request.method == 'POST':

       
       #Obtenemos los valores de la pretición del usuario
        nombre = request.POST.get('nombre')
        cantidad = request.POST.get('cantidad')
        precio = request.POST.get('precio')
        comentario = request.POST.get('comentario')


        #Obtenemos el objeto de la base de datos con ese ID
        pro = Producto.objects.get(id=id)

        #Sobreescribimos los valores actuales con los que nos llegaron de la petición
        pro.nombre = nombre
        pro.cantidad = cantidad
        pro.precio = precio
        pro.comentario = comentario

        #Guardamos el objeto
        pro.save()

        #Redireccionamos al usuario al index
        return redirect('index')

    obj = Producto.objects.get(id=id)
    return render(request,'edit.html', context={'data':obj})