from projectapi import ProjectAPI

def get_project_title(project_json):
    """Возвращает title проекта, если он есть"""
    return project_json.get("title")

# ----------------------------
# Тест создания проекта
# ----------------------------
def test_create_project_positive():
    response = ProjectAPI.create_project("Test Project PO")
    print("Status code:", response.status_code)
    print("Response JSON:", response.json())
    
    # Проверяем, что вернулся код 201 и есть id проекта
    assert response.status_code == 201
    json_data = response.json()
    assert "id" in json_data
    project_id = json_data["id"]

    # Получаем проект по id, чтобы проверить title
    get_resp = ProjectAPI.get_project(project_id)
    print("GET status:", get_resp.status_code)
    print("GET JSON:", get_resp.json())
    assert get_resp.status_code == 200
    actual_title = get_project_title(get_resp.json())
    assert actual_title == "Test Project PO"

# ----------------------------
# Тест получения списка проектов
# ----------------------------
def test_get_project_list():
    resp = ProjectAPI.get_all_projects()  # метод должен вернуть весь список проектов
    print("Status code:", resp.status_code)
    print("Response JSON:", resp.json())
    assert resp.status_code == 200

    # Проверяем, что пришёл список внутри ключа 'content'
    json_data = resp.json()
    assert "content" in json_data
    assert isinstance(json_data["content"], list)

# ----------------------------
# Тест обновления проекта
# ----------------------------
def test_update_project():
    # Создаём проект
    create_resp = ProjectAPI.create_project("Old Project Name")
    project_id = create_resp.json()["id"]

    # Обновляем проект
    update_resp = ProjectAPI.update_project(project_id, "Updated Project Name")
    print("Update status:", update_resp.status_code)
    print("Update JSON:", update_resp.json())
    assert update_resp.status_code == 200

    # Получаем проект и проверяем title
    get_resp = ProjectAPI.get_project(project_id)
    updated_title = get_project_title(get_resp.json())
    assert updated_title == "Updated Project Name"

# ----------------------------
# Тест удаления проекта
# ----------------------------
def test_delete_project():
    # Создаём проект
    create_resp = ProjectAPI.create_project("Project To Delete")
    project_id = create_resp.json()["id"]

    # Удаляем проект
    delete_resp = ProjectAPI.delete_project(project_id)
    print("Delete status:", delete_resp.status_code)
    assert delete_resp.status_code == 204

    # Проверяем, что проект удалён
    get_resp = ProjectAPI.get_project(project_id)
    assert get_resp.status_code == 404
