from django.shortcuts import render
from django.urls import path
from . import views

#

#

urlpatterns = [
    path("", views.baz_inf, name='AAA'),
    path("Kroy", views.Kroy, name='Kr'),
    path("st_1", views.st_1, name='st_1'),
    path("st_2", views.st_2, name='st_2'),
    path("st_3", views.st_3, name='st_3'),
    path("st_4", views.st_4, name='st_4'),
    path("st_5", views.st_5, name='st_5'),
    path("st_6", views.st_6, name='st_6'),
    path("cor_g_y", views.cor_g_y, name='cor_g_y'),
    path("cor_l", views.cor_l, name='cor_l'),
    path("st_7", views.st_7, name='st_7'),
    path("st_8", views.st_8, name='st_8'),
    path("st_9", views.st_9, name='st_9'),
    path("st_10", views.st_10, name='st_10'),
    path("p_1", views.p_1, name='p_1'),
    path("Y_1", views.Y_1, name='Y_1'),
    path("Y_2", views.Y_2, name='Y_2'),
    path("Y_3", views.Y_3, name='Y_3'),
    path("Y_4", views.Y_4, name='Y_4'),
    path("purif", views.purif, name='purif'),
    path("st_11", views.st_11, name='st_11'),
    path("st_12", views.st_12, name='st_12'),
    path("st_13", views.st_13, name='st_13'),
    path("st_14", views.st_14, name='st_14'),
    path("st_15", views.st_15, name='st_15'),
    path("st_16", views.st_16, name='st_16'),
    path("NDK", views.NDK, name='NDK'),
    path("p_vzriv", views.p_vzriv, name='p_vzriv'),
    path("termi", views.termi, name='termi'),
    path("perehv", views.perehv, name='perehv'),
    path("rino", views.rino, name='rino'),
    path("razer", views.razer, name='razer'),
    path("palyba", views.P_palyba, name='palyba'),
    path("P_tel_hynt", views.P_tel_hynt, name='P_tel_hynt'),
    path("tehmar", views.tehmar, name='tehmar'),
    path("serv", views.serv, name='serv'),
    path("skvad", views.skvad, name='skvad'),
    path("S_zal_na_ze", views.S_zal_na_ze, name='S_zal_na_ze'),
    path("P_skayt", views.P_skayt, name='P_skayt'),
    path("nev_ro", views.nev_ro, name='nev_ro'),
    path("Draigo", views.Draigo, name='Draigo'),
    path("P_pervim", views.P_pervim, name='P_pervim'),
    path("hempion", views.hempion, name='hempion'),
    path("palad", views.palad, name='palad'),
    path("libr", views.libr, name='libr'),
    path("<int:pk>", views.PrintRosDetailView.as_view(), name='test_vibor'),
    path("vind", views.vind, name='vind'),
    path("P_laz", views.P_laz, name='P_laz'),
    path("P_skrit", views.P_skrit, name='P_skrit'),
    path("P_odin", views.P_odin, name='P_odin'),
    path("<int:pk>/izmen", views.PrintRosUpdateView.as_view(), name='izmen'),
    path("<int:pk>/dele", views.PrintRosDeleteView.as_view(), name='dele'),
    path("kep", views.kep, name='kep'),
    path("Htern", views.Htern, name='Htern'),
    path("kali", views.kali, name='kali'),
    ######################################################
    path("heti", views.heti, name='heti'),  ### считалка ростеров.
    #####################################################
    path("magi", views.magi, name='magi'),
    path("kapil", views.kapil, name='kapil'),
    path("ohihe", views.ohihe, name='ohihe'),
    path("dred", views.dred, name='dred'),
    path("GM_v_NDK", views.GM_v_NDK, name='GM_v_NDK'),
    path("P_hover", views.P_hover, name='P_hover'),
    path("kogoti", views.kogoti, name='kogoti'),
    path("akolit", views.akolit, name='akolit'),
    path("P_AI", views.P_AI, name='P_AI'),
    #path("<path:w>", views.baz_inf_w, name='AAA_w') ### экспериментальный уловитель фигни . возвращяет обратно на первую страницу
    #######################################################
    path("kyrs_1", views.KYRS, name='KY'),

]





