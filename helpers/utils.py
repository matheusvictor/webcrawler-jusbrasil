import re

CNJ_PATTERN = r'^\d{7}-\d{2}.\d{4}.\d{1}.\d{2}.\d{4}$'


def remove_duplicated_space_and_line_breaks_from_cnj_input(cnj: str):
    return re.sub(pattern=r'\s+', repl=' ', string=cnj.strip())


def is_cnj_format_valid(cnj: str) -> bool:
    cnj = remove_duplicated_space_and_line_breaks_from_cnj_input(cnj)
    regex = re.compile(CNJ_PATTERN)
    return bool(regex.fullmatch(cnj))


def remove_special_symbols_from_cnj(cnj: str):
    return cnj.replace('-', '').replace('.', '')


def extract_metadata_from_cnj(cnj: str):
    cnj_parts = cnj.split(sep='.')
    a = cnj_parts[0].split(sep='-')[1]
    print(cnj_parts, a)


def find_court_from_cnj_by_regex(cnj: str, court_code: str):
    match = re.search(court_code, cnj)
    return match.group()
