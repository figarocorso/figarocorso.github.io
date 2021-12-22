import os
import sys

from PIL import Image


THUMBNAIL_SIZE = (200, 200)
BIG_SIZE = (800, 800)

BLOG_PATH = "/home/figarocorso/coding/figarocorso.github.io"
IMAGE_PATH = "/images/blog/{}"
THUMBNAILS_PATH = "/images/blog/thumbnails/{}"
POSTS_PATH = "/_day_by_day/{}"

JPG_EXTENSION = "jpg"


def get_image_info(parameters):
    if len(parameters) != 2:
        show_usage_message()
        exit()

    image_location = parameters[1]
    image_full_name = os.path.basename(image_location)
    image_name = os.path.splitext(image_full_name)[0]

    return image_location, image_name


def ask_user_for_post_information():
    date = input("Date of the post (2017-08-27 format): ")
    title = input("Post title: ")
    return date, title


def show_usage_message():
    print("Usage: python create-image-post.py image-location")
    print("Gimp will be opened where you have to square your pic")
    print("and save with the same name")


def open_gimp(image_location):
    os.system("gimp -d -f -s {}".format(image_location))


def resize_image_and_save(image_location, output_name):
    image = Image.open(image_location)
    image.resize(BIG_SIZE)
    image.save(BLOG_PATH + IMAGE_PATH.format(output_name))
    image.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)
    image.save(BLOG_PATH + THUMBNAILS_PATH.format(output_name))


def create_post_file(date, title, post_filename, image_name):
    post_text = get_post_text(date, title, image_name)
    with open(BLOG_PATH + POSTS_PATH.format(post_filename), 'w') as post_file:
        post_file.write(post_text)


def get_post_text(date, title, image_name):
    post_text = '---\n'
    post_text += 'layout: post\n'
    post_text += 'category: day-by-day\n'
    post_text += "date: {}\n".format(date)
    post_text += "title: {}\n".format(title)
    post_text += "image:\n"
    post_text += "  thumbnail: {}\n".format(THUMBNAILS_PATH.format(image_name))
    post_text += "  path: {}\n".format(IMAGE_PATH.format(image_name))
    post_text += '---'

    return post_text


def add_commit(title, image_name, post_filename):
    os.system("cd {} && git add {}".format(BLOG_PATH, BLOG_PATH + THUMBNAILS_PATH.format(image_name)))
    os.system("cd {} && git add {}".format(BLOG_PATH, BLOG_PATH + IMAGE_PATH.format(image_name)))
    os.system("cd {} && git add {}".format(BLOG_PATH, BLOG_PATH + POSTS_PATH.format(post_filename)))
    os.system("cd {} && git commit -m \"{}\"".format(BLOG_PATH, title))


if __name__ == "__main__":
    image_location, image_name = get_image_info(sys.argv)
    date, title = ask_user_for_post_information()
    open_gimp(image_location)
    cleaned_title = title.lower().replace(' ', '-')
    output_image_name = "{}-{}.{}".format(date, cleaned_title, JPG_EXTENSION)
    resize_image_and_save(image_location, output_image_name)
    post_filename = "{}-{}.md".format(date, cleaned_title)
    create_post_file(date, title, post_filename, output_image_name)
    add_commit(title, output_image_name, post_filename)
