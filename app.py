from flask import Flask
from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from sqlite3_exporter import SQLite3SpanExporter

# Create a Flask app
app = Flask(__name__)

# Setup OpenTelemetry
def setup_opentelemetry():
    # Create a TracerProvider
    resource = Resource(attributes={
        "service.name": "my-flask-app"
    })
    provider = TracerProvider(resource=resource)

    # Create an SQLite exporter
    exporter = SQLite3SpanExporter(file_name="telemetry.db")

    # Create a BatchSpanProcessor (can be used to process spans in batches)
    span_processor = BatchSpanProcessor(exporter)

    # Add the processor to the provider
    provider.add_span_processor(span_processor)

    # Set the global TracerProvider
    trace.set_tracer_provider(provider)

# Instrument the Flask app
FlaskInstrumentor().instrument_app(app)

# Initialize OpenTelemetry
setup_opentelemetry()

# Routes
@app.route('/')
def home():
    return "Hello, OpenTelemetry with Flask!"

@app.route('/test')
def test():
    return "This is a test route."

if __name__ == "__main__":
    app.run(debug=True)
