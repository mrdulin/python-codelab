from collections import namedtuple

Post = namedtuple('Post', 'id text')


async def get_post(id: str):
    return Post(id=int(id), text='Text for the post body.')
