import requests
import random
from bs4 import BeautifulSoup
from openpyxl import Workbook


def get_content_as_text_from_url(url):
    text = requests.get(url).text
    return text


def output_courses_info_to_xlsx(output_file_path, courses_info):
    wb = Workbook()
    ws = wb.active
    ws.append(['url', 'title', 'date begin', 'week durations', 'rating'])
    for course in courses_info:
        ws.append([
            course['url'],
            course['title'],
            course['course_begin'],
            course['week_duration'],
            course['rating']
        ])
    wb.save(output_file_path)


def get_course_info(course_slug):
    course_soup = BeautifulSoup(course_slug, 'lxml')

    title_element = course_soup.find('h1', {'class': 'title display-3-text'})
    if title_element:
        title = title_element.get_text()
    else:
        title = None

    course_begin_element = course_soup.find('div', id='start-date-string')
    course_begin = None if course_begin_element is None else course_begin_element.get_text()

    weeks_elements = course_soup.find('div', {'class': 'rc-WeekView'})
    if weeks_elements:
        week_duration = len(weeks_elements.contents)
    else:
        week_duration = None

    course_rating_element = course_soup.find(
        'div', {
            'class': 'ratings-text headline-2-text'
        }
    )
    if course_rating_element:
        course_rating = course_rating_element.get_text()
    else:
        course_rating = None

    course_info = {
        'title': title,
        'course_begin': course_begin,
        'week_duration': week_duration,
        'rating': course_rating
    }

    return course_info


def get_courses_info(courses_urls):
    courses_info = []
    for course_url in courses_urls:
        course_html = get_content_as_text_from_url(course_url)

        course_info = get_course_info(course_html)
        course_info['url'] = course_url

        courses_info.append(
            course_info
        )

    return courses_info


def get_courses_list_from_feed(coursera_feed_url, qty):
    feed_xml = get_content_as_text_from_url(coursera_feed_url)
    feed_soup = BeautifulSoup(feed_xml, 'lxml')
    urls = feed_soup.findAll('loc')
    urls = [course.get_text() for course in urls]
    return random.sample(urls, qty)


if __name__ == '__main__':
    courses_qty_to_select = 20
    file_output_path = 'courses-info.xlsx'
    coursera_feed_url = 'https://www.coursera.org/sitemap~www~courses.xml'
    courses_urls = get_courses_list_from_feed(
        coursera_feed_url,
        courses_qty_to_select
    )
    courses_info = get_courses_info(courses_urls)
    output_courses_info_to_xlsx(file_output_path, courses_info)
