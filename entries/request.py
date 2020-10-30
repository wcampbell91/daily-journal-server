from models.tags import Tags
import tags
from models import Journal_entries, Mood
import sqlite3
import json

def get_all_entries():
    with sqlite3.connect("./daily-journal.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.concept,
            e.entry,
            e.mood_id,
            e.date,
            m.id id,
            m.label mood
        FROM Journal_entries e
        JOIN Mood m
            ON m.id = e.mood_id
        """)

        dataset = db_cursor.fetchall()

        entries = []

        for row in dataset:
            entry = Journal_entries(row['id'], row['concept'], row['entry'],
                            row['mood_id'], row['date'])

            mood = Mood(row['mood_id'], row['mood'])

            entry.mood = mood.__dict__

            db_cursor.execute("""
            SELECT t.id, t.name FROM entry_tag e
            JOIN tag t ON t.id = e.tag_id
            WHERE e.entry_id = ?
            """, (entry.id, ))

            tagset = db_cursor.fetchall()

            tags = []

            for tag in tagset:  
                tags.append({'id': tag['id'], 'name': tag['name']})
            
            entry.tags = tags

            entries.append(entry.__dict__)


    return json.dumps(entries)

def get_single_entry(id):
    with sqlite3.connect("./daily-journal.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT 
            e.id,
            e.concept,
            e.entry,
            e.mood_id,
            e.date, 
            m.id id,
            m.label mood
        FROM Journal_entries e
        JOIN mood m 
            ON m.id = e.mood_id
        WHERE e.id = ?
        """, ( id, ))
        
        data = db_cursor.fetchone()

        entry = Journal_entries(data['id'], data['concept'], data['entry'], data['mood_id'],
                                    data['date'])

        mood = Mood(data['mood_id'], data['mood'])

        db_cursor.execute("""
        SELECT t.id, t.name FROM entry_tag e
        JOIN tag t ON t.id = e.tag_id
        WHERE e.entry_id = ?
        """, (id, ))

        tagset = db_cursor.fetchall()

        tags = []

        for tag in tagset:
            tags.append({"id": tag['id'], "name": tag['name']})

        entry.tags = tags
        entry.mood = mood.__dict__

        return json.dumps(entry.__dict__)

def search_for_entry(entry):
    with sqlite3.connect('./daily-journal.db') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(f"""
        SELECT
            e.id,
            e.concept,
            e.entry,
            e.mood_id,
            e.date
        FROM Journal_entries e
        WHERE e.entry LIKE '%{entry}%'
        """)

        entries = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            entry = Journal_entries(row['id'], row['concept'], row['entry'], row['mood_id'],
                                    row['date'])
            entries.append(entry.__dict__)

        return json.dumps(entries)

def delete_entry(id):
    with sqlite3.connect('./daily-journal.db') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Journal_entries
        WHERE id = ?
        """, (id, ))

def create_journal_entry(new_object):
    with sqlite3.connect('./daily-journal.db') as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Journal_entries
            ( concept, entry, mood_id, date )
        VALUES
            (?, ?, ?, ?)
        """, (new_object['concept'], new_object['entry'],
                new_object['mood_id'], new_object['date']))
        
        id = db_cursor.lastrowid

        for tag in new_object['tags']:
            db_cursor.execute("""
                INSERT INTO entry_tag
                    (entry_id, tag_id)
                VALUES (?,?)
                """,(id, tag)
            )
    

        new_object['id'] = id

    return json.dumps(new_object)

def update_entry(id, new_entry):
    with sqlite3.connect('./daily-journal.db') as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Journal_entries
            SET
                concept = ?,
                entry = ?,
                mood_id = ?,
                date = ?
        WHERE id = ?
        """, (new_entry['concept'], new_entry['entry'], new_entry['mood_id'],
                new_entry['date'], id))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True
