from django import template

register = template.Library()

@register.filter(name='chunks')
def chunks(data_list, chunk_size):
    chunk = []
    i = 1
    for data in data_list:
        chunk.append(data)
        i += 1
        if i == chunk_size:
            yield chunk
            i = 0
            chunk = []
    if chunk:
        yield chunk