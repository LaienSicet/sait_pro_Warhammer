from multiprocessing.reduction import register

from django.shortcuts import render, redirect
from .models import Ros
from .forms import RosForm
from django.views.generic import DetailView, UpdateView, DeleteView





A = Ros.objects.all()



def dekor(a):
    def b(*b1):
        global A
        A = Ros.objects.all()
        return a(*b1)
    return b
########################################################################## экспериментальные "щёты" для ростеров
def heti(request):
    B = []
    A = Ros.objects.all()
    for i in A:
        R2 = i.r.split(" ")
        R3 = []
        for k in R2:
            if "\n" in k:
                k1 = k.split("\n")
                for p in k1:
                    R3.append(p)
            else:
                R3.append(k)
        sy = 0
        for l in R3:
            l1 = l.replace('.', '').replace(',', '').replace('(', '').replace(')', '').replace('+', '')
            try:
                sy += int(l1)
            except:
                pass
        B.append([i, sy])
    return render(request, 'roster_1/heti.html', {'A': A, 'B': B})
##############################################################################
#
def fil_sym(i):
    R = i.split(" ")
    R2 = []
    for k in R:
        if "\n" in k:
            k1 = k.split("\n")
            for p in k1:
                R2.append(p)
        else:
            R2.append(k)
    sy = 0
    for l in R2:
        l1 = l.replace('.', '').replace(',', '').replace('(', '').replace(')', '').replace('+', '')
        try:
            sy += int(l1)
        except:
            pass
    return sy
#






class PrintRosDetailView(DetailView):
    model = Ros
    A = Ros.objects.all()
    template_name = 'roster_1/RO.html'
    context_object_name = 'a'
    extra_context = {'A': A}



class PrintRosUpdateView(UpdateView):
    model = Ros
    A = Ros.objects.all()
    template_name = 'roster_1/nev_ro.html'
    extra_context = {'A': A}
    context_object_name = 'a'
    form_class = RosForm


class PrintRosDeleteView(DeleteView):
    model = Ros
    success_url = '/'
    A = Ros.objects.all()
    template_name = 'roster_1/pyt_na_del.html'
    extra_context = {'A': A}
    context_object_name = 'a'


@ dekor
def baz_inf(request):
    return render(request, 'roster_1/nahalo.html', {'A': A})


def baz_inf_w(request, w):
    return render(request, 'roster_1/nahalo.html', {'A': A})


# 'S': ['1', '2', '3', '4', '5', '6'], 'S0': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']


@ dekor
def nev_ro(request):
    form = RosForm()
    ohi = ''
    if request.method == 'POST':
        from roster.roster_1.forms import RosForm
        form = RosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AAA')
        else:
            ohi = "что-то пошло нетак."
    return render(request, 'roster_1/nev_ro.html', {'A': A, 'form': form, 'ohi': ohi})



def Kroy(request):

    return render(request, 'roster_1/kroy.html', {'A': A,  'C': ['1', '2'], 'S': ['1', '2', '3', '4', '5', '6'],
                                                  'S0': ['1', '2', '4','7', '8', '11']})

def Draigo(request):
    return render(request, 'roster_1/Draigo.html', {'A': A, 'C': ['1', '2'],
                                                    'S': ['1', '2', '3', '4', '5', '6'],
                                                    'S0': ['1', '2', '3', '4', '5', '7', '8', '11']})

def magi(request):
    return render(request, 'roster_1/magi.html', {'A': A, 'C': ['1', '2'],
                                                  'S': ['1', '2', '3', '4', '5', '6'],
                                                  'S0': ['1', '2', '3', '4', '5', '7', '8', '11']})

def libr(request):
    return render(request, 'roster_1/libr.html', {'A': A, 'C': ['1', '2'],
                                                  'S': ['1', '2', '3', '4', '5', '6'],
                                                  'S0': ['1', '2', '3', '4', '7', '8', '11']})


def kep(request):
    return render(request, 'roster_1/kep.html', {'A': A, 'C': ['1', '2'],
                                                 'S': ['1', '2', '3', '4', '5', '6'],
                                                 'S0': ['1', '2', '3', '4', '7', '8',  '11']})

def kapil(request):
    return render(request, 'roster_1/kapil.html', {'A': A, 'C': ['1', '2'],
                                                   'S': ['1', '2', '3', '4', '5', '6'],
                                                   'S0': ['1', '2', '3', '4', '7', '8',  '11']})

