import json
import os
import re

CNJ_PATTERN = r'^\d{7}-\d{2}.\d{4}.\d{1}.\d{2}.\d{4}$'


def save_json_file(data, file_name: str):
    json_object = json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False)

    if not file_name.endswith('.json'):
        file_name += '.json'

    path = os.path.join('output', file_name)
    os.makedirs('output', exist_ok=True)

    with open(path, "w", encoding='utf8') as outfile:
        outfile.write(json_object)
        outfile.close()


def remove_duplicated_space_and_line_breaks_from_cnj_input(cnj: str):
    return re.sub(pattern=r'\s+', repl=' ', string=cnj.strip())


def remove_special_symbols_from_string(string: str):
    regex_pattern = r'[\n\t]'
    return re.sub(regex_pattern, '', string)


def is_cnj_format_valid(cnj: str) -> bool:
    cnj = remove_duplicated_space_and_line_breaks_from_cnj_input(cnj)
    regex = re.compile(CNJ_PATTERN)
    return bool(regex.fullmatch(cnj))


def remove_special_symbols_from_cnj(cnj: str):
    return cnj.replace('-', '').replace('.', '')


def find_court_from_cnj_by_regex(cnj: str, court_code: str):
    return re.search(court_code, cnj)
