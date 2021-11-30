from app.model.dosen import Dosen #import database dosennya dan mahasiswanya
from app.model.mahasiswa import Mahasiswa
from app import response, app, db #import response (behasil / gagal)
from flask import request, jsonify, abort

def index(): # deff adalah function
  try:
    dosen = Dosen.query.all() # ini kalau di Oracle macem Select * from Dosen
    data = formatArray(dosen) #
    return response.success(data, "success") # ngereturn dari response.py kelas succes
  except Exception as e:
    print(e)
    
    
    
# function untuk format array nya Dosen
def formatArray(datas):
  array = []  
  for i in datas:
    array.append(singleObject(i)) # INGAT pelajaran di w3school tentang Lists, Tuples, Sets, DIctionaries ? nah ini method yang ada di Lists
                    # menambahkan di arraynya
                    # membuat Function singleDosen dulu
  return array


# function format untuk menampilkan Dosen
def singleObject(data):
  data={
    'id':data.id,
    'nidn':data.nidn,
    'nama':data.nama,
    'phone':data.phone,
    'alamat':data.alamat
  }
  return data


def detail(id):
  try:
      # Code ini sama seperti Select * from Dosen where id = :id
    dosen = Dosen.query.filter_by(id=id).first()
      # Code ini sama seperti Select * from Mahasiswa where dosen_satu = :id OR dosen_dua = :id
    mahasiswa = Mahasiswa.query.filter((Mahasiswa.dosen_satu == id) | (Mahasiswa.dosen_dua == id))
    
    if not dosen:
      return response.badRequest([], 'Tidak ada data dosen')
    
    datamahasiswa = formatMahasiswa(mahasiswa)
    data = singleDetailMahasiswa(dosen, datamahasiswa)
    
    return response.success(data, "success") # data = singleDetailMahasiswa(dosen, datamahasiswa)
  except Exception as e:
    print(e)
    

def singleDetailMahasiswa(dosen, mahasiswa):   # var mahasiswa berasal dari function formatMahasiswa yang tadi sudah dibuat
  data = {
    'id':dosen.id,
    'nidn':dosen.nidn,
    'nama':dosen.nama,
    'phone':dosen.phone,
    'mahasiswa':mahasiswa # nah function tadi itu (singleDetailMahasiswa) ditempatkan disini, jadi nested di jsonnya
  }
  return data


# Function format array nya si Mahasiswa (Podo kyk dosen lah yo metodene)    
def formatMahasiswa(data):
  array = []
  for i in data:
    array.append(singleMahasiswa(i)) # gawe Function singleMahasiswa sek. Persis gone dosen
  return array
    

def singleMahasiswa(mahasiswa): # var nya ini sama dengan value yang ada di dalam data json
  data={
    'id':mahasiswa.id,
    'nim':mahasiswa.nim,
    'nama':mahasiswa.nama,
    'phone':mahasiswa.phone
  }
  return data
    
