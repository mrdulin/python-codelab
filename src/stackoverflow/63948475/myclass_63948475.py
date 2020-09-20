class MyClass:

    def __init__(self, client):
        self.client = client

    def method_to_test(self):
        images = self.client.get_stuff()
        image = images[0]
        result = []
        for region in image.regions:
            result.append(region.region_id)
        return result
