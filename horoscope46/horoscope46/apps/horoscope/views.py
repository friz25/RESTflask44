from dataclasses import dataclass

from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.template.loader import render_to_string
from django.urls import reverse
from django.shortcuts import render

zodiac_dict = {
    'aries': "Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).",
    'taurus': "Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).",
    'gemini': "Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).",
    'cancer': "Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).",
    'leo': "Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).",
    'virgo': "Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).",
    'libra': "Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).",
    'scorpio': "Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).",
    'sagittarius': "Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).",
    'capricorn': "Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).",
    'aquarius': "Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).",
    'pisces': "Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта)."
}
zodiac_types_dict = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces'],
}
'''выводит список ссылок-стихий зодиаков'''
def index2(request):
    types = list(zodiac_types_dict)
    """
    <ol>
        <li>fire</li>
        <li>earth</li>
        <li>air</li>
    </ol>
    """
    li_elements = ''
    for zodiac_type in types:
        # redirect_path = reverse('horoscope:index2', args=(zodiac_type,))
        li_elements += f"<li> <a href='{zodiac_type.title()}'>{zodiac_type.title()} </a> </li>"
    response = f"""
        <ul>
            {li_elements}
        </ul>
        """
    return HttpResponse(response)
'''выводит список ссылок-знаков зодиаков для конкретной стихии (огонь,земля,...)'''
def index3(request):
    zodiacs = list(zodiac_dict)
    """ 'fire': ['aries', 'leo', 'sagittarius']
    <ol>
        <li>aries</li>
        <li>leo</li>
        <li>sagittarius</li>
    </ol>
    """
    li_elements = ''
    for sign in zodiac_types_dict[request]:
        redirect_path = reverse('horoscope:horoscope-name', args=(sign,))
        li_elements += f"<li> <a href='{redirect_path}'>{sign} </a> </li>"
    response = f"""
        <ul>
            {li_elements}
        </ul>
        """
    return HttpResponse(response)
'''Выводит список ссылок-знаков задиаков'''
def index(request):
    zodiacs = list(zodiac_dict)
    """
    <ol>
        <li>aries</li>
        <li>taurus</li>
        <li>geminin</li>
    </ol>
    """
    li_elements = ''
    for sign in zodiacs:
        redirect_path = reverse('horoscope:horoscope-name', args=(sign,))
        li_elements += f"<li> <a href='{redirect_path}'>{sign.title()} </a> </li>"
    response = f"""
    <ul>
        {li_elements}
    </ul>
    """
    return HttpResponse(response)

'''Выводит список ссылок-знаков задиаков (на стороне HTML)'''
def index0(request):
    zodiacs = list(zodiac_dict)
    # f"<li> <a href='{redirect_path}'>{sign.title()} </a> </li>"
    context={
        'zodiacs':zodiacs,
        'zodiac_dict':[],
    }
    return render(request, 'horoscope/index.html', context=context)

@dataclass
class Person:
    name: str
    age: int

def get_info_about_zodiacs(request, zodiac_sign: str):
    '''
    if zodiac_sign == 'leo':
        return HttpResponse("<h1>Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).</h1>")
    elif zodiac_sign == 'scorpio':
        return HttpResponse("<h1>Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).</h1>")
    elif zodiac_sign == 'taurus':
        return HttpResponse("<h1>Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).</h1>")
    '''
    description = zodiac_dict.get(zodiac_sign.lower())
    zodiacs = list(zodiac_dict)
    if description:
        # return HttpResponse(description)
        data = {
            'description':description,
            'sign':zodiac_sign,
            'sign_name':description.split()[0],
            'zodiacs': zodiacs,
            'my_int':111,
            'my_float':111.5,
            'my_list': [1,2,3],
            'my_tuple': (1,2,3,4,5),
             'my_dict': {'name': 'Jack', 'age': 40},
             'my_class': Person('Victor', 18),
                }
        return render(request, 'horoscope/info_zodiac.html', context=data)
    elif zodiac_types_dict.get(zodiac_sign.lower()):
        return index3(zodiac_sign.lower())
    else:
        return HttpResponseNotFound(f"<h1>Неизвестный знак зодиака - {zodiac_sign} !</h1>")
    # response = render_to_string('horoscope/info_zodiac.html')
    # return HttpResponse(response)


def get_info_about_zodiacs_by_number(request, zodiac_sign: int):
    zodiacs = list(zodiac_dict)
    if zodiac_sign > len(zodiacs):
        return HttpResponseNotFound(f"<h1>Неправильный порядковый номер зодиака - {zodiac_sign} !</h1>")
    name_zodiac = zodiacs[zodiac_sign - 1]
    redirect_url = reverse('horoscope:horoscope-name', args=(name_zodiac,))
    return HttpResponseRedirect(redirect_url)


def get_info_by_date(request, month, day):
    return HttpResponse(f'<h1>Month {month} \n Day {day}</h1>')
