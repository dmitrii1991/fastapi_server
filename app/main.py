import os
import sys
from datetime import datetime

import aiofiles
import uvicorn
from fastapi import status, FastAPI, File, UploadFile, HTTPException
from starlette.responses import FileResponse

try:
    from fastapi_server.app.settings import FILES_DIR
    from fastapi_server.app.models import FileBaseModel, FileFullModel
except ModuleNotFoundError:
    from settings import FILES_DIR
    from models import FileBaseModel, FileFullModel


app = FastAPI(
    title="Pack-file",
    description="A simple server to store files",
    version="1.0.0",
)


@app.post(
    "/file/upload/",
    response_model=FileFullModel,
    status_code=status.HTTP_200_OK,
    tags=["file"],
    summary="Download a file",
    response_description="The downloaded file",
)
async def upload(file: UploadFile = File(...)):
    if file:
        file_bytes = file.file.read()
        filename = file.filename
        name, expansion = filename.split('.')
        now = datetime.now()
        size = round(sys.getsizeof(file_bytes) / 1024 / 1024, 2)  # megabytes

        if not os.path.exists(FILES_DIR):
            os.mkdir(FILES_DIR)

        file_dir = FILES_DIR + '/'
        file_path = file_dir + filename

        async with aiofiles.open(file_path, 'wb+') as new_file:
            await new_file.write(file_bytes)
        return FileFullModel(full_name=filename, name=name, expansion=expansion, size=size, date_change=now)


@app.get(
    "/file/status/",
    response_model=FileFullModel,
    status_code=status.HTTP_200_OK,
    tags=["file"],
    summary="Get status of file",
    response_description="Status of file",
)
async def filestatus(filename: FileBaseModel):
    filename_path = os.path.join(FILES_DIR, filename.full_name)
    if os.path.exists(filename_path):
        if '.' in filename.full_name:
            name, expansion = filename.full_name.split('.')
        else:
            name, expansion = filename.full_name, ''
        size = round(os.path.getsize(filename_path) / 1024 / 1024, 2)  # megabytes
        time = datetime.fromtimestamp(os.path.getmtime(filename_path))
        return FileFullModel(
            full_name=filename.full_name,
            name=name,
            expansion=expansion,
            size=size,
            date_change=time
        )
    raise HTTPException(status_code=404, detail="File not found")


@app.get(
    "/file/download/{filename}",
    status_code=status.HTTP_200_OK,
    tags=["file"],
    summary="Get status of file",
    response_description="Status of file",
)
async def download(filename: str):
    filename_path = os.path.join(FILES_DIR, filename)
    if os.path.exists(filename_path):
        return FileResponse(
            path=filename_path,
            media_type='application/octet-stream',
        )
    raise HTTPException(status_code=404, detail="File not found")


@app.delete(
    "/file/delete/{filename}",
    response_model=FileFullModel,
    status_code=status.HTTP_200_OK,
    tags=["file"],
    summary="Delete file",
    response_description="The Deleted file"
)
async def delete(filename: str):
    filename_path = os.path.join(FILES_DIR, filename)
    if os.path.exists(filename_path):
        name, expansion = filename.split('.')
        size = round(os.path.getsize(filename_path) / 1024 / 1024, 2)  # megabytes
        time = datetime.now()
        os.remove(filename_path)
        return FileFullModel(
            full_name=filename,
            name=name,
            expansion=expansion,
            size=size,
            date_change=time,
            detail="deleted"
        )
    else:
        raise HTTPException(status_code=404, detail="File not found")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
