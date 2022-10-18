from yt_contate.pipeline.steps.get_video_list import GetVideoList
from yt_contate.pipeline.steps.step import StepException
from yt_contate.pipeline.pileline import Pileline

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'


def main():
    inputs = {
        'channel_id': CHANNEL_ID
    }
    steps = [
        GetVideoList(),
    ]

    p = Pileline(steps)
    p.run(inputs)


if __name__ == '__main__':
    main()
