import pytest

from Foo.bar import posts


@pytest.mark.asyncio
async def test_get_post_exists():
    returned_post = await posts.get_post('0')
    assert returned_post.id == 0
    assert returned_post.text == 'Text for the post body.'
    assert True == Fals
