from pydantic import BaseModel
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None
    image: UploadFile = None

@router.get("/create_item_form/", response_class=HTMLResponse)
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
        elif field_type_str == "UploadFile":
            input_type = "file"
        form_fields += f"<label>{field_name.capitalize()}:</label><br>"
        if input_type == "textarea":
            form_fields += f"<textarea name='{field_name}'></textarea><br>"
        else:
            form_fields += f"<input type='{input_type}' name='{field_name}' {'required' if field_name != 'description' else ''}><br>"
    html_content = f"""
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
    return HTMLResponse(content=html_content, status_code=200)