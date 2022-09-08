from app.controllers import buah
from app import app

app.route("/",                 methods=["GET", "POST"])(buah.index)     (buah.index)
app.route("/delete/<buah_id>", methods=["GET"])                         (buah.delete)                                             
