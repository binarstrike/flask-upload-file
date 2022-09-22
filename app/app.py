from . import me

@me.route("/")
def root_page():
    return {"data":"ini halaman root /"}