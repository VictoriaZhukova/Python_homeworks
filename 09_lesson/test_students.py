from sqlalchemy import text

def test_add_student(db):
    # Добавляем студента
    insert_query = text("""
        INSERT INTO student (level, education_form, subject_id)
        VALUES (:level, :education_form, :subject_id)
        RETURNING user_id
    """)
    result = db.execute(insert_query, {"level": "1", "education_form": "online", "subject_id": 101})
    user_id = result.scalar()
    db.commit()

    # Проверяем, что студент добавлен
    select_query = text("SELECT level, education_form, subject_id FROM student WHERE user_id = :user_id")
    student = db.execute(select_query, {"user_id": user_id}).fetchone()
    assert student == ("1", "online", 101)

    # Чистим за собой
    db.execute(text("DELETE FROM student WHERE user_id = :user_id"), {"user_id": user_id})
    db.commit()


def test_update_student(db):
    # Добавляем студента
    result = db.execute(text("""
        INSERT INTO student (level, education_form, subject_id)
        VALUES ('2', 'offline', 102)
        RETURNING user_id
    """))
    user_id = result.scalar()
    db.commit()

    # Обновляем данные
    db.execute(text("""
        UPDATE student SET level = :level, education_form = :education_form
        WHERE user_id = :user_id
    """), {"level": "3", "education_form": "online", "user_id": user_id})
    db.commit()

    # Проверяем обновление
    student = db.execute(text("SELECT level, education_form FROM student WHERE user_id = :user_id"), {"user_id": user_id}).fetchone()
    assert student == ("3", "online")

    # Чистим за собой
    db.execute(text("DELETE FROM student WHERE user_id = :user_id"), {"user_id": user_id})
    db.commit()


def test_delete_student(db):
    # Добавляем студента
    result = db.execute(text("""
        INSERT INTO student (level, education_form, subject_id)
        VALUES ('1', 'offline', 103)
        RETURNING user_id
    """))
    user_id = result.scalar()
    db.commit()

    # Удаляем
    db.execute(text("DELETE FROM student WHERE user_id = :user_id"), {"user_id": user_id})
    db.commit()

    # Проверяем, что студента больше нет
    student = db.execute(text("SELECT user_id FROM student WHERE user_id = :user_id"), {"user_id": user_id}).fetchone()
    assert student is None
