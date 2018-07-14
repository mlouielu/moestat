from lxml import etree


def parse_search_parameters(html):
    root = etree.HTML(html)
    pl = {}
    for select in root.xpath('//select'):
        # title = list(select.xpath('preceding-sibling::span')[0].itertext())[0]
        title = 'ListBox' + select.xpath('preceding-sibling::span')[0].get('id')[5:]
        options = list(map(lambda x: x.get('value'), select.xpath('option')))
        pl[title] = options

    return pl


def parse_aspx_state(html):
    root = etree.HTML(html)
    return {s.get('name'): s.get('value') for s in root.xpath('//input[@type="hidden"]')}
