from aiohttp import web
import json

ads = []


async def create_ad(request):
    data = await request.json()
    ads.append(data)
    return web.json_response({'message': 'Ad created successfully'})


async def get_ads(request):
    return web.json_response(ads)


async def delete_ad(request):
    index = int(request.match_info['index'])

    if index < len(ads):
        ads.pop(index)
        return web.json_response({'message': 'Ad deleted successfully'})
    else:
        return web.json_response({'error': 'Ad not found'})


app = web.Application()
app.router.add_post('/ads', create_ad)
app.router.add_get('/ads', get_ads)
app.router.add_delete('/ads/{index}', delete_ad)

web.run_app(app)
