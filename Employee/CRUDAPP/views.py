from django.shortcuts import render, redirect, get_object_or_404
from CRUDAPP.models import Employe


def Welcome(request):
    return render(request, 'welcome.html')

# Create your views here.
def Insert_emp(request):
    if request.method == 'POST':
        nom = request.POST['nom']
        prenom = request.POST['prenom']
        email = request.POST['email']
        telephone = request.POST['telephone']
        date_naissance = request.POST['date_naissance']
        date_embauche = request.POST['date_embauche']
        poste = request.POST['poste']
        salaire = request.POST['salaire']
        adresse = request.POST['adresse']
        data = Employe(nom=nom, prenom=prenom, email=email, telephone=telephone, date_naissance=date_naissance, date_embauche=date_embauche, poste=poste, salaire=salaire, adresse=adresse)
        data.save()

        return redirect('show')
    
    else:
        return render(request, 'insert.html')
    

def Show_emp(request):
    show = Employe.objects.all()
    context = {'show':show}
    return render(request, 'show.html', context)


def Edit_emp(request,pk):
    employe = get_object_or_404(Employe, id=pk)
    if request.method == 'POST':
        employe.nom = request.POST['nom']
        employe.prenom = request.POST['prenom']
        employe.email = request.POST['email']
        employe.telephone = request.POST['telephone']
        employe.date_naissance = request.POST['date_naissance']
        employe.date_embauche = request.POST['date_embauche']
        employe.poste = request.POST['poste']
        employe.salaire = request.POST['salaire']
        employe.adresse = request.POST['adresse']
        employe.save()

        return redirect('show')
    context = {'employe':employe}
    return render(request,'edit.html', context)


def Delete_emp(request, pk):
    employe_delete = get_object_or_404(Employe, id=pk)
    if request.method == 'POST':
        employe_delete.delete()

        return render('show')
    context={'employe_delete': employe_delete}

    return render(request, 'delete.html',context)