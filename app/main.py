from fastapi import FastAPI, Depends, Request, Form
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from starlette.status import HTTP_302_FOUND, HTTP_303_SEE_OTHER
from fastapi.middleware.cors import CORSMiddleware

from service import TasksService
import uvicorn

app = FastAPI()

app.mount('/static', StaticFiles(directory='app/static'), name='static')
templates = Jinja2Templates(directory='app/templates')

@app.get('/')
async def get_all_tasks(request: Request):
    service = TasksService()
    tasks = await service.service_get_all_tasks()
    return templates.TemplateResponse('app/layout.html', {'request': request, 'tasks_list': tasks})

@app.post('/task/create')
async def create_task(title: str = Form(...)):
    service = TasksService()
    await service.service_create_task(title)
    url = app.url_path_for('get_all_tasks')
    return RedirectResponse(url=url, status_code=HTTP_303_SEE_OTHER)

@app.get('/task/update/{task_id}')
async def update_task(task_id: int):
    service = TasksService()
    await service.service_update_complete_task(task_id)
    url = app.url_path_for('get_all_tasks')
    return RedirectResponse(url=url, status_code=HTTP_303_SEE_OTHER)

@app.get('/task/delete/{task_id}')
async def delete_task(task_id: int):
    service = TasksService()
    await service.service_delete_task(task_id)
    url = app.url_path_for('get_all_tasks')
    return RedirectResponse(url=url, status_code=HTTP_302_FOUND)

if __name__ == '__main__':
    uvicorn.run("main:app", reload=True, host='0.0.0.0', port=8000)