def Htern(request):
    return render(request, 'roster_1/Htern.html', {'A': A, 'C': ['1', '2'],
                                                   'S': ['1', '2', '3', '4', '5', '6'],
                                                   'S0': ['1', '2', '3', '4', '7', '8',  '11']})


def purif(request):
    return render(request, 'roster_1/pyrifaer.html', {'A': A, 'C': ['1'], 'S': ['1', '2', '3', '4', '5', '6'],
                                                      'S0': ['1', '2', '4', '5', '7', '8', '9', '11']})


def NDK(request):
    return render(request, 'roster_1/NDK.html', {'A': A, 'C': ['1', '3'], 'S': ['1', '2', '3', '4', '5', '6'],
                                                 'S0': ['1', '2',  '4', '6', '7', '8', '11']})

def GM_v_NDK(request):
    return render(request, 'roster_1/GM_v_NDK.html', {'A': A, 'C': ['1', '3'], 'S': ['1', '2', '3', '4', '5', '6'],
                                                 'S0': ['1', '2', '3', '4', '6', '7', '8', '11']})

def termi(request):
    return render(request, 'roster_1/terminatori.html', {'A': A, 'C': ['1'],
                                                         'S': ['1', '2', '3', '4', '5', '6'],
                                                         'S0': ['1', '2', '4', '5', '7', '8', '11']})


def akolit(request):
    return render(request, 'roster_1/akolit.html', {'A': A, 'C': [], 'S': [],
                                                    'S0': ['1', '2', '4', '5', '7', '8', '9', '11']})


def palad(request):
    return render(request, 'roster_1/palad.html', {'A': A, 'C': ['1'],
                                                         'S': ['1', '2', '3', '4', '5', '6'],
                                                         'S0': ['1', '2', '4', '5', '8', '7', '11']})


def perehv(request):
    return render(request, 'roster_1/perehv.html', {'A': A, 'C': ['1'], 'S': ['1', '2', '3', '4', '5', '6'],
                                                    'S0': ['1', '2', '4', '5','7', '8', '9', '11']})

def rino(request):
    return render(request, 'roster_1/rino.html', {'A': A, 'C': ['3', '4'], 'S': ['5'],
                                                  'S0': ['1', '2', '4', '6', '7', '8', '10']})


def razer(request):
    return render(request, 'roster_1/razer.html', {'A': A, 'C': ['3'], 'S': ['5'],
                                                   'S0': ['1', '2', '4', '6', '7', '8', '10']})


def kogoti(request):
    return render(request, 'roster_1/kogoti.html', {'A': A, 'C': ['3', '11'], 'S': ['5'],
                                                    'S0': ['1', '2', '4', '6', '7', '8']})

def dred(request):
    return render(request, 'roster_1/dred.html', {'A': A, 'C': ['10'], 'S': ['1', '2', '3', '4', '5', '6'],
                                                  'S0': ['1', '2', '4', '6', '7', '8', '10']})

def tehmar(request):
    return render(request, 'roster_1/tehmar.html', {'A': A,  'C': ['1', '2'], 'S': ['1', '2', '3', '4', '5', '6'],
                                                    'S0': ['1', '2', '3', '4', '7', '8', '9', '11']})

def hempion(request):
    return render(request, 'roster_1/hempion.html', {'A': A, 'C': ['1', '2', '6'], 'S': ['1', '2', '3', '4', '5', '6'],
                                                     'S0': ['1', '2', '4', '7', '8', '11']})


def vind(request):
    return render(request, 'roster_1/vind.html', {'A': A, 'C': ['7', '8', '9'], 'S': [],
                                                  'S0': ['1', '2', '3', '4', '7', '8', '10' '11']})

def kali(request):
    return render(request, 'roster_1/kali.html', {'A': A, 'C': ['1', '6', '7', '9'], 'S': [],
                                                  'S0': ['1', '2',  '4', '7', '8', '11']})


def serv(request):
    return render(request, 'roster_1/servitor.html', {'A': A, 'C': [], 'S': ['5'],
                                                      'S0': ['1', '2', '4', '7', '8', '9', '11']})


def skvad(request):
    return render(request, 'roster_1/skvad.html', {'A': A, 'C': ['1', '5'], 'S': ['1', '2', '3', '4', '5', '6'],
                                                   'S0': ['1', '2', '4', '5', '7', '8', '9', '11']})

