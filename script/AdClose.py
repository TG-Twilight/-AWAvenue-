import json

def format_domain(List):
    domain = ["#This rule is only used with AdClose", "", ""]
    for line in List:
        domain_lines = f"domain, {line.strip()}"
        domain.append(domain_lines)
    return domain


def build(rule):
    return {'list': format_domain(rule.domain_list), 'suffix': '.rule', 'comment': '#', 'total': len(rule.domain_list)}
