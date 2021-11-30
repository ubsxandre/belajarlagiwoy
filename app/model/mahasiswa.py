from app import db    # ngimport var db dari folder app
from app.model.dosen import Dosen # ngimport kelas 'Dosen' dari path app/model/dosen

class Mahasiswa(db.Model):
  id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
  nim = db.Column(db.String(30), nullable=False)
  nama = db.Column(db.String(100), nullable=False)
  phone = db.Column(db.String(13), nullable=False)
  alamat = db.Column(db.String(100), nullable=False)
  dosen_satu = db.Column(db.BigInteger, db.ForeignKey(Dosen.id))
  dosen_dua = db.Column(db.BigInteger, db.ForeignKey(Dosen.id))
  
  def __repr__(self):
      return '<Mahasiswa {}>'.format(self.name) # return ke Dosen {Andreas} misalnya
  