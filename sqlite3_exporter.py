import sqlite3
from opentelemetry.sdk.trace.export import SpanExporter, SpanExportResult

class SQLite3SpanExporter(SpanExporter):
    def __init__(self, file_name):
        self.connection = sqlite3.connect(file_name)
        self._create_table()

    def _create_table(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS spans (
                trace_id TEXT,
                span_id TEXT,
                parent_span_id TEXT,
                name TEXT,
                start_time INTEGER,
                end_time INTEGER,
                status_code TEXT,
                status_description TEXT
            )
        """)
        self.connection.commit()

    def export(self, spans):
        cursor = self.connection.cursor()
        for span in spans:
            cursor.execute("""
                INSERT INTO spans (trace_id, span_id, parent_span_id, name, start_time, end_time, status_code, status_description)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                span.context.trace_id,
                span.context.span_id,
                span.parent.span_id if span.parent else None,
                span.name,
                span.start_time,
                span.end_time,
                span.status.status_code.name,
                span.status.description
            ))
        self.connection.commit()
        return SpanExportResult.SUCCESS

    def shutdown(self):
        self.connection.close()