def ohihe(request):
    return render(request, 'roster_1/ohihe.html', {'A': A, 'C': ['1'], 'S': ['1', '2', '3', '4', '5', '6'],
                                                   'S0': ['1', '2', '4', '5', '7', '8', '9', '11']})

def st_1(request):
    return render(request, 'roster_1/PRAVILA.html', {'A': A, 'pravila': "1"})

def st_2(request):
    return render(request, 'roster_1/PRAVILA.html',  {'A': A, 'pravila': "2"})

def st_3(request):
    return render(request, 'roster_1/PRAVILA.html',  {'A': A, 'pravila': "3"})

def st_4(request):
    return render(request, 'roster_1/PRAVILA.html',  {'A': A, 'pravila': "4"})

def st_5(request):
    return render(request, 'roster_1/PRAVILA.html',  {'A': A, 'pravila': "5"})

def st_6(request):
    return render(request, 'roster_1/PRAVILA.html',  {'A': A, 'pravila': "6"})

def cor_g_y(request):
    return render(request, 'roster_1/PRAVILA.html',  {'A': A, 'pravila': "7"})

def cor_l(request):
    return render(request, 'roster_1/PRAVILA.html',  {'A': A, 'pravila': "8"})

def st_7(request):
    return render(request, 'roster_1/PRAVILA.html',  {'A': A, 'pravila': "9"})

def st_8(request):

    return render(request, 'roster_1/PRAVILA.html',  {'A': A, 'pravila': "10"})

def st_9(request):
    return render(request, 'roster_1/PRAVILA.html',  {'A': A, 'pravila': "11"})

def st_10(request):
    return render(request, 'roster_1/PRAVILA.html',  {'A': A, 'pravila': "12"})

def p_1(request):
    return render(request, 'roster_1/PRAVILA.html',  {'A': A, 'pravila': "13"})

def Y_1(request):
    return render(request, 'roster_1/PRAVILA.html',  {'A': A, 'pravila': "14"})

def Y_2(request):
    return render(request, 'roster_1/PRAVILA.html',  {'A': A, 'pravila': "15"})

def Y_3(request):
    return render(request, 'roster_1/PRAVILA.html',  {'A': A, 'pravila': "16"})

def Y_4(request):
    return render(request, 'roster_1/PRAVILA.html',  {'A': A, 'pravila': "17"})

def st_11(request):
    return render(request, 'roster_1/PRAVILA.html',  {'A': A, 'pravila': "18"})

def st_12(request):
    return render(request, 'roster_1/PRAVILA.html',  {'A': A, 'pravila': "19"})

def st_13(request):
    return render(request, 'roster_1/PRAVILA.html',  {'A': A, 'pravila': "20"})

def st_14(request):
    return render(request, 'roster_1/PRAVILA.html',  {'A': A, 'pravila': "21"})

def st_15(request):
    return render(request, 'roster_1/PRAVILA.html',  {'A': A, 'pravila': "22"})


def st_16(request):
    return render(request, 'roster_1/PRAVILA.html',  {'A': A, 'pravila': "23"})


def p_vzriv(request):
    return render(request, 'roster_1/PRAVILA.html',  {'A': A, 'pravila': "24"})


def P_palyba(request):
    return render(request, 'roster_1/PRAVILA.html',  {'A': A,  'pravila': "25"})


def P_tel_hynt(request):
    return render(request, 'roster_1/PRAVILA.html',  {'A': A, 'pravila': "26"})


def S_zal_na_ze(request):
    return render(request, 'roster_1/PRAVILA.html',  {'A': A,  'pravila': "27"})


def P_skayt(request):
    return render(request, 'roster_1/PRAVILA.html',  {'A': A, 'pravila': "28"})

def P_pervim(request):
    return render(request, 'roster_1/PRAVILA.html',  {'A': A, 'pravila': "29"})

def P_laz(request):
    return render(request, 'roster_1/PRAVILA.html',  {'A': A, 'pravila': "30"})

def P_skrit(request):
    return render(request, 'roster_1/PRAVILA.html',  {'A': A, 'pravila': "31"})

def P_odin(request):
    return render(request, 'roster_1/PRAVILA.html',  {'A': A, 'pravila': "32"})

def P_hover(request):
    return render(request, 'roster_1/PRAVILA.html',  {'A': A, 'pravila': "33"})

def P_AI(request):
    return render(request, 'roster_1/PRAVILA.html',  {'A': A, 'pravila': "34"})

