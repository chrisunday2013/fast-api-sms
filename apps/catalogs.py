import fastapi 

router = fastapi.APIRouter()


@router.get("/catalogs/:{id}")
async def read_section():
    return {"courses": []}


@router.get("/catalogs/:{id}/content-blocks")
async def read_section_content_blocks():
    return {"courses": []}


@router.get("/content-blocks/:{id}")
async def read_content_block():
    return {"courses": []}        