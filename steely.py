from PIL import Image

STEELY = "skull_template.png"

__RATIO__ = .7


def main(image_path, ratio):
    background = Image.open(image_path)
    foreground = Image.open(STEELY)

    fg_w, fg_h = foreground.size
    background = background.resize(tuple(map(lambda x: int(x * ratio), foreground.size)), Image.ANTIALIAS)
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
    parser.add_argument(
        '-r',
        '--ratio',
        type=float,
        help="Size ratio for image provided. Default is .7",
        default=.7
    )
    args = parser.parse_args()

    main(args.image_file, args.ratio)
