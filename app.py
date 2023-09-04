import logging
from http import HTTPStatus

from flask import Flask, render_template, request, jsonify
from constants import constants
from helpers.utils import is_cnj_format_valid, find_court_from_cnj
from models.tjal_first_instance import TjalFirstInstance
from models.tjal_second_instance import TjalSecondInstance
from models.tjce_first_instance import TjceFirstInstance
from models.tjce_second_instance import TjceSecondInstance

logging.basicConfig(level=logging.DEBUG, format="[%(levelname)s] %(message)s")

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
                    crawler_tjal_first_instance = TjalFirstInstance(
                        base_url="https://www2.tjal.jus.br/cpopg/show.do?processo.numero=",
                        cnj=cnj,
                    )
                    result_tjal_first_instance = crawler_tjal_first_instance.extract()

                    crawler_tjal_second_instance = TjalSecondInstance(
                        base_url="https://www2.tjal.jus.br/cposg5/open.do",
                        cnj=cnj,
                    )
                    result_tjal_second_instance = crawler_tjal_second_instance.extract()
                    return (
                        jsonify(
                            data=dict(
                                primeiraInstancia=result_tjal_first_instance,
                                segundaInstancia=result_tjal_second_instance,
                            ),
                        ),
                        200,
                    )

                elif court_code == constants.TJCE_CODE:
                    crawler_tjce_first_instance = TjceFirstInstance(
                        base_url="https://esaj.tjce.jus.br/cpopg/show.do",
                        cnj=cnj,
                    )
                    result_for_first_instance = crawler_tjce_first_instance.extract()

                    crawler_tjce_second_instance = TjceSecondInstance(
                        base_url="https://esaj.tjce.jus.br/cposg5/open.do",
                        cnj=cnj,
                    )

                    result_for_second_instance = crawler_tjce_second_instance.extract()
                    return (
                        jsonify(
                            data=dict(
                                primeiraInstancia=result_for_first_instance,
                                segundaInstancia=dict(result_for_second_instance),
                            ),
                        ),
                        200,
                    )
                else:
                    return (
                        jsonify(error="Tribunal não reconhecido."),
                        HTTPStatus.NOT_FOUND,
                    )
            except:
                return (
                    jsonify(error="Erro não reconhecido"),
                    HTTPStatus.INTERNAL_SERVER_ERROR,
                )
        else:
            return jsonify(error="CNJ inválido para busca."), HTTPStatus.BAD_REQUEST

    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route(rule="/buscar/instancia=<int:degree>", methods=["POST"])
def search_by_instance(degree: int):
    try:
        cnj = request.json["cnj"]

        if is_cnj_format_valid(cnj):
            try:
                court_code = find_court_from_cnj(cnj)

                if court_code == constants.TJAL_CODE:
                    if degree == 1:
                        crawler_tjal_first_instance = TjalFirstInstance(
                            base_url="https://www2.tjal.jus.br/cpopg/show.do?processo.numero=",
                            cnj=cnj,
                        )
                        result_tjal_first_instance = (
                            crawler_tjal_first_instance.extract()
                        )
                        return (
                            jsonify(
                                data=dict(primeiraInstancia=result_tjal_first_instance),
                            ),
                            200,
                        )
                    elif degree == 2:
                        crawler_tjal_second_instance = TjalSecondInstance(
                            base_url="https://www2.tjal.jus.br/cposg5/open.do",
                            cnj=cnj,
                        )
                        result_tjal_second_instance = (
                            crawler_tjal_second_instance.extract()
                        )
                        return (
                            jsonify(
                                data=dict(segundaInstancia=result_tjal_second_instance),
                            ),
                            200,
                        )
                    else:
                        crawler_tjal_first_instance = TjalFirstInstance(
                            base_url="https://www2.tjal.jus.br/cpopg/show.do?processo.numero=",
                            cnj=cnj,
                        )
                        result_tjal_first_instance = (
                            crawler_tjal_first_instance.extract()
                        )
                        crawler_tjal_second_instance = TjalSecondInstance(
                            base_url="https://www2.tjal.jus.br/cposg5/open.do",
                            cnj=cnj,
                        )
                        result_tjal_second_instance = (
                            crawler_tjal_second_instance.extract()
                        )

                        return (
                            jsonify(
                                data=dict(
                                    primeiraInstancia=result_tjal_first_instance,
                                    segundaInstancia=result_tjal_second_instance,
                                ),
                            ),
                            200,
                        )

                elif court_code == constants.TJCE_CODE:
                    if degree == 1:
                        crawler_tjce_first_instance = TjceFirstInstance(
                            base_url="https://esaj.tjce.jus.br/cpopg/show.do",
                            cnj=cnj,
                        )
                        result_tjce_first_instance = (
                            crawler_tjce_first_instance.extract()
                        )
                        return (
                            jsonify(
                                data=dict(primeiraInstancia=result_tjce_first_instance),
                            ),
                            200,
                        )
                    elif degree == 2:
                        crawler_tjce_second_instance = TjceSecondInstance(
                            base_url="https://esaj.tjce.jus.br/cposg5/open.do",
                            cnj=cnj,
                        )
                        result_tjce_second_instance = (
                            crawler_tjce_second_instance.extract()
                        )
                        return (
                            jsonify(
                                data=dict(segundaInstancia=result_tjce_second_instance),
                            ),
                            200,
                        )
                    else:
                        crawler_tjce_first_instance = TjceFirstInstance(
                            base_url="https://esaj.tjce.jus.br/cpopg/show.do",
                            cnj=cnj,
                        )
                        result_tjce_first_instance = (
                            crawler_tjce_first_instance.extract()
                        )
                        crawler_tjce_second_instance = TjceSecondInstance(
                            base_url="https://esaj.tjce.jus.br/cposg5/open.do",
                            cnj=cnj,
                        )
                        result_tjce_second_instance = (
                            crawler_tjce_second_instance.extract()
                        )

                        return (
                            jsonify(
                                data=dict(
                                    primeiraInstancia=result_tjce_first_instance,
                                    segundaInstancia=result_tjce_second_instance,
                                ),
                            ),
                            200,
                        )
                else:
                    return (
                        jsonify(error="Tribunal não reconhecido."),
                        HTTPStatus.NOT_FOUND,
                    )
            except:
                return (
                    jsonify(error="Erro não reconhecido"),
                    HTTPStatus.INTERNAL_SERVER_ERROR,
                )
        else:
            return jsonify(error="CNJ inválido para busca."), HTTPStatus.BAD_REQUEST

    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
    app.config["JSON_SORT_KEYS"] = False
