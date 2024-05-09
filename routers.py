import asyncio
from fastapi import APIRouter
from cats_api import download_cat_image, async_download_cat_image, status_list
router = APIRouter()

@router.get('/sync/images/download')
async def sync_download_all_images():
    quantity = sum([download_cat_image(status) for status in status_list])

    return {'message': f'{quantity} images downloaded successfully.'}

@router.get('/async/images/download')
async def async_download_all_images():
    corroutines = [async_download_cat_image(status) for status in status_list]
    await asyncio.gather(*corroutines)
    return {'message': f'{len(corroutines)} images downloaded successfully.'}