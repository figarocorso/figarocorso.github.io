#!/usr/bin/python
# -*- coding: utf-8 -*-

import os


ROOT_FOLDER = '/home/mjulian/coding/figarocorso.github.io/'
POST_FOLDER = ROOT_FOLDER + '_posts/day-by-day/'
IMAGE_FOLDER = ROOT_FOLDER + 'images/blog/'


def get_file_lines(filename):
    with open(POST_FOLDER + filename) as f:
        return f.readlines()


def get_post_image_urls(lines):
    image_urls = []
    for line in lines:
        image_url = get_image_url_or_none(line)
        if image_url:
            image_urls.append(image_url)

    return image_urls


def get_image_url_or_none(line):
    # TODO: Use re
    try:
        image_url_beggining = line.index('](') + 2
        image_url_ending = line.index(')')
        line.index('![')
    except ValueError:
        return None

    return line[image_url_beggining:image_url_ending]


def url_is_blog_image(url):
    return 'blog.migueljulian.com' in url and 'uploads' in url


def get_post_image(image_urls):
    for image_url in image_urls:
        if url_is_blog_image(image_url):
            return image_url
    return None


def get_image_name(url):
    return url.split('/')[-1]


def add_image_header(file_lines, image_name):
    header = "image: /images/blog/%s\n" % image_name
    file_lines.insert(3, header)


def replace_image_url(file_lines, image_name):
    needle = 'http://blog.migueljulian.com/wp-content/uploads'
    line_count = 0
    for line in file_lines:
        new_line = ''
        if needle in line:
            new_line = line.replace(needle, '/images/blog')

        if new_line:
            file_lines[line_count] = new_line

        line_count += 1


def write_file(filename, lines):
    print filename
    with open(POST_FOLDER + filename, 'w') as f:
        for line in lines:
            f.write(line)


if __name__ == "__main__":
    for filename in os.listdir(POST_FOLDER):
        file_lines = get_file_lines(filename)
        post_images = get_post_image_urls(file_lines)
        post_image = get_post_image(post_images)
        if post_image:
            image_name = get_image_name(post_image)
            add_image_header(file_lines, image_name)
            replace_image_url(file_lines, image_name)
            write_file(filename, file_lines)
