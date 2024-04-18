from fastapi import FastAPI, Form, File, UploadFile
from pydantic import BaseModel
from typing import Any

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None
    image: Any = None

@app.get("/create_item_form/")
async def create_item_form():
    """
    This endpoint returns an HTML form with fields based on the Item Pydantic model.
    """
    form_fields = ""
    for field_name, field_type in Item.__annotations__.items():
        field_type_str = field_type.__name__
        input_type = "text"
        if field_type_str == "float":
            input_type = "number"
        elif field_type_str == "str" and field_name == "description":
            input_type = "textarea"
        elif field_type_str == "FileUpload":
            input_type = "file"
        form_fields += f"<label>{field_name.capitalize()}:</label><br>"
        if input_type == "textarea":
            form_fields += f"<textarea name='{field_name}'></textarea><br>"
        elif input_type == "file":
            form_fields += f"<input type='{input_type}' name='{field_name}' accept='image/*'><br>"
        else:
            form_fields += f"<input type='{input_type}' name='{field_name}' {'required' if field_name != 'description' else ''}><br>"
    form_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Create Item Form</title>
    </head>
    <body>
        <h1>Create Item Form</h1>
        <form action="/items/" method="post" enctype="multipart/form-data">
            {form_fields}
            <input type="submit" value="Submit">
        </form>
    </body>
    </html>
    """
    return HTMLResponse(content=form_html, status_code=200)

@app.post("/items/")
async def create_item(item: Item = Form(...), image: UploadFile = File(None)):
    """
    This endpoint receives form data containing an Item object and an optional file upload (image).
    """
    item_dict = item.model_dump()
    return {"item_data": item_dict, "file_name": getattr(image, "filename", None)}

if __name__ == "__main__":
    import uvicorn
    from starlette.responses import HTMLResponse
    uvicorn.run(app, host="0.0.0.0", port=8000)
