from flask import Flask, render_template, request, jsonify
from constants import constants
from helpers.utils import is_cnj_format_valid, find_court_from_cnj
from models.TjalFirstInstance import TjalFirstInstance

app = Flask(__name__)


@app.route(rule="/home", methods=["GET"])
def home():
    return render_template(
        template_name_or_list="search_form.html", title="Formulário de busca"
    )


@app.route(rule="/buscar", methods=["POST"])
def search():
    try:
        cnj = request.json["cnj"]

        if is_cnj_format_valid(cnj):
            try:
                court_code = find_court_from_cnj(cnj)

                if court_code == constants.TJAL_CODE:
                    crawler_tjal = TjalFirstInstance(
                        base_url="https://www2.tjal.jus.br/cpopg/show.do?processo.numero=",
                        cnj=cnj,
                    )

                    result_tjal = crawler_tjal.extract()
                    return (
                        jsonify(
                            message="CNJ válido para busca.",
                            data=dict(
                                primeiraInstancia=result_tjal, segundaInstancia=dict()
                            ),
                        ),
                        200,
                    )

                elif court_code == constants.TJCE_CODE:
                    pass
                else:
                    return jsonify(error="Tribunal não reconhecido."), 404
            except:
                return jsonify(error="Erro não reconhecido"), 500
        else:
            return jsonify(error="CNJ inválido para busca."), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)
    app.config["JSON_SORT_KEYS"] = False
