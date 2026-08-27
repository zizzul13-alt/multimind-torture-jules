from fasthtml.common import *
import sys
sys.path.append('.')

from references.ref_arknights import render_arknights_proof, handle_arknights_deploy
from references.ref_noomo import render_noomo_proof
from references.ref_dioriviera import render_dioriviera_proof
from references.ref_viensla import render_viensla_proof

app, rt = fast_app()

@rt("/ref/arknights")
def get_ark():
    return render_arknights_proof()

@rt("/ref/arknights/deploy", methods=["POST"])
def post_ark_deploy():
    return handle_arknights_deploy()

@rt("/ref/noomo")
def get_noomo():
    return render_noomo_proof()

@rt("/ref/dioriviera")
def get_dior():
    return render_dioriviera_proof()

@rt("/ref/viensla")
def get_viensla():
    return render_viensla_proof()

if __name__ == '__main__':
    print("All reference routes imported cleanly!")
