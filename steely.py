from PIL import Image

STEELY = "skull_template.png"


def main(image_path):
    background = Image.open(image_path)
    foreground = Image.open(STEELY)

    fg_w, fg_h = foreground.size
    background = background.resize(tuple(map(lambda x: int(x * .7), foreground.size)), Image.ANTIALIAS)
    bg_w, bg_h = background.size

    target = Image.new('RGB', foreground.size, 'white')
    print((abs(bg_w - fg_w) // 2, abs(bg_h - fg_h) // 3))
    target.paste(
        background,
        (abs(bg_w - fg_w) // 2, abs(bg_h - fg_h) // 10),
        background
    )
    target.paste(foreground, (0, 0), foreground)

    target.save('out.bmp')


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        'image_file',
        type=str
    )
    args = parser.parse_args()

    main(args.image_file)
