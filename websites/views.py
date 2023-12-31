from django.shortcuts import render
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup as bs4

# Create your views here.

from django.shortcuts import render

def landing_page(request):
    return render(request, 'landingpage.html')

def mang_wiki(request):
    data = {
        'heading' : "Mangrove Wikipedia"
    }

    return render(request, 'mang_wiki.html', data)

def about(request):
    data = {
        "heading" : "About"
    }

    return render(request, "about.html", data)

def berita_page(request):
    beritas = []

    sumber_scrap = ["https://www.detik.com/tag/hutan-mangrove", "https://www.detik.com/tag/mangrove", "https://www.detik.com/tag/hutan-bakau?tag_from=mangrove"]

    for sumber in sumber_scrap:
        container_page = requests.get(sumber).text
        container_page_soup = bs4(container_page, "lxml")

        for artikel in container_page_soup.find_all('article'):
            berita_item = {}

            # Judul Berita
            judul_berita = artikel.find('h2', class_="title").text
            berita_item["judul_berita"] = judul_berita

            # Gambar Berita
            image_src = artikel.find('img')['src']
            berita_item["image_src"] = image_src

            # Link Berita
            link_berita = artikel.find('a')['href']
            berita_item["link_berita"] = link_berita

            # Tanggal dan Waktu Berita
            tanggal_waktu = artikel.find('span', class_="date").text
            berita_item["tanggal_waktu"] = tanggal_waktu

            # Tambahkan berita item ke daftar
            beritas.append(berita_item)


    data = {
        "heading" : "Berita", 
        "beritas" : beritas
    }

    return render(request, 'berita.html', data)

def handler404(request, exception):
    return render(request, '404.html')

def handler500(request):
    return render(request, '500.html')