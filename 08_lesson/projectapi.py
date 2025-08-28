import requests
from config import BASE_URL, HEADERS

class ProjectAPI:

    @staticmethod
    def create_project(title: str):
        """Создать проект с указанным title"""
        payload = {"title": title}
        response = requests.post(f"{BASE_URL}/projects", json=payload, headers=HEADERS)
        return response

    @staticmethod
    def update_project(project_id: str, title: str):
        """Обновить проект по id с новым title"""
        payload = {"title": title}
        response = requests.put(f"{BASE_URL}/projects/{project_id}", json=payload, headers=HEADERS)
        return response

    @staticmethod
    def get_project(project_id: str):
        """Получить проект по id"""
        response = requests.get(f"{BASE_URL}/projects/{project_id}", headers=HEADERS)
        return response

    @staticmethod
    def get_all_projects():
        """Получить список всех проектов"""
        response = requests.get(f"{BASE_URL}/projects", headers=HEADERS)
        return response

    @staticmethod
    def delete_project(project_id: str):
        """Удалить проект по id"""
        response = requests.delete(f"{BASE_URL}/projects/{project_id}", headers=HEADERS)
        return response